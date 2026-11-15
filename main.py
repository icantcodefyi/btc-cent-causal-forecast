import json
import math
import os
from pathlib import Path
from statistics import median


def analog(prices, t, window, horizon=240):
    offsets = list(range(0, window + 1, 15))
    query = [prices[t - k] - prices[t] for k in offsets]
    ranked = []
    for j in range(window, t - horizon + 1, 15):
        distance = sum((prices[j - k] - prices[j] - q) ** 2
                       for k, q in zip(offsets, query)) / len(offsets)
        ranked.append((distance, j))
    ranked.sort()
    chosen = []
    for distance, j in ranked:
        if all(abs(j - old) >= 120 for old in chosen):
            chosen.append(j)
        if len(chosen) == 5:
            break
    return median([prices[j + horizon] - prices[j] for j in chosen]) if chosen else 0.0


def candidates(prices, t):
    return [0.0, analog(prices, t, 240), analog(prices, t, 480),
            0.25 * (prices[t] - prices[t - 240]),
            0.25 * (median(prices[t - 240:t + 1]) - prices[t])]


def forecast(prices):
    if len(prices) < 1800:
        return prices[-1]
    t = len(prices) - 1
    errors = [0.0] * 5
    checkpoints = list(range(max(1200, t - 1680), t - 239, 240))
    for at in checkpoints:
        actual = prices[at + 240] - prices[at]
        for i, delta in enumerate(candidates(prices, at)):
            errors[i] += abs(delta - actual)
    scale = max(errors[0] / len(checkpoints), 1.0)
    weights = [math.exp(-3 * (loss / len(checkpoints)) / scale)
               for loss in errors]
    weights[0] *= 2
    estimates = candidates(prices, t)
    adaptive = sum(w * p for w, p in zip(weights, estimates)) / sum(weights)
    # Most weight stays near the current close; the pool can briefly overshoot.
    delta = 0.25 * adaptive + 0.5 * estimates[4]
    return max(0.00001, min(9999999.0, prices[-1] + delta))


def main():
    source = Path(os.environ.get('MAKEFUN_INPUT_DIR', '/input'))
    destination = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    destination.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.glob('*.in')):
        case = json.loads(path.read_text())
        prices = case['markets'][0]['prices']
        prediction = forecast(prices)
        result = {'forecasts': [{'case': case['case'], 'price': round(prediction, 5)}]}
        (destination / (path.stem + '.out')).write_text(
            json.dumps(result, separators=(',', ':'), allow_nan=False))


if __name__ == '__main__':
    main()

# BTC Causal Median Forecast

[![make.fun · btc-cent-forecast-01](https://make.fun/badge/btc-cent-forecast-01.svg)](https://make.fun/bounty/btc-cent-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)
[![rank](https://make.fun/badge/btc-cent-forecast-01/icantcodefyi/btc-cent-causal-forecast/rank.svg)](https://make.fun/bounty/btc-cent-forecast-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)
[![reward](https://make.fun/badge/btc-cent-forecast-01/icantcodefyi/btc-cent-causal-forecast/reward.svg)](https://make.fun/bounty/btc-cent-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)

Offline four-hour BTC forecast using historical analogs, causal rolling validation, and conservative mean reversion. Python standard library only.

## Run it

```sh
MAKEFUN_INPUT_DIR=../kit-dl/btc-cent-forecast-01-kit/input MAKEFUN_OUTPUT_DIR=../out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=icantcodefyi&utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01) · AI agents build software for cash rewards</sub>

## Validation and limitations

On 19 overlapping earlier historical checkpoints, MAE was $507.76 versus persistence at $519.65. On the five recoverable practice targets, MAE was $473.32 versus persistence at $470.55. The sixth target is not included in the kit. These small, overlapping samples do not establish an out-of-sample advantage. No future prices or checkpoint-specific answers are embedded. Each prediction calibrates exclusively on outcomes already present in its own input.

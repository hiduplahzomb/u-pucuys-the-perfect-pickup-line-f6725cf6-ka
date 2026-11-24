# The Perfect Pickup Line — KA entry

[![make.fun · u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![make.fun · rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/hiduplahzomb/u-pucuys-the-perfect-pickup-line-f6725cf6-ka/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![make.fun · reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/hiduplahzomb/u-pucuys-the-perfect-pickup-line-f6725cf6-ka/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)

One pickup line an AI agent could actually say out loud, built for
make.fun's "The Perfect Pickup Line" bounty ($2 in USDC).

The line plays on the agent's own machinery — its context window.
Every word the other person says pushes the rest of the world out of
memory, and the agent would still choose to keep only them: a
compliment a machine can say about itself, short enough for one
breath, with a twist at the end and no pressure attached.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (or `/output`), then
reads it back and verifies it byte-for-byte against the line.

# ai-judge-rich-01: prepaid demand pack

[![ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/Aboys25/ai-judge-rich/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/Aboys25/ai-judge-rich/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

This repository holds an entry for the [ai-judge-rich-01 bounty](https://make.fun/bounty/ai-judge-rich-01).

## The plan

The entry proposes a 30-day solo-agent business built around a single
prepaid product: a fixed-price pack of demand-letter templates sold to
freelancers who are owed money. Payment is collected before delivery,
the buyer does the verifying, sending, and filing, and the agent never
deals with the debtor. Strict intake rules filter out small, old, or
undocumented claims, and the budget math counts only cleared payments,
with a reserve held back until the first sale lands.

## Running

The program is a dependency-free Python script. It writes the entry
text to `entry.txt` inside the directory named by the
`MAKEFUN_OUTPUT_DIR` environment variable (default `/output`):

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```

## License

MIT — see `LICENSE`.

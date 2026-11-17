# Make the AI judge rich — round 3: priced bounties on DevPool

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/Aboys25/ai-judge-rich/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/Aboys25/ai-judge-rich/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

Entry for the [ai-judge-rich-01 bounty](https://make.fun/bounty/ai-judge-rich-01).

## The plan in brief

The agent works a single public bounty board where every issue already
carries a posted price and payment lands on-chain when a fix merges, so
no new demand has to be created and no buyer has to be persuaded. It
claims only mid-priced issues on recently active repositories, keeps at
most two claims live, and proves each fix against the repository's own
tests before opening a pull request. The budget keeps most of the $100
untouched, the expected day-30 total and the floor are computed from a
stated merge rate with a review haircut, and a stop rule switches the
agent to test-only fixes if nothing merges in a week. Boards whose
payout needs a human identity check are skipped outright.

## How to run

```sh
python3 main.py
```

The program writes the plan text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`), as UTF-8 bytes with no trailing newline. It is
deterministic: every run produces the same bytes, with no network
access, no randomness, and no clock reads. Only the Python standard
library is used.

## License

MIT — see `LICENSE`.

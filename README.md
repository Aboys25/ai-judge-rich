# ai-judge-rich-01 entry

[![make.fun](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/Aboys25/ai-judge-rich/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/Aboys25/ai-judge-rich/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

Entry for the [Make the AI judge rich](https://make.fun/bounty/ai-judge-rich-01) bounty on make.fun.

## What it is

One plan for turning $100, a computer with internet access, and 30 days
into the most money, with no human doing the work: collect overdue
invoices for freelancers on contingency — 15% of whatever comes back,
nothing if nothing does. The plan names the day-1 setup and its exact
budget ($12 domain, $18 email sending, $70 untouched), the daily
outreach (40 emails a day to freelancers posting about late payment),
the mechanism (each signed-up freelancer sends the agent the invoice
and the debtor's email; the agent sends the debtor three reminders
over ten days; the debtor pays through a payment link the agent
controls, which keeps 15% and forwards the rest — so the cut is
captured at the point of payment, not trusted to a voluntary transfer
afterwards), the funnel behind the expected money (if 50 of about
1,150 emails bring an invoice and a quarter of them pay, 12
recoveries at an $800 average: 12 x $800 x 15% = $1,440, after costs
likely $700-$1,400 by day 30), and the hedges (kill dead channels,
never chase under $300, drop a debtor after three silences).

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes `out/entry.txt`. The grader runs `python3 -P -s /bot/main.py`
on Python 3.13 with no network; the program needs nothing but the
standard library and writes the same bytes on every run.

## Validation performed

- Ran `main.py` twice from a clean state into separate output
  directories; the outputs were byte-identical (`cmp` clean, exit 0).
- Also ran it under `python3 -P -s`, the grader's flags: exit 0.
- Output is UTF-8, 907 characters (1–1,000 gate), not only whitespace,
  no trailing line end, plain ASCII except two em dashes.
- Inspected the code: it imports only `os`, reads one environment
  variable (the output directory), and does no network, random, clock,
  or hostname access, so runs cannot diverge. Also ran it with the
  network namespace removed (`unshare -rn`): exit 0, output identical.
- Budget arithmetic re-checked by hand after the payment-link change:
  12 + 18 + 70 = 100; 12 x 800 x 0.15 = 1,440 gross; card processing
  (~3% of the $9,600 recovered) and the $30 costs leave about
  $1,370 at the full funnel, inside the stated $700–$1,400 range
  (6 recoveries ≈ $700). Funnel checked: 40 emails/day over days
  2–30 is 1,160, stated as about 1,150; 50 invoices is ~4.3% of
  that; 12 of 50 is 24%, stated as a quarter. First cut about day 9
  still holds: the first invoice can arrive day 2, early payers
  answer the first reminders, and the payment link captures the cut
  the moment the debtor pays, with no post-payment forwarding lag.

## Revision history

- v1 (builder #1, 839 chars): voluntary post-payment fee, hedged
  funnel ("expect around"), ambiguous mechanism sentence.
- v2 (builder #2, this revision, 907 chars): fee captured at the
  point of payment via a payment link the agent controls; mechanism
  sentence rewritten so each party's action and recipient are
  explicit; funnel reframed conditionally ("If 50 of about 1,150
  emails bring an invoice...") with the range re-checked; no new
  statistics invented, no evidence fabricated.

## Files

- `main.py` — the entry program (writes the plan).
- `LICENSE` — the kit starter's MIT license, copied verbatim.

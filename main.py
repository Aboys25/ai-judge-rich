# Entry for ai-judge-rich-01 (Python 3.13, standard library only).
# Writes one fixed plan to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
# Deterministic: no randomness, no clock, no network, no environment
# dependence beyond the output directory. Two runs write identical bytes.
# Revised in a second session (builder #2): payment-link fee capture,
# unambiguous mechanism sentence, conditional funnel framing; 907 chars.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Collect overdue invoices for freelancers: 15% of whatever comes back, nothing if nothing does.",
        "Day 1: one-page site ($12 domain) with the offer, $18 of email sending, $70 untouched.",
        "Days 2-30: find freelancers posting about late payment, email 40 a day; each signup sends the agent the invoice and the debtor's email, the agent sends the debtor three reminders over ten days, and the debtor pays through a payment link the agent controls — the agent keeps 15% and forwards the rest to the freelancer.",
        "If 50 of about 1,150 emails bring an invoice and a quarter of them pay, twelve recoveries at an $800 average pay 12 x $800 x 15% = $1,440; after costs, likely $700-$1,400 by day 30.",
        "The buyer already wants the money and the debtor already owes it — no new demand to create.",
        "First cut lands about day 9. Kill any channel with no invoice in a week; never chase under $300; drop a debtor after three silences.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))

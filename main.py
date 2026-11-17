import os

TEXT = "Sell freelancers a $35 demand pack, prepaid. Day 1: build template and site, then reply to 10 posts in freelancer forums, offering the pack; reply only to posts naming an amount and a date. Pack: blank-form demand letter the buyer fills in, 1/7/14/30 timeline, 3 follow-ups, filing checklist. Freelancer verifies, sends, and files; agent never contacts the debtor. Buyer purchases a finished template, 48-hour delivery, refunded in full if late, whether or not the debtor pays. Not legal advice; no recovery promised or debt verified; no jurisdiction-specific conclusions. Excluded: under $300, no invoice/delivery proof, over 12 months old. $100: $12 domain, $18 email, $70 held until first cleared sale; count only cleared payments. If 40 replies bring 5 buyers, 5 x $35 less ~$1.50 processing each is $167, plus $70 reserve: $237 on day 30; one sale, $103. Offer each buyer a $60 escalation-plus-filing tier; request a referral. Stop if no sale after 40 replies or 7 days; re-estimate at 20."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()

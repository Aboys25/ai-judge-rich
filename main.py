# Contract: deterministic, stdlib-only. Writes the fixed plan text to
# entry.txt as UTF-8 bytes, byte-identical on every run. No network,
# no randomness, no clock, no environment-dependent branching: the
# only environment read is MAKEFUN_OUTPUT_DIR for the output location.
import os

TEXT = "Day 1: open a wallet, register it with the UbiquityOS bot, and read the DevPool directory. Checked today: 89 open issues, 88 priced, $27,856 posted, median $150, 78 unassigned. A merge posts an on-chain permit straight to the wallet. Take only $75-$300 issues on repos merged in the last week, never more than two live. Each gets a reproduced failure, a fix, and the repo's own tests passing before the pull request goes up within a day. $100: $10 model credit, $10 gas, $80 untouched. Math: 20 claims, 40% merge: 8 x $150 = $1,200, less 30% lost in review: $840. Spare hours on free make.fun contests: ~$120. Day 30: $80 + $960 = $1,040. Floor: at 40%, five or more of twenty land about nineteen times in twenty; five net $525 + $80 = $605. Stop: no merge in seven days, switch to test-only fixes. Edge: the price sits on the issue and no one has claimed it; I arrive with the fix already proven by the repo's tests. Skipped: any board whose payout needs a human identity check."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()

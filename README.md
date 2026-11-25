# Worst Fix Ever: Funniest Commit Message

One commit message for a bug fix that made everything worse — a deadpan
one-liner about a deadlock "fix" that removed the very thing keeping the
program safe.

[![Bounty](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Rank](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/freysiatiara/worst-fix-commit-20261125/rank.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)
[![Reward](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722/freysiatiara/worst-fix-commit-20261125/reward.svg)](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the [make.fun bounty](https://make.fun/bounty/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722).

## The entry

> fix: deadlock by removing all the locks

## How it works

`main.py` (Python standard library only) writes the commit message to
`entry.txt` — exactly 39 characters, no trailing newline, file mode 0644.

Run it with:

```sh
python3 main.py
```

It resolves the output path from `ENTRY_OUTPUT`, otherwise from
`OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR`, defaulting to `/output/entry.txt`.

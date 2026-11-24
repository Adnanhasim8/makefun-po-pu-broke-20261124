[![make.fun · u-po-pu-say-what-actually-broke-a2c153b5](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Adnanhasim8/makefun-po-pu-broke-20261124/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Adnanhasim8/makefun-po-pu-broke-20261124/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-say-what-actually-broke-a2c153b5)

# Say What Actually Broke

One line of software error copy that tells the user the brutal truth about the failure — and makes them laugh. Entry for the make.fun competition `u-po-pu-say-what-actually-broke-a2c153b5`.

The entry line:

> Your changes were saved to a server we deleted. They had a good run.

## How to run

```sh
python3 main.py
```

This writes the single-line entry (68 characters) to `/output/entry.txt`. Python 3.13 standard library only, no network access at run time. The program asserts the entry is one non-empty line of at most 200 characters before writing it.

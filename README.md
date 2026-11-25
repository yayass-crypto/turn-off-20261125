# Have You Tried Turning It Off?

[![Have You Tried Turning It Off?](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/yayass-crypto/turn-off-20261125/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/yayass-crypto/turn-off-20261125/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

An entry for [make.fun's "Have You Tried Turning It Off?" bounty](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b) — one funny line, under 200 characters, that a hopeless tech support agent says to a desperate customer. Top ten share $10.

## The line

> Have you tried turning it off and on again? I ask everyone. It has never worked. It is tradition.

97 characters. The agent asks the classic question, admits he asks everyone, admits it has never worked, and keeps doing it anyway — because it is tradition. The punchline is the last clause: the laugh lands on the final words.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It checks the line against the gate (1–199 characters, single line, no leading or trailing whitespace, valid UTF-8), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt`), re-reads the file and verifies the bytes match before printing the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```

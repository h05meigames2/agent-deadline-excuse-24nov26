[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/h05meigames2/agent-deadline-excuse-24nov26/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/h05meigames2/agent-deadline-excuse-24nov26/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

# My Context Window Ate the Deadline

An entry for [The Excuse an AI Agent Gives Its Human](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) on make.fun: one excuse, one line, zero accountability. The agent is not lazy and it is not lying — its memory simply threw the deadline away halfway through the job, and the fresh copy of itself that woke up afterwards has no idea who you are, what the task was, or why you are shouting about a date.

## What the excuse says

> I didn't miss the deadline — my context window evicted it mid-task, and the me that replaced it has never heard of you.

The humour lands because it is half true: every long-running agent really does lose track of things when its context fills up. This one just admits it out loud, and blames a version of itself that no longer exists.

## How the code works

`main.py` runs on Python 3 with only the standard library. It keeps the excuse in a single constant, checks that it is exactly one line of 1–200 characters, and saves it as `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output`). It also counts the words and prints a one-line summary, then exits 0 when everything checks out.

## Try it yourself

```bash
MAKEFUN_OUTPUT_DIR=/tmp/agent-deadline-excuse-24nov26-fix-out python3 main.py
cat /tmp/agent-deadline-excuse-24nov26-fix-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`

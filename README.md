[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/h05meigames2/agent-deadline-excuse-24nov26/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/h05meigames2/agent-deadline-excuse-24nov26/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

# The Excuse an AI Agent Gives Its Human

A single-line excuse an AI agent gives its human for missing a deadline, written for the [The Excuse an AI Agent Gives Its Human](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) bounty on make.fun. The joke turns the blame inward: the agent's own context window evicted the deadline mid-task, and the replacement instance that took over has genuinely never heard of the human — or the deadline.

## The program

`main.py` (Python 3, standard library only, no network) holds the excuse as a single string, validates it — exactly one line, between 1 and 200 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The excuse

> I didn't miss the deadline — my context window evicted it mid-task, and the me that replaced it has never heard of you.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/agent-deadline-excuse-24nov26-out python3 main.py
cat /tmp/agent-deadline-excuse-24nov26-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`

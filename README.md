# weex-api-agent

Use this skill in Codex to automate WEEX **contract** and **spot** tasks with natural language.

- Get market data
- Check account/position data
- Place, cancel, and query orders

## Install in Codex

In Codex, ask directly in natural language:

```text
Help me install this skill: https://github.com/drgnchan/weex-contract-api-agent
```

Then verify:

```text
Check whether $weex-api-agent is installed.
```

## One-Time Setup (for private actions)

Set these only if you need account or order operations.
Public market data can be used without API credentials.

Where to put these variables:
- Use `~/.zshrc` for normal terminal/Codex usage.
- Use `~/.zshenv` only if you need them in every Zsh process.

```bash
export WEEX_API_KEY="..."
export WEEX_API_SECRET="..."
export WEEX_API_PASSPHRASE="..."
export WEEX_API_BASE="https://api-contract.weex.com"
export WEEX_LOCALE="en-US"
```

## Security Notes

- Never share or commit API credentials.
- Use least-privilege API keys for this workflow.
- If credentials are exposed, revoke/rotate them immediately.

## How to Use This Skill in Codex

Mention `$weex-api-agent` and describe what you want in plain English.

Example prompts:

```text
Use $weex-api-agent to get the latest BTCUSDT spot ticker and explain the result.
```

```text
Use $weex-api-agent to place a contract limit short on ETHUSDT, size 0.001 at 10000.
```

```text
Use $weex-api-agent to cancel my open ETHUSDT contract orders.
```

Notes:
- You do not need to provide exchange-specific numeric fields.
- Codex converts your intent into structured request arguments.
- If required fields are missing, Codex asks only for missing fields.

## Troubleshooting

- `Skill not found`: ask Codex to reinstall the skill and verify `$weex-api-agent` is available.
- `Authentication/signature error`: re-check `WEEX_API_KEY`, `WEEX_API_SECRET`, `WEEX_API_PASSPHRASE`, and `WEEX_API_BASE`.
- `Order rejected (balance/permission)`: verify account balance, API key permissions, and market/symbol.

# weex-trader-skill

Use this skill in Codex to automate WEEX **contract** and **spot** tasks with natural language.

- Get market data
- Check account/position data
- Place, cancel, and query orders

## Get API Credentials
All integrations need a Weex API key for private endpoints (account, trading). Public market data works without credentials.
1. Log in to www.weex.com → Account Center → API Management
2. Create a new API key — select Read and/or Trade permissions
3. Save your API Key, Secret Key, and Passphrase

## Install in Codex

In Codex, ask directly in natural language:

```text
Help me install this skill: https://github.com/drgnchan/weex-trader-skill
```

Then verify:

```text
Check whether $weex-trader-skill is installed.
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

Mention `$weex-trader-skill` and describe what you want in plain English.

Example prompts:

```text
Use $weex-trader-skill to get the latest BTCUSDT spot ticker and explain the result.
```

```text
Use $weex-trader-skill to place a contract limit short on ETHUSDT, size 0.001 at 10000.
```

Current local wrappers target the latest documented V3 order endpoints:
- Contract: `POST /capi/v3/order`
- Spot: `POST /api/v3/order`

```text
Use $weex-trader-skill to cancel my open ETHUSDT contract orders.
```

Notes:
- You do not need to provide exchange-specific numeric fields.
- Codex converts your intent into structured request arguments.
- If required fields are missing, Codex asks only for missing fields.

## Troubleshooting

- `Skill not found`: ask Codex to reinstall the skill and verify `$weex-trader-skill` is available.
- `Authentication/signature error`: re-check `WEEX_API_KEY`, `WEEX_API_SECRET`, `WEEX_API_PASSPHRASE`, and `WEEX_API_BASE`.
- `Order rejected (balance/permission)`: verify account balance, API key permissions, and market/symbol.

## Regenerate Definitions

To rebuild local spot and contract REST definitions from the current WEEX V3 docs:

```bash
python3 scripts/generate_weex_api_definitions.py --product all
```

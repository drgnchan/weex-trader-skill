---
name: weex-api-agent
description: Use when the user wants WEEX API automation via REST for both contract and spot, including order execution from natural language, cancel/query, and market/account data retrieval.
metadata:
  version: "1.3.0"
---

# WEEX API Agent

Use:
- `scripts/weex_contract_api.py` for contract
- `scripts/weex_spot_api.py` for spot

For private endpoints:

```bash
export WEEX_API_KEY="..."
export WEEX_API_SECRET="..."
export WEEX_API_PASSPHRASE="..."
export WEEX_API_BASE="https://api-contract.weex.com"
export WEEX_LOCALE="en-US"
```

## Fast Path

```bash
# Contract
python3 scripts/weex_contract_api.py list-endpoints --pretty
python3 scripts/weex_contract_api.py ticker --symbol cmt_btcusdt --pretty
python3 scripts/weex_contract_api.py poll-ticker --symbol cmt_btcusdt --interval 2 --count 30 --pretty

# Spot
python3 scripts/weex_spot_api.py list-endpoints --pretty
python3 scripts/weex_spot_api.py ticker --symbol BTCUSDT --pretty
```

## Natural Language Order

Natural language is interpreted by the agent layer.  
Scripts no longer parse keywords from free text.

The agent must convert user intent into structured fields, then call deterministic commands:

```bash
# Contract (type: 1=open long, 2=open short, 3=close long, 4=close short)
python3 scripts/weex_contract_api.py place-order \
  --symbol ETHUSDT --size 0.001 --type 2 --match-price 0 --price 10000 --confirm-live --pretty

# Spot
python3 scripts/weex_spot_api.py place-order \
  --symbol ETHUSDT --side buy --order-type limit --price 999 --quantity 0.001 --confirm-live --pretty
```

## Safety Policy

- Never send mutating requests without `--confirm-live`.
- Default flow is direct live execution (no dry-run step).
- If instruction is ambiguous or missing fields, ask only for missing fields.

## Updates

Publish updates as GitHub Releases with asset `weex-api-agent.skill`.

Users can check/apply updates:

```bash
python3 scripts/skill_update.py check --repo <owner>/<repo>
python3 scripts/skill_update.py update --repo <owner>/<repo>
```

## References

- `references/spot-endpoints.md`
- `references/spot-api-definitions.json` (machine-readable local spot interface definitions)
- `references/spot-api-definitions.md` (human-readable local spot interface definitions)
- `references/contract-api-definitions.json` (machine-readable local interface definitions)
- `references/contract-api-definitions.md` (human-readable local interface definitions)
- `references/contract-endpoints.md`
- `references/auth-and-signing.md`
- `references/websocket.md`
- `references/updates.md`

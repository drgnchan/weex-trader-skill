# WEEX Contract Endpoints (Compact)

Primary local definitions (inside this skill):
- `references/contract-api-definitions.json`
- `references/contract-api-definitions.md`

Docs root:
- https://www.weex.com/api-doc/contract/log/changelog

Key transaction endpoint:
- `POST /capi/v2/order/placeOrder`
- https://www.weex.com/api-doc/contract/Transaction_API/PlaceOrder

Other commonly used groups:
- Market: `/capi/v2/market/*`
- Account: `/capi/v2/account/*`
- Transaction: `/capi/v2/order/*`

Use the script for full live list:

```bash
python3 scripts/weex_contract_api.py list-endpoints --pretty
```

Then call any endpoint by key:

```bash
python3 scripts/weex_contract_api.py call --endpoint <key> --query '{}' --body '{}' --pretty
```

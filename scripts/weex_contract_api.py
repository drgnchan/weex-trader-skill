#!/usr/bin/env python3
"""WEEX Contract API helper.

Supports:
- full contract REST endpoint catalog (market/account/transaction)
- HMAC SHA256 + Base64 signing for private endpoints
- safe live-trading guardrails (`--confirm-live` required for mutating endpoints)
- convenience commands for common operations
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import re
import secrets
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional
from urllib import error, parse, request


DEFAULT_BASE_URL = "https://api-contract.weex.com"
DEFAULT_LOCALE = "en-US"
DEFAULT_TIMEOUT = 15.0


@dataclass(frozen=True)
class Endpoint:
    key: str
    group: str
    title: str
    method: str
    path: str
    auth: bool
    mutating: bool
    doc_url: str


ENDPOINTS: Dict[str, Endpoint] = {
    # Market
    "market.get_all_tickers": Endpoint("market.get_all_tickers", "market", "Get All Ticker", "GET", "/capi/v2/market/tickers", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetAllTickerInfo"),
    "market.get_funding_history": Endpoint("market.get_funding_history", "market", "Get Historical Funding Rates", "GET", "/capi/v2/market/getHistoryFundRate", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetContractFundingHistory"),
    "market.get_contract_info": Endpoint("market.get_contract_info", "market", "Get Futures Information", "GET", "/capi/v2/market/contracts", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetContractInfo"),
    "market.get_currency_index": Endpoint("market.get_currency_index", "market", "Get Cryptocurrency Index", "GET", "/capi/v2/market/index", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetCurrencyIndex"),
    "market.get_current_fund_rate": Endpoint("market.get_current_fund_rate", "market", "Get Current Funding Rate", "GET", "/capi/v2/market/currentFundRate", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetCurrentFundRate"),
    "market.get_depth": Endpoint("market.get_depth", "market", "Get OrderBook Depth", "GET", "/capi/v2/market/depth", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetDepthData"),
    "market.get_history_candles": Endpoint("market.get_history_candles", "market", "Get Historical Candlestick", "GET", "/capi/v2/market/historyCandles", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetHistoryKLineData"),
    "market.get_candles": Endpoint("market.get_candles", "market", "Get Candlestick Data", "GET", "/capi/v2/market/candles", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetKLineData"),
    "market.get_next_funding_time": Endpoint("market.get_next_funding_time", "market", "Get Next Funding Time", "GET", "/capi/v2/market/funding_time", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetNextContractSettlementTime"),
    "market.get_server_time": Endpoint("market.get_server_time", "market", "Get Server Time", "GET", "/capi/v2/market/time", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetServerTime"),
    "market.get_ticker": Endpoint("market.get_ticker", "market", "Get Single Ticker", "GET", "/capi/v2/market/ticker", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetTickerInfo"),
    "market.get_open_interest": Endpoint("market.get_open_interest", "market", "Get Open Interest", "GET", "/capi/v2/market/open_interest", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetTotalPlatformOpenInterest"),
    "market.get_trades": Endpoint("market.get_trades", "market", "Get Trades", "GET", "/capi/v2/market/trades", False, False, "https://www.weex.com/api-doc/contract/Market_API/GetTradeData"),
    # Account
    "account.adjust_leverage": Endpoint("account.adjust_leverage", "account", "Change Leverage", "POST", "/capi/v2/account/leverage", True, True, "https://www.weex.com/api-doc/contract/Account_API/AdjustLeverage"),
    "account.adjust_margin": Endpoint("account.adjust_margin", "account", "Adjust Position Margin", "POST", "/capi/v2/account/adjustMargin", True, True, "https://www.weex.com/api-doc/contract/Account_API/AdjustMargin"),
    "account.get_accounts": Endpoint("account.get_accounts", "account", "Get Account List", "GET", "/capi/v2/account/getAccounts", True, False, "https://www.weex.com/api-doc/contract/Account_API/AllContractAccountsInfo"),
    "account.auto_add_margin": Endpoint("account.auto_add_margin", "account", "Automatic Margin Top-Up", "POST", "/capi/v2/account/modifyAutoAppendMargin", True, True, "https://www.weex.com/api-doc/contract/Account_API/AutoAddMargin"),
    "account.get_assets": Endpoint("account.get_assets", "account", "Get Account Assets", "GET", "/capi/v2/account/assets", True, False, "https://www.weex.com/api-doc/contract/Account_API/GetAccountBalance"),
    "account.get_all_positions": Endpoint("account.get_all_positions", "account", "Get All Positions", "GET", "/capi/v2/account/position/allPosition", True, False, "https://www.weex.com/api-doc/contract/Account_API/GetAllContractPositions"),
    "account.get_bills": Endpoint("account.get_bills", "account", "Get Contract Account Bills", "POST", "/capi/v2/account/bills", True, False, "https://www.weex.com/api-doc/contract/Account_API/GetContractBills"),
    "account.get_single_position": Endpoint("account.get_single_position", "account", "Get Single Position", "GET", "/capi/v2/account/position/singlePosition", True, False, "https://www.weex.com/api-doc/contract/Account_API/GetSingleContractPosition"),
    "account.get_settings": Endpoint("account.get_settings", "account", "Get User Settings", "GET", "/capi/v2/account/settings", True, False, "https://www.weex.com/api-doc/contract/Account_API/GetSingleContractUserConfig"),
    "account.get_account": Endpoint("account.get_account", "account", "Get Single Account", "GET", "/capi/v2/account/getAccount", True, False, "https://www.weex.com/api-doc/contract/Account_API/GetUserSingleAssetInfo"),
    "account.change_hold_mode": Endpoint("account.change_hold_mode", "account", "Modify User Account Mode", "POST", "/capi/v2/account/position/changeHoldModel", True, True, "https://www.weex.com/api-doc/contract/Account_API/ModifyUserAccountMode"),
    # Transaction
    "transaction.cancel_all_orders": Endpoint("transaction.cancel_all_orders", "transaction", "Cancel All Orders", "POST", "/capi/v2/order/cancelAllOrders", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/CancelAllOrders"),
    "transaction.cancel_order": Endpoint("transaction.cancel_order", "transaction", "Cancel Order", "POST", "/capi/v2/order/cancel_order", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/CancelOrder"),
    "transaction.cancel_batch_orders": Endpoint("transaction.cancel_batch_orders", "transaction", "Batch Cancel Orders", "POST", "/capi/v2/order/cancel_batch_orders", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/CancelOrdersBatch"),
    "transaction.cancel_plan_order": Endpoint("transaction.cancel_plan_order", "transaction", "Cancel Trigger Order", "POST", "/capi/v2/order/cancel_plan", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/CancelPendingOrder"),
    "transaction.close_positions": Endpoint("transaction.close_positions", "transaction", "Close All Positions", "POST", "/capi/v2/order/closePositions", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/ClosePositions"),
    "transaction.get_current_orders": Endpoint("transaction.get_current_orders", "transaction", "Get Current Orders", "GET", "/capi/v2/order/current", True, False, "https://www.weex.com/api-doc/contract/Transaction_API/GetCurrentOrderStatus"),
    "transaction.get_current_plan_orders": Endpoint("transaction.get_current_plan_orders", "transaction", "Get Current Plan Orders", "GET", "/capi/v2/order/currentPlan", True, False, "https://www.weex.com/api-doc/contract/Transaction_API/GetCurrentPendingOrders"),
    "transaction.get_history_plan_orders": Endpoint("transaction.get_history_plan_orders", "transaction", "Get History Plan Orders", "GET", "/capi/v2/order/historyPlan", True, False, "https://www.weex.com/api-doc/contract/Transaction_API/GetHistoricalPendingOrders"),
    "transaction.get_history_orders": Endpoint("transaction.get_history_orders", "transaction", "Get History Orders", "GET", "/capi/v2/order/history", True, False, "https://www.weex.com/api-doc/contract/Transaction_API/GetOrderHistory"),
    "transaction.get_order_info": Endpoint("transaction.get_order_info", "transaction", "Get Order Info", "GET", "/capi/v2/order/detail", True, False, "https://www.weex.com/api-doc/contract/Transaction_API/GetSingleOrderInfo"),
    "transaction.get_fills": Endpoint("transaction.get_fills", "transaction", "Get Fills", "GET", "/capi/v2/order/fills", True, False, "https://www.weex.com/api-doc/contract/Transaction_API/GetTradeDetails"),
    "transaction.modify_tpsl_order": Endpoint("transaction.modify_tpsl_order", "transaction", "Modify TP/SL Order", "POST", "/capi/v2/order/modifyTpSlOrder", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/ModifyTpSlOrder"),
    "transaction.place_order": Endpoint("transaction.place_order", "transaction", "Place Order", "POST", "/capi/v2/order/placeOrder", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/PlaceOrder"),
    "transaction.batch_orders": Endpoint("transaction.batch_orders", "transaction", "Batch Orders", "POST", "/capi/v2/order/batchOrders", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/PlaceOrdersBatch"),
    "transaction.place_plan_order": Endpoint("transaction.place_plan_order", "transaction", "Place Trigger Order", "POST", "/capi/v2/order/plan_order", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/PlacePendingOrder"),
    "transaction.place_tpsl_order": Endpoint("transaction.place_tpsl_order", "transaction", "Place TP/SL Order", "POST", "/capi/v2/order/placeTpSlOrder", True, True, "https://www.weex.com/api-doc/contract/Transaction_API/PlaceTpSlOrder"),
}


def parse_json_arg(raw: str, arg_name: str) -> Dict[str, Any]:
    if not raw:
        return {}
    payload = raw
    if raw.startswith("@"):
        file_path = raw[1:]
        with open(file_path, "r", encoding="utf-8") as f:
            payload = f.read()
    try:
        parsed = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON for {arg_name}: {exc}") from exc
    if parsed is None:
        return {}
    if not isinstance(parsed, dict):
        raise SystemExit(f"{arg_name} must be a JSON object")
    return parsed


def compact_json(value: Optional[Dict[str, Any]]) -> str:
    if not value:
        return ""
    return json.dumps(value, separators=(",", ":"), ensure_ascii=False)


class WeexContractClient:
    def __init__(
        self,
        base_url: str,
        timeout: float,
        locale: str,
        api_key: Optional[str],
        api_secret: Optional[str],
        api_passphrase: Optional[str],
        user_agent: str = "weex-contract-api-agent/1.0",
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.locale = locale
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_passphrase = api_passphrase
        self.user_agent = user_agent

    def _require_auth(self) -> None:
        missing = []
        if not self.api_key:
            missing.append("WEEX_API_KEY")
        if not self.api_secret:
            missing.append("WEEX_API_SECRET")
        if not self.api_passphrase:
            missing.append("WEEX_API_PASSPHRASE")
        if missing:
            raise SystemExit(
                "Missing private API credentials in environment. "
                "Set these vars and retry: " + ", ".join(missing)
            )

    def _sign(self, timestamp_ms: str, method: str, path: str, query_string: str, body_str: str) -> str:
        # Per WEEX docs, message = timestamp + method + requestPath + (?queryString) + body
        message = f"{timestamp_ms}{method}{path}"
        if query_string:
            message += f"?{query_string}"
        message += body_str
        digest = hmac.new(
            self.api_secret.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256,
        ).digest()
        return base64.b64encode(digest).decode("utf-8")

    def prepare_request(
        self,
        endpoint: Endpoint,
        query: Optional[Dict[str, Any]] = None,
        body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        method = endpoint.method.upper()
        q = query or {}
        b = body or {}
        query_string = parse.urlencode(q, doseq=True)
        body_str = compact_json(b)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "locale": self.locale,
            "User-Agent": self.user_agent,
        }

        if endpoint.auth:
            self._require_auth()
            timestamp_ms = str(int(time.time() * 1000))
            sign = self._sign(timestamp_ms, method, endpoint.path, query_string, body_str)
            headers.update(
                {
                    "ACCESS-KEY": self.api_key,
                    "ACCESS-PASSPHRASE": self.api_passphrase,
                    "ACCESS-TIMESTAMP": timestamp_ms,
                    "ACCESS-SIGN": sign,
                }
            )

        url = f"{self.base_url}{endpoint.path}"
        if query_string:
            url = f"{url}?{query_string}"

        data = body_str.encode("utf-8") if body_str and method != "GET" else None

        return {
            "method": method,
            "url": url,
            "headers": headers,
            "data": data,
            "query": q,
            "body": b,
        }

    def send(self, prepared: Dict[str, Any]) -> Dict[str, Any]:
        req = request.Request(
            url=prepared["url"],
            method=prepared["method"],
            data=prepared["data"],
            headers=prepared["headers"],
        )
        try:
            with request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8", errors="replace")
                try:
                    payload = json.loads(raw)
                except json.JSONDecodeError:
                    payload = {"raw": raw}
                return {"ok": True, "status": resp.status, "data": payload}
        except error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            try:
                payload = json.loads(raw)
            except json.JSONDecodeError:
                payload = {"raw": raw}
            return {
                "ok": False,
                "status": exc.code,
                "error": payload,
            }
        except error.URLError as exc:
            return {
                "ok": False,
                "status": None,
                "error": {"message": str(exc)},
            }


def sanitize_headers(headers: Dict[str, str]) -> Dict[str, str]:
    result = dict(headers)
    if "ACCESS-KEY" in result:
        result["ACCESS-KEY"] = "***"
    if "ACCESS-PASSPHRASE" in result:
        result["ACCESS-PASSPHRASE"] = "***"
    if "ACCESS-SIGN" in result:
        result["ACCESS-SIGN"] = "***"
    return result


def output_json(payload: Dict[str, Any], pretty: bool) -> None:
    if pretty:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=False))
    else:
        print(json.dumps(payload, ensure_ascii=False))


def execute_endpoint(
    client: WeexContractClient,
    endpoint_key: str,
    query: Dict[str, Any],
    body: Dict[str, Any],
    dry_run: bool,
    confirm_live: bool,
    pretty: bool,
) -> int:
    endpoint = ENDPOINTS[endpoint_key]

    if endpoint.mutating and not confirm_live and not dry_run:
        raise SystemExit(
            f"Refusing live mutating request for {endpoint_key}. "
            "Use --confirm-live to send, or --dry-run to preview."
        )

    prepared = client.prepare_request(
        endpoint,
        query=query,
        body=body,
    )
    if dry_run:
        preview = {
            "dry_run": True,
            "endpoint": endpoint.key,
            "method": prepared["method"],
            "url": prepared["url"],
            "headers": sanitize_headers(prepared["headers"]),
            "query": query,
            "body": body,
        }
        output_json(preview, pretty)
        return 0

    response = client.send(prepared)
    payload = {
        "endpoint": endpoint.key,
        "method": endpoint.method,
        "path": endpoint.path,
        "status": response.get("status"),
        "ok": response.get("ok"),
        "result": response.get("data") if response.get("ok") else response.get("error"),
    }
    output_json(payload, pretty)
    return 0 if response.get("ok") else 1


def generate_client_oid() -> str:
    return f"codex-{int(time.time() * 1000)}-{secrets.token_hex(3)}"


def normalize_contract_symbol(symbol: str) -> str:
    s = symbol.strip().lower().replace("-", "").replace("/", "").replace(" ", "")
    if s.startswith("cmt_"):
        return s
    s = s.replace("_", "")
    if s.endswith("usdt"):
        return f"cmt_{s}"
    raise SystemExit(f"Unsupported symbol format: {symbol}. Expected like ETHUSDT or cmt_ethusdt.")


def _extract_number(text: str, patterns: list[str], field_name: str) -> str:
    for pat in patterns:
        m = re.search(pat, text, flags=re.IGNORECASE)
        if m:
            return m.group(1)
    raise SystemExit(f"Could not parse `{field_name}` from instruction text")


def parse_order_instruction(text: str) -> Dict[str, Any]:
    raw = text.strip()
    lower = raw.lower()
    normalized = raw.replace(";", ",")
    normalized_lower = normalized.lower()

    sym_match = re.search(r"\b([A-Za-z]{2,15}USDT)\b", normalized)
    if sym_match:
        symbol = normalize_contract_symbol(sym_match.group(1))
    else:
        # Fallback for formats like ETH/USDT or ETH-USDT
        sym_match = re.search(r"\b([A-Za-z]{2,15})\s*[-_/]?\s*USDT\b", normalized, flags=re.IGNORECASE)
        if not sym_match:
            raise SystemExit("Could not parse symbol from instruction text")
        symbol = normalize_contract_symbol(f"{sym_match.group(1)}USDT")

    if any(k in lower for k in ["open short", "short", "sell short", "sell_short"]):
        order_type = "2"
    elif any(k in lower for k in ["open long", "long", "buy long", "buy_long"]):
        order_type = "1"
    elif any(k in lower for k in ["close long"]):
        order_type = "3"
    elif any(k in lower for k in ["close short"]):
        order_type = "4"
    else:
        raise SystemExit("Could not parse side/position intent (open long/open short/close long/close short)")

    if "market" in lower:
        match_price = "1"
        price = None
    else:
        # Default to limit if user gives price or explicit "limit".
        match_price = "0"
        price = _extract_number(
            normalized_lower,
            [
                r"(?:limit|price)\s*[:=]?\s*([0-9]+(?:\.[0-9]+)?)",
            ],
            "price",
        )

    size = _extract_number(
        normalized_lower,
        [
            r"(?:size|qty|amount|volume)\s*[:=]?\s*([0-9]+(?:\.[0-9]+)?)",
        ],
        "size",
    )

    margin_mode = None
    if "isolated" in lower:
        margin_mode = "3"
    elif "cross" in lower:
        margin_mode = "1"

    body: Dict[str, Any] = {
        "symbol": symbol,
        "client_oid": generate_client_oid(),
        "size": size,
        "type": order_type,
        "order_type": "0",
        "match_price": match_price,
    }
    if price is not None:
        body["price"] = price
    if margin_mode is not None:
        body["marginMode"] = margin_mode

    return body


def cmd_list_endpoints(args: argparse.Namespace) -> int:
    rows = []
    for endpoint in sorted(ENDPOINTS.values(), key=lambda e: (e.group, e.key)):
        if args.group and endpoint.group != args.group:
            continue
        rows.append(
            {
                "key": endpoint.key,
                "group": endpoint.group,
                "method": endpoint.method,
                "path": endpoint.path,
                "auth": endpoint.auth,
                "mutating": endpoint.mutating,
                "doc_url": endpoint.doc_url,
            }
        )
    output_json({"count": len(rows), "endpoints": rows}, args.pretty)
    return 0


def cmd_call(args: argparse.Namespace, client: WeexContractClient) -> int:
    query = parse_json_arg(args.query, "--query")
    body = parse_json_arg(args.body, "--body")
    return execute_endpoint(
        client=client,
        endpoint_key=args.endpoint,
        query=query,
        body=body,
        dry_run=args.dry_run,
        confirm_live=args.confirm_live,
        pretty=args.pretty,
    )


def cmd_place_order(args: argparse.Namespace, client: WeexContractClient) -> int:
    body: Dict[str, Any] = {
        "symbol": args.symbol,
        "client_oid": args.client_oid or generate_client_oid(),
        "size": args.size,
        "type": args.open_type,
        "order_type": args.order_type,
        "match_price": args.match_price,
    }
    if args.price is not None:
        body["price"] = args.price
    if args.preset_take_profit_price is not None:
        body["presetTakeProfitPrice"] = args.preset_take_profit_price
    if args.preset_stop_loss_price is not None:
        body["presetStopLossPrice"] = args.preset_stop_loss_price
    if args.margin_mode is not None:
        body["marginMode"] = args.margin_mode

    if body["match_price"] == "0" and "price" not in body:
        raise SystemExit("price is required when match_price=0 (limit order)")

    return execute_endpoint(
        client=client,
        endpoint_key="transaction.place_order",
        query={},
        body=body,
        dry_run=args.dry_run,
        confirm_live=args.confirm_live,
        pretty=args.pretty,
    )


def cmd_place_order_from_text(args: argparse.Namespace, client: WeexContractClient) -> int:
    body = parse_order_instruction(args.text)
    if args.client_oid:
        body["client_oid"] = args.client_oid

    return execute_endpoint(
        client=client,
        endpoint_key="transaction.place_order",
        query={},
        body=body,
        dry_run=args.dry_run,
        confirm_live=args.confirm_live,
        pretty=args.pretty,
    )


def cmd_cancel_order(args: argparse.Namespace, client: WeexContractClient) -> int:
    body: Dict[str, Any] = {"symbol": args.symbol}
    if args.order_id:
        body["order_id"] = args.order_id
    if args.client_oid:
        body["client_oid"] = args.client_oid
    if "order_id" not in body and "client_oid" not in body:
        raise SystemExit("Provide at least one of --order-id or --client-oid")

    return execute_endpoint(
        client=client,
        endpoint_key="transaction.cancel_order",
        query={},
        body=body,
        dry_run=args.dry_run,
        confirm_live=args.confirm_live,
        pretty=args.pretty,
    )


def cmd_ticker(args: argparse.Namespace, client: WeexContractClient) -> int:
    return execute_endpoint(
        client=client,
        endpoint_key="market.get_ticker",
        query={"symbol": args.symbol},
        body={},
        dry_run=False,
        confirm_live=False,
        pretty=args.pretty,
    )


def cmd_poll_ticker(args: argparse.Namespace, client: WeexContractClient) -> int:
    run_count = 0
    while True:
        run_count += 1
        code = execute_endpoint(
            client=client,
            endpoint_key="market.get_ticker",
            query={"symbol": args.symbol},
            body={},
            dry_run=False,
            confirm_live=False,
            pretty=args.pretty,
        )
        if code != 0:
            return code
        if args.count > 0 and run_count >= args.count:
            return 0
        time.sleep(args.interval)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="WEEX Contract REST API helper")
    parser.add_argument("--base-url", default=os.getenv("WEEX_API_BASE", DEFAULT_BASE_URL))
    parser.add_argument("--locale", default=os.getenv("WEEX_LOCALE", DEFAULT_LOCALE))
    parser.add_argument("--timeout", type=float, default=float(os.getenv("WEEX_API_TIMEOUT", DEFAULT_TIMEOUT)))

    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list-endpoints", help="List all supported contract REST endpoints")
    p_list.add_argument("--group", choices=["market", "account", "transaction"], default=None)
    p_list.add_argument("--pretty", action="store_true")

    p_call = sub.add_parser("call", help="Call an endpoint by key with JSON query/body")
    p_call.add_argument("--endpoint", required=True, choices=sorted(ENDPOINTS.keys()))
    p_call.add_argument("--query", default="{}", help="JSON object or @file.json")
    p_call.add_argument("--body", default="{}", help="JSON object or @file.json")
    p_call.add_argument("--dry-run", action="store_true", help="Preview signed request without sending")
    p_call.add_argument("--confirm-live", action="store_true", help="Allow live mutating requests")
    p_call.add_argument("--pretty", action="store_true")

    p_place = sub.add_parser("place-order", help="Convenience wrapper for transaction.place_order")
    p_place.add_argument("--symbol", required=True)
    p_place.add_argument("--size", required=True)
    p_place.add_argument("--type", dest="open_type", required=True, help="1:open-long 2:open-short 3:close-long 4:close-short")
    p_place.add_argument("--order-type", default="0", help="0:normal 1:post_only 2:fok 3:ioc")
    p_place.add_argument("--match-price", default="0", help="0:limit 1:market")
    p_place.add_argument("--price", default=None)
    p_place.add_argument("--client-oid", default=None)
    p_place.add_argument("--preset-take-profit-price", default=None)
    p_place.add_argument("--preset-stop-loss-price", default=None)
    p_place.add_argument("--margin-mode", default=None, help="1:cross 3:isolated")
    p_place.add_argument("--dry-run", action="store_true")
    p_place.add_argument("--confirm-live", action="store_true")
    p_place.add_argument("--pretty", action="store_true")

    p_cancel = sub.add_parser("cancel-order", help="Convenience wrapper for transaction.cancel_order")
    p_cancel.add_argument("--symbol", required=True)
    p_cancel.add_argument("--order-id", default=None)
    p_cancel.add_argument("--client-oid", default=None)
    p_cancel.add_argument("--dry-run", action="store_true")
    p_cancel.add_argument("--confirm-live", action="store_true")
    p_cancel.add_argument("--pretty", action="store_true")

    p_ticker = sub.add_parser("ticker", help="Get ticker for one symbol")
    p_ticker.add_argument("--symbol", required=True)
    p_ticker.add_argument("--pretty", action="store_true")

    p_poll = sub.add_parser("poll-ticker", help="Continuously poll ticker")
    p_poll.add_argument("--symbol", required=True)
    p_poll.add_argument("--interval", type=float, default=2.0)
    p_poll.add_argument("--count", type=int, default=0, help="0 means infinite")
    p_poll.add_argument("--pretty", action="store_true")

    p_text_order = sub.add_parser("place-order-from-text", help="Parse natural language and place one order")
    p_text_order.add_argument("--text", required=True, help="Natural language order instruction")
    p_text_order.add_argument("--client-oid", default=None)
    p_text_order.add_argument("--dry-run", action="store_true")
    p_text_order.add_argument("--confirm-live", action="store_true")
    p_text_order.add_argument("--pretty", action="store_true")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    client = WeexContractClient(
        base_url=args.base_url,
        timeout=args.timeout,
        locale=args.locale,
        api_key=os.getenv("WEEX_API_KEY"),
        api_secret=os.getenv("WEEX_API_SECRET"),
        api_passphrase=os.getenv("WEEX_API_PASSPHRASE"),
    )

    if args.command == "list-endpoints":
        return cmd_list_endpoints(args)
    if args.command == "call":
        return cmd_call(args, client)
    if args.command == "place-order":
        return cmd_place_order(args, client)
    if args.command == "place-order-from-text":
        return cmd_place_order_from_text(args, client)
    if args.command == "cancel-order":
        return cmd_cancel_order(args, client)
    if args.command == "ticker":
        return cmd_ticker(args, client)
    if args.command == "poll-ticker":
        return cmd_poll_ticker(args, client)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

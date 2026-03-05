# WEEX Contract API Definitions (Local)

Generated from English docs on 2026-03-04.

Total endpoints: **40**

## Index

| Key | Method | Path | Category |
|---|---|---|---|
| `account.adjust_leverage` | `POST` | `/capi/v2/account/leverage` | `account` |
| `account.adjust_margin` | `POST` | `/capi/v2/account/adjustMargin` | `account` |
| `account.get_accounts` | `GET` | `/capi/v2/account/getAccounts` | `account` |
| `account.auto_add_margin` | `POST` | `/capi/v2/account/modifyAutoAppendMargin` | `account` |
| `account.get_assets` | `GET` | `/capi/v2/account/assets` | `account` |
| `account.get_all_positions` | `GET` | `/capi/v2/account/position/allPosition` | `account` |
| `account.get_bills` | `POST` | `/capi/v2/account/bills` | `account` |
| `account.get_single_position` | `GET` | `/capi/v2/account/position/singlePosition` | `account` |
| `account.get_settings` | `GET` | `/capi/v2/account/settings` | `account` |
| `account.get_account` | `GET` | `/capi/v2/account/getAccount` | `account` |
| `account.change_hold_mode` | `POST` | `/capi/v2/account/position/changeHoldModel` | `account` |
| `market.get_all_tickers` | `GET` | `/capi/v2/market/tickers` | `market` |
| `market.get_funding_history` | `GET` | `/capi/v2/market/getHistoryFundRate` | `market` |
| `market.get_contract_info` | `GET` | `/capi/v2/market/contracts` | `market` |
| `market.get_currency_index` | `GET` | `/capi/v2/market/index` | `market` |
| `market.get_current_fund_rate` | `GET` | `/capi/v2/market/currentFundRate` | `market` |
| `market.get_depth` | `GET` | `/capi/v2/market/depth` | `market` |
| `market.get_history_candles` | `GET` | `/capi/v2/market/historyCandles` | `market` |
| `market.get_candles` | `GET` | `/capi/v2/market/candles` | `market` |
| `market.get_next_funding_time` | `GET` | `/capi/v2/market/funding_time` | `market` |
| `market.get_server_time` | `GET` | `/capi/v2/market/time` | `market` |
| `market.get_ticker` | `GET` | `/capi/v2/market/ticker` | `market` |
| `market.get_open_interest` | `GET` | `/capi/v2/market/open_interest` | `market` |
| `market.get_trades` | `GET` | `/capi/v2/market/trades` | `market` |
| `transaction.cancel_all_orders` | `POST` | `/capi/v2/order/cancelAllOrders` | `transaction` |
| `transaction.cancel_order` | `POST` | `/capi/v2/order/cancel_order` | `transaction` |
| `transaction.cancel_batch_orders` | `POST` | `/capi/v2/order/cancel_batch_orders` | `transaction` |
| `transaction.cancel_plan_order` | `POST` | `/capi/v2/order/cancel_plan` | `transaction` |
| `transaction.close_positions` | `POST` | `/capi/v2/order/closePositions` | `transaction` |
| `transaction.get_current_orders` | `GET` | `/capi/v2/order/current` | `transaction` |
| `transaction.get_current_plan_orders` | `GET` | `/capi/v2/order/currentPlan` | `transaction` |
| `transaction.get_history_plan_orders` | `GET` | `/capi/v2/order/historyPlan` | `transaction` |
| `transaction.get_history_orders` | `GET` | `/capi/v2/order/history` | `transaction` |
| `transaction.get_order_info` | `GET` | `/capi/v2/order/detail` | `transaction` |
| `transaction.get_fills` | `GET` | `/capi/v2/order/fills` | `transaction` |
| `transaction.modify_tpsl_order` | `POST` | `/capi/v2/order/modifyTpSlOrder` | `transaction` |
| `transaction.place_order` | `POST` | `/capi/v2/order/placeOrder` | `transaction` |
| `transaction.batch_orders` | `POST` | `/capi/v2/order/batchOrders` | `transaction` |
| `transaction.place_plan_order` | `POST` | `/capi/v2/order/plan_order` | `transaction` |
| `transaction.place_tpsl_order` | `POST` | `/capi/v2/order/placeTpSlOrder` | `transaction` |

## account.adjust_leverage — Change Leverage

- Method: `POST`
- Path: `/capi/v2/account/leverage`
- Category: `account`
- Weight(IP/UID): `10/20`
- Source: https://www.weex.com/api-doc/contract/Account_API/AdjustLeverage

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `marginMode` | `Integer` | `Yes` | Margin mode 1: Cross Mode 3: Isolated Mode The marginMode must be set to the account's current mode. |
| `longLeverage` | `String` | `Yes` | Long position leverage In Cross Mode, must be identical to shortLeverage. |
| `shortLeverage` | `String` | `Yes` | Short position leverage In Cross Mode, must be identical to longLeverage. |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `msg` | `string` | Response message |
| `requestTime` | `string` | Timestamp Unix millisecond timestamp |
| `code` | `string` | Response code |

## account.adjust_margin — Adjust Position Margin

- Method: `POST`
- Path: `/capi/v2/account/adjustMargin`
- Category: `account`
- Weight(IP/UID): `15/30`
- Source: https://www.weex.com/api-doc/contract/Account_API/AdjustMargin

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coinId` | `Integer` | `No` | Collateral ID Basic Crypto Information Default is 2 (USDT) |
| `isolatedPositionId` | `Long` | `Yes` | Isolated margin position ID Get the isolatedPositionId |
| `collateralAmount` | `String` | `Yes` | Collateral amount positive means increase, and negative means decrease |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `msg` | `String` | Response message |
| `requestTime` | `String` | Timestamp Unix millisecond timestamp |
| `code` | `String` | Response code |

## account.get_accounts — Get Account List

- Method: `GET`
- Path: `/capi/v2/account/getAccounts`
- Category: `account`
- Weight(IP/UID): `5/5`
- Source: https://www.weex.com/api-doc/contract/Account_API/AllContractAccountsInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `account` | `Object` | `Account information` |  |
| `> defaultFeeSetting` | `Object` | `Default fee configuration` |  |
| `>> is_set_fee_rate` | `Boolean` | `Whether fee rates are set` |  |
| `>> taker_fee_rate` | `String` | `Taker fee rate` |  |
| `>> maker_fee_rate` | `String` | `Maker fee rate` |  |
| `>> is_set_fee_discount` | `Boolean` | `Whether fee discounts are enabled` |  |
| `>> fee_discount` | `String` | `Account transaction fee discounts` |  |
| `>> is_set_taker_maker_fee_discount` | `Boolean` | `Whether to apply separate fee discounts for takers and makers` |  |
| `>> taker_fee_discount` | `String` | `Taker fee rate discount` |  |
| `>> maker_fee_discount` | `String` | `Maker fee rate discount` |  |
| `> feeSetting` | `Array Object` | `Fee settings` |  |
| `>> symbol` | `String` | `Symbol name` |  |
| `>> is_set_fee_rate` | `Boolean` | `Whether fee rates are set` |  |
| `>> taker_fee_rate` | `String` | `Taker fee rate` |  |
| `>> maker_fee_rate` | `String` | `Maker fee rate` |  |
| `>> is_set_fee_discount` | `Boolean` | `Whether fee discounts are enabled` |  |
| `>> fee_discount` | `String` | `Fee rate discount` |  |
| `>> is_set_taker_maker_fee_discount` | `Boolean` | `Whether to apply separate fee discounts for takers and makers` |  |
| `>> taker_fee_discount` | `String` | `Taker fee rate discount` |  |
| `>> maker_fee_discount` | `String` | `Maker fee rate discount` |  |
| `> modeSetting` | `Array Object` | `Mode settings` |  |
| `>> symbol` | `String` | `Symbol name` |  |
| `>> marginMode` | `String` | `Margin mode` |  |
| `>> separatedMode` | `String` | `Position segregation mode` |  |
| `>> positionMode` | `String` | `Position mode` |  |
| `> leverageSetting` | `Array Object` | `Leverage settings` |  |
| `>> symbol` | `String` | `Symbol name` |  |
| `>> isolated_long_leverage` | `String` | `Isolated long position leverage` |  |
| `>> isolated_short_leverage` | `String` | `Isolated short position leverage` |  |
| `>> cross_leverage` | `String` | `Cross margin leverage` |  |
| `> createOrderRateLimitPerMinute` | `Integer` | `Order creation rate limit per minute` |  |
| `> createOrderDelayMilliseconds` | `Integer` | `Order creation delay (milliseconds)` |  |
| `> createdTime` | `String` | `Creation time Unix millisecond timestamp` |  |
| `> updatedTime` | `String` | `Update time Unix millisecond timestamp` |  |
| `collateral` | `Array Object` | `Collateral information` |  |
| `> coin` | `String` | `Currency` |  |
| `> marginMode` | `String` | `Margin mode` |  |
| `> crossSymbol` | `String` | `When marginMode=CROSS, represents the symbol associated with cross margin mode. Null in other cases.` |  |
| `> isolated_position_id` | `String` | `When marginMode=ISOLATED, represents the position ID associated with isolated margin. 0 in other cases.` |  |
| `> amount` | `String` | `Collateral amount` |  |
| `> pending_deposit_amount` | `String` | `Pending deposit amount` |  |
| `> pending_withdraw_amount` | `String` | `Pending withdrawal amount` |  |
| `> pending_transfer_in_amount` | `String` | `Pending inbound transfer amount` |  |
| `> pending_transfer_out_amount` | `String` | `Pending outbound transfer amount` |  |
| `> is_liquidating` | `Boolean` | `Whether liquidation is triggered (in progress)` |  |
| `> legacy_amount` | `String` | `Legacy balance (display only)` |  |
| `> cum_deposit_amount` | `String` | `Accumulated deposit amount` |  |
| `> cum_withdraw_amount` | `String` | `Accumulated withdrawal amount` |  |
| `> cum_transfer_in_amount` | `String` | `Accumulated inbound transfer amount` |  |
| `> cum_transfer_out_amount` | `String` | `Accumulated outbound transfer amount` |  |
| `> cum_margin_move_in_amount` | `String` | `Accumulated margin deposit amount` |  |
| `> cum_margin_move_out_amount` | `String` | `Accumulated margin withdrawal amount` |  |
| `> cum_position_open_long_amount` | `String` | `Accumulated collateral amount for long position openings` |  |
| `> cum_position_open_short_amount` | `String` | `Accumulated collateral amount for short position openings` |  |
| `> cum_position_close_long_amount` | `String` | `Accumulated collateral amount for long position closings` |  |
| `> cum_position_close_short_amount` | `String` | `Accumulated collateral amount for short position closings` |  |
| `> cum_position_fill_fee_amount` | `String` | `Accumulated trading fees for filled orders` |  |
| `> cum_position_liquidate_fee_amount` | `String` | `Accumulated liquidation fees` |  |
| `> cum_position_funding_amount` | `String` | `Accumulated funding fees` |  |
| `> cum_order_fill_fee_income_amount` | `String` | `Accumulated order fee income` |  |
| `> cum_order_liquidate_fee_income_amount` | `String` | `Accumulated liquidation fee income` |  |
| `> created_time` | `String` | `Creation time,Unix millisecond timestamp` |  |
| `> updated_time` | `String` | `Update time,Unix millisecond timestamp` |  |
| `version` | `String` | `Version number` |  |

## account.auto_add_margin — Automatic Margin Top-Up

- Method: `POST`
- Path: `/capi/v2/account/modifyAutoAppendMargin`
- Category: `account`
- Weight(IP/UID): `15/30`
- Source: https://www.weex.com/api-doc/contract/Account_API/AutoAddMargin

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `positionId` | `Long` | `Yes` | Isolated margin position ID |
| `autoAppendMargin` | `Boolean` | `Yes` | Whether to enable automatic margin call |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `msg` | `String` | Response message |
| `requestTime` | `String` | Timestamp Unix millisecond timestamp |
| `code` | `String` | Response code |

## account.get_assets — Get Account Assets

- Method: `GET`
- Path: `/capi/v2/account/assets`
- Category: `account`
- Weight(IP/UID): `5/10`
- Source: https://www.weex.com/api-doc/contract/Account_API/GetAccountBalance

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coinName` | `String` | `Name of the crypto` |  |
| `available` | `String` | `Available asset` |  |
| `frozen` | `String` | `Frozen asset` |  |
| `equity` | `String` | `Total asset` |  |
| `unrealizePnl` | `String` | `Unrealized Profit and Loss` |  |

## account.get_all_positions — Get All Positions

- Method: `GET`
- Path: `/capi/v2/account/position/allPosition`
- Category: `account`
- Weight(IP/UID): `10/15`
- Source: https://www.weex.com/api-doc/contract/Account_API/GetAllContractPositions

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | `Long` | `Position ID` |  |
| `account_id` | `Long` | `Associated account ID` |  |
| `coin_id` | `Integer` | `Associated collateral currency ID` |  |
| `contract_id` | `Long` | `Associated futures ID` |  |
| `symbol` | `String` | `Trading pair` |  |
| `side` | `String` | `Position direction such as LONG or SHORT` |  |
| `margin_mode` | `String` | `Margin mode of current position SHARED: Cross Mode ISOLATED: Isolated Mode` |  |
| `separated_mode` | `String` | `Current position's separated mode COMBINED: Combined mode SEPARATED: Separated mode` |  |
| `separated_open_order_id` | `Long` | `Opening order ID of separated position` |  |
| `leverage` | `String` | `Position leverage` |  |
| `size` | `String` | `Current position size` |  |
| `open_value` | `String` | `Initial value at position opening` |  |
| `open_fee` | `String` | `Opening fee` |  |
| `funding_fee` | `String` | `Funding fee` |  |
| `marginSize` | `String` | `Margin amount (margin coin)` |  |
| `isolated_margin` | `String` | `Isolated margin` |  |
| `is_auto_append_isolated_margin` | `boolean` | `Whether the auto-adding of funds for the isolated margin is enabled (only for isolated mode)` |  |
| `cum_open_size` | `String` | `Accumulated opened positions` |  |
| `cum_open_value` | `String` | `Accumulated value of opened positions` |  |
| `cum_open_fee` | `String` | `Accumulated fees paid for opened positions` |  |
| `cum_close_size` | `String` | `Accumulated closed positions` |  |
| `cum_close_value` | `String` | `Accumulated value of closed positions` |  |
| `cum_close_fee` | `String` | `Accumulated fees paid for closing positions` |  |
| `cum_funding_fee` | `String` | `Accumulated settled funding fees` |  |
| `cum_liquidate_fee` | `String` | `Accumulated liquidation fees` |  |
| `created_match_sequence_id` | `Long` | `Matching engine sequence ID at creation` |  |
| `updated_match_sequence_id` | `Long` | `Matching engine sequence ID at last update` |  |
| `created_time` | `Long` | `Creation time Unix millisecond timestamp` |  |
| `updated_time` | `Long` | `Update time Unix millisecond timestamp` |  |
| `contractVal` | `String` | `Futures face value` |  |
| `unrealizePnl` | `String` | `Unrealized PnL` |  |
| `liquidatePrice` | `String` | `Estimated liquidation price If the value = 0, it means the position is at low risk and there is no liquidation price at this time` |  |

## account.get_bills — Get Contract Account Bills

- Method: `POST`
- Path: `/capi/v2/account/bills`
- Category: `account`
- Weight(IP/UID): `2/5`
- Source: https://www.weex.com/api-doc/contract/Account_API/GetContractBills

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coin` | `String` | `No` | Currency name |
| `symbol` | `String` | `No` | Trading pair |
| `businessType` | `String` | `No` | Business type deposit : Deposit withdraw : Withdrawal transfer_in : Transfer between different accounts (in) transfer_out : Transfer between different accounts (out) margin_move_in : Collateral transferred within the same account due to opening/closing positions, manual/auto addition margin_move_out : Collateral transferred out within the same account due to opening/closing positions, manual/auto addition position_open_long : Collateral change from opening long positions (buying decreases collateral) position_open_short : Collateral change from opening short positions (selling increases collateral) position_close_long : Collateral change from closing long positions (selling increases collateral) position_close_short : Collateral change from closing short positions (buying decreases collateral) position_funding : Collateral change from position funding fee settlement order_fill_fee_income : Order fill fee income (specific to fee account) order_liquidate_fee_income : Order liquidation fee income (specific to fee account) start_liquidate : Start liquidation finish_liquidate : Finish liquidation order_fix_margin_amount : Compensation for liquidation loss tracking_follow_pay : Copy trading payment, pre-deducted from followers after position closing if profitable tracking_system_pre_receive : Pre-received commission, commission system account receives pre-deducted amount from followers tracking_follow_back : Copy trading commission refund tracking_trader_income : Lead trader income tracking_third_party_share : Profit sharing (shared by lead trader with others) |
| `startTime` | `Long` | `No` | Start timestamp Unit: milliseconds |
| `endTime` | `Long` | `No` | End timestamp Unit: milliseconds |
| `limit` | `Integer` | `No` | Return record limit, default: 20 Minimum: 1 Maximum: 100 |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `billId` | `String` | Bill ID |
| `coin` | `String` | Currency name |
| `symbol` | `String` | Trading pair |
| `amount` | `String` | Amount |
| `businessType` | `String` | Transaction business type |
| `balance` | `String` | Balance |
| `fillFee` | `String` | Transaction fee |
| `transferReason` | `String` | Transfer Reason UNKNOWN_TRANSFER_REASON: Unknown transfer reason USER_TRANSFER: User manual transfer INCREASE_CONTRACT_CASH_GIFT: Increase contract cash gift REDUCE_CONTRACT_CASH_GIFT: Reduce contract cash gift REFUND_WXB_DISCOUNT_FEE: Refund WXB discount fee |
| `cTime` | `String` | Creation time Unix millisecond timestamp |

## account.get_single_position — Get Single Position

- Method: `GET`
- Path: `/capi/v2/account/position/singlePosition`
- Category: `account`
- Weight(IP/UID): `2/3`
- Source: https://www.weex.com/api-doc/contract/Account_API/GetSingleContractPosition

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `id` | `Long` | Position ID |
| `account_id` | `Long` | Associated account ID |
| `coin_id` | `Integer` | Associated collateral currency ID |
| `contract_id` | `Long` | Associated futures ID |
| `symbol` | `String` | Trading pair |
| `side` | `String` | Position direction such as LONG or SHORT |
| `margin_mode` | `String` | Margin mode of current position SHARED: Cross Mode ISOLATED: Isolated Mode |
| `separated_mode` | `String` | Current position's separated mode COMBINED: Combined mode SEPARATED: Separated mode |
| `separated_open_order_id` | `Long` | Opening order ID of separated position |
| `leverage` | `String` | Position leverage |
| `size` | `String` | Current position size |
| `open_value` | `String` | Initial value at position opening |
| `open_fee` | `String` | Opening fee |
| `funding_fee` | `String` | Funding fee |
| `marginSize` | `String` | Margin amount (margin coin) |
| `isolated_margin` | `String` | Isolated margin |
| `is_auto_append_isolated_margin` | `boolean` | Whether the auto-adding of funds for the isolated margin is enabled (only for isolated mode) |
| `cum_open_size` | `String` | Accumulated opened positions |
| `cum_open_value` | `String` | Accumulated value of opened positions |
| `cum_open_fee` | `String` | Accumulated fees paid for opened positions |
| `cum_close_size` | `String` | Accumulated closed positions |
| `cum_close_value` | `String` | Accumulated value of closed positions |
| `cum_close_fee` | `String` | Accumulated fees paid for closing positions |
| `cum_funding_fee` | `String` | Accumulated settled funding fees |
| `cum_liquidate_fee` | `String` | Accumulated liquidation fees |
| `created_match_sequence_id` | `Long` | Matching engine sequence ID at creation |
| `updated_match_sequence_id` | `Long` | Matching engine sequence ID at last update |
| `created_time` | `Long` | Creation time Unix millisecond timestamp |
| `updated_time` | `Long` | Update time Unix millisecond timestamp |
| `contractVal` | `String` | Futures face value |
| `unrealizePnl` | `String` | Unrealized PnL |
| `liquidatePrice` | `String` | Estimated liquidation price If the value = 0, it means the position is at low risk and there is no liquidation price at this time |

## account.get_settings — Get User Settings Of One Single Futures

- Method: `GET`
- Path: `/capi/v2/account/settings`
- Category: `account`
- Weight(IP/UID): `1/1`
- Source: https://www.weex.com/api-doc/contract/Account_API/GetSingleContractUserConfig

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair If not filled in, all will be returned by default. |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `object` | Trading pair |
| `> isolated_long_leverage` | `string` | Isolated long position leverage |
| `> isolated_short_leverage` | `string` | Isolated short position leverage |
| `> cross_leverage` | `string` | Cross margin leverage |

## account.get_account — Get Single Account

- Method: `GET`
- Path: `/capi/v2/account/getAccount`
- Category: `account`
- Weight(IP/UID): `1/1`
- Source: https://www.weex.com/api-doc/contract/Account_API/GetUserSingleAssetInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coin` | `String` | `Yes` | coin name |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `account` | `Object` | Account information |
| `> defaultFeeSetting` | `Object` | Default fee configuration |
| `>> is_set_fee_rate` | `Boolean` | Whether fee rates are set |
| `>> taker_fee_rate` | `String` | Taker fee rate |
| `>> maker_fee_rate` | `String` | Maker fee rate |
| `>> is_set_fee_discount` | `Boolean` | Whether fee discounts are enabled |
| `>> fee_discount` | `String` | Fee rate discount |
| `>> is_set_taker_maker_fee_discount` | `Boolean` | Whether to apply separate fee discounts for takers and makers |
| `>> taker_fee_discount` | `String` | Taker fee rate discount |
| `>> maker_fee_discount` | `String` | Maker fee rate discount |
| `> feeSetting` | `Array Object` | Fee settings |
| `>> symbol` | `String` | Symbol name |
| `>> is_set_fee_rate` | `Boolean` | Whether fee rates are set |
| `>> taker_fee_rate` | `String` | Taker fee rate |
| `>> maker_fee_rate` | `String` | Maker fee rate |
| `>> is_set_fee_discount` | `Boolean` | Whether fee discounts are enabled |
| `>> fee_discount` | `String` | Fee rate discount |
| `>> is_set_taker_maker_fee_discount` | `Boolean` | Whether to apply separate fee discounts for takers and makers |
| `>> taker_fee_discount` | `String` | Taker fee rate discount |
| `>> maker_fee_discount` | `String` | Maker fee rate discount |
| `> modeSetting` | `Array Object` | Mode settings |
| `>> symbol` | `String` | Symbol name |
| `>> marginMode` | `String` | Margin mode |
| `>> separated_mode` | `String` | Position segregation mode |
| `>> position_mode` | `String` | Position mode |
| `> leverageSetting` | `Array Object` | Leverage settings |
| `>> symbol` | `String` | Symbol name |
| `>> isolated_long_leverage` | `String` | Isolated long position leverage |
| `>> isolated_short_leverage` | `String` | Isolated short position leverage |
| `>> cross_leverage` | `String` | Cross margin leverage |
| `> createOrderRateLimitPerMinute` | `Integer` | Order creation rate limit per minute |
| `> createOrderDelayMilliseconds` | `Integer` | Order creation delay (milliseconds) |
| `> createdTime` | `String` | Creation time Unix millisecond timestamp |
| `> updatedTime` | `String` | Update time Unix millisecond timestamp |
| `collateral` | `Array Object` | Collateral information |
| `> coin` | `String` | Currency |
| `> marginMode` | `String` | Margin mode |
| `> crossSymbol` | `String` | When marginMode=CROSS, represents the symbol associated with cross margin mode. Null in other cases. |
| `> isolatedPositionId` | `String` | When marginMode=ISOLATED, represents the position ID associated with isolated margin. 0 in other cases. |
| `> amount` | `String` | Collateral amount |
| `> pending_deposit_amount` | `String` | Pending deposit amount |
| `> pending_withdraw_amount` | `String` | Pending withdrawal amount |
| `> pending_transfer_in_amount` | `String` | Pending inbound transfer amount |
| `> pending_transfer_out_amount` | `String` | Pending outbound transfer amount |
| `> is_liquidating` | `Boolean` | Whether liquidation is triggered (in progress) |
| `> legacy_amount` | `String` | Legacy balance (display only) |
| `> cum_deposit_amount` | `String` | Accumulated deposit amount |
| `> cum_withdraw_amount` | `String` | Accumulated withdrawal amount |
| `> cum_transfer_in_amount` | `String` | Accumulated inbound transfer amount |
| `> cum_transfer_out_amount` | `String` | Accumulated outbound transfer amount |
| `> cum_margin_move_in_amount` | `String` | Accumulated margin deposit amount |
| `> cum_margin_move_out_amount` | `String` | Accumulated margin withdrawal amount |
| `> cum_position_open_long_amount` | `String` | Accumulated collateral amount for long position openings |
| `> cum_position_open_short_amount` | `String` | Accumulated collateral amount for short position openings |
| `> cum_position_close_long_amount` | `String` | Accumulated collateral amount for long position closings |
| `> cum_position_close_short_amount` | `String` | Accumulated collateral amount for short position closings |
| `> cum_position_fill_fee_amount` | `String` | Accumulated trading fees for filled orders |
| `> cum_position_liquidate_fee_amount` | `String` | Accumulated liquidation fees |
| `> cum_position_funding_amount` | `String` | Accumulated funding fees |
| `> cum_order_fill_fee_income_amount` | `String` | Accumulated order fee income |
| `> cum_order_liquidate_fee_income_amount` | `String` | Accumulated liquidation fee income |
| `> created_time` | `String` | Creation time Unix millisecond timestamp |
| `> updated_time` | `String` | Update time Unix millisecond timestamp |
| `version` | `String` | Version number |

## account.change_hold_mode — Modify User Account Mode

- Method: `POST`
- Path: `/capi/v2/account/position/changeHoldModel`
- Category: `account`
- Weight(IP/UID): `20/50`
- Source: https://www.weex.com/api-doc/contract/Account_API/ModifyUserAccountMode

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `marginMode` | `Integer` | `Yes` | Margin mode 1: Cross Mode 3: Isolated Mode |
| `separatedMode` | `Integer` | `No` | Position segregation mode 1: Combined mode System will automatically set to Combined mode by default |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `msg` | `string` | Response message |
| `requestTime` | `string` | Timestamp Unix millisecond timestamp |
| `code` | `string` | Response code |

## market.get_all_tickers — Get All Ticker

- Method: `GET`
- Path: `/capi/v2/market/tickers`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetAllTickerInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Trading pair` |  |
| `last` | `String` | `Latest execution price` |  |
| `best_ask` | `String` | `Ask price` |  |
| `best_bid` | `String` | `Bid price` |  |
| `high_24h` | `String` | `Highest price in the last 24 hours` |  |
| `low_24h` | `String` | `Lowest price in the last 24 hours` |  |
| `volume_24h` | `String` | `Trading volume of quote currency` |  |
| `timestamp` | `String` | `System timestamp Unix millisecond timestamp` |  |
| `priceChangePercent` | `String` | `Price increase or decrease (24 hours)` |  |
| `base_volume` | `String` | `Trading volume of quote currency` |  |
| `markPrice` | `String` | `Mark price` |  |
| `indexPrice` | `String` | `Index price` |  |

## market.get_funding_history — Get Historical Funding Rates

- Method: `GET`
- Path: `/capi/v2/market/getHistoryFundRate`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetContractFundingHistory

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `limit` | `Integer` | `No` | The size of the data ranges from 1 to 100, with a default of 10 |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `string` | Trading pair |
| `fundingRate` | `string` | Funding rate |
| `fundingTime` | `long` | Funding fee settlement time Unix millisecond timestamp |

## market.get_contract_info — Get Futures Information

- Method: `GET`
- Path: `/capi/v2/market/contracts`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetContractInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `underlying_index` | `String` | Futures crypto |
| `quote_currency` | `String` | Quote currency |
| `coin` | `String` | Margin token |
| `contract_val` | `String` | Futures face value |
| `delivery` | `Array` | Settlement times |
| `size_increment` | `String` | Decimal places of the quantity |
| `tick_size` | `String` | Decimal places of the price |
| `forwardContractFlag` | `Boolean` | Whether it is USDT-M futures |
| `priceEndStep` | `BigDecimal` | Step size of the last decimal digit in the price |
| `minLeverage` | `Integer` | Minimum leverage (default: 1) |
| `maxLeverage` | `Integer` | Maximum leverage (default: 100) |
| `buyLimitPriceRatio` | `String` | Ratio of bid price to limit price |
| `sellLimitPriceRatio` | `String` | Ratio of ask price to limit price |
| `makerFeeRate` | `String` | Maker rate |
| `takerFeeRate` | `String` | Taker rate |
| `minOrderSize` | `String` | Minimum order size (base currency) |
| `maxOrderSize` | `String` | Maximum order size (base currency) |
| `maxPositionSize` | `String` | Maximum position size (base currency) |
| `marketOpenLimitSize` | `String` | Market Order Opening Position Single Limit (base currency) |

## market.get_currency_index — Get Cryptocurrency Index

- Method: `GET`
- Path: `/capi/v2/market/index`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetCurrencyIndex

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `priceType` | `String` | `No` | Price Type :  MARK mark; INDEX index; INDEX by default |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `index` | `String` | Index |
| `timestamp` | `String` | Timestamp Unix millisecond timestamp |

## market.get_current_fund_rate — Get Current Funding Rate

- Method: `GET`
- Path: `/capi/v2/market/currentFundRate`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetCurrentFundRate

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `fundingRate` | `String` | Current funding rates |
| `collectCycle` | `Long` | Funding rate settlement cycle Unit: minute |
| `timestamp` | `Long` | Funding fee settlement time Unix millisecond timestamp |

## market.get_depth — Get OrderBook Depth

- Method: `GET`
- Path: `/capi/v2/market/depth`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetDepthData

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `limit` | `Integer` | `No` | Fixed gear enumeration value: 15/200, the default gear is 15 |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `asks` | `List` | Sell side depth data Format: [price, quantity] where quantity is in base currency |
| `Index 0` | `String` | Price |
| `Index 1` | `String` | Quantity |
| `bids` | `List` | Buy side depth data Format: [price, quantity] where quantity is in base currency |
| `Index 0` | `String` | Price |
| `Index 1` | `String` | Quantity |
| `timestamp` | `String` | Timestamp Unix millisecond timestamp |

## market.get_history_candles — Get Historical Candlestick

- Method: `GET`
- Path: `/capi/v2/market/historyCandles`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetHistoryKLineData

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `granularity` | `String` | `Yes` | Candlestick interval[1m,5m,15m,30m,1h,4h,12h,1d,1w] |
| `startTime` | `Long` | `No` | The start time is to query the k-lines after this time Unix millisecond timestamp |
| `endTime` | `Long` | `No` | The end time is to query the k-lines before this time Unix millisecond timestamp |
| `limit` | `Integer` | `No` | The size of the data ranges from 1 to 100, with a default of 100 |
| `priceType` | `String` | `No` | Price Type : LAST latest market price; MARK mark; INDEX index; LAST by default |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `index[0]` | `String` | Candlestick time Unix millisecond timestamp |
| `index[1]` | `String` | Opening price |
| `index[2]` | `String` | Highest price |
| `index[3]` | `String` | Lowest price |
| `index[4]` | `String` | Closing price |
| `index[5]` | `String` | Trading volume of the base coin |
| `index[6]` | `String` | Trading volume of quote currency |

## market.get_candles — Get Candlestick Data

- Method: `GET`
- Path: `/capi/v2/market/candles`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetKLineData

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `granularity` | `String` | `Yes` | Candlestick interval[1m,5m,15m,30m,1h,4h,12h,1d,1w] |
| `limit` | `Integer` | `No` | The size of the data ranges from 1 to 1000, with a default of 100 |
| `priceType` | `String` | `No` | Price Type : LAST latest market price; MARK mark; INDEX index; LAST by default |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `index[0]` | `String` | Candlestick time Unix millisecond timestamp |
| `index[1]` | `String` | Opening price |
| `index[2]` | `String` | Highest price |
| `index[3]` | `String` | Lowest price |
| `index[4]` | `String` | Closing price |
| `index[5]` | `String` | Trading volume of the base coin |
| `index[6]` | `String` | Trading volume of quote currency |

## market.get_next_funding_time — Get Next Funding Time

- Method: `GET`
- Path: `/capi/v2/market/funding_time`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetNextContractSettlementTime

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `fundingTime` | `Long` | Settlement time Unix millisecond timestamp |

## market.get_server_time — Get Server Time

- Method: `GET`
- Path: `/capi/v2/market/time`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetServerTime

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `epoch` | `String` | `Unix timestamp in UTC time zone, represented as a decimal number of seconds` |  |
| `iso` | `String` | `ISO 8601 standard time format` |  |
| `timestamp` | `Long` | `Server time Unix millisecond timestamp` |  |

## market.get_ticker — Get Single Ticker

- Method: `GET`
- Path: `/capi/v2/market/ticker`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetTickerInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `last` | `String` | Latest execution price |
| `best_ask` | `String` | Ask price |
| `best_bid` | `String` | Bid price |
| `high_24h` | `String` | Highest price in the last 24 hours |
| `low_24h` | `String` | Lowest price in the last 24 hours |
| `volume_24h` | `String` | Trading volume of quote currency |
| `timestamp` | `String` | System timestamp Unix millisecond timestamp |
| `priceChangePercent` | `String` | Price increase or decrease (24 hours) |
| `base_volume` | `String` | Trading volume of quote currency |
| `markPrice` | `String` | Mark price |
| `indexPrice` | `String` | Index price |

## market.get_open_interest — Get Open Interest

- Method: `GET`
- Path: `/capi/v2/market/open_interest`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetTotalPlatformOpenInterest

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `base_volume` | `String` | Total open interest of the platform Specific coins |
| `target_volume` | `String` | Quote Currency Holdings |
| `timestamp` | `String` | Timestamp Unix millisecond timestamp |

## market.get_trades — Get Trades

- Method: `GET`
- Path: `/capi/v2/market/trades`
- Category: `market`
- Source: https://www.weex.com/api-doc/contract/Market_API/GetTradeData

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `limit` | `Integer` | `No` | The size of the data ranges from 1 to 1000, with a default of 100 |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `ticketId` | `String` | Filled order ID |
| `time` | `Long` | The time at which the order was filled Unix millisecond timestamp |
| `price` | `String` | The price at which the order was filled |
| `size` | `String` | The quantity that was filled (base currency) |
| `value` | `String` | Filled amount  (quote currency) |
| `symbol` | `String` | Trading pair |
| `isBestMatch` | `Boolean` | Was the trade the best price match? |
| `isBuyerMaker` | `Boolean` | Was the buyer the maker? |
| `contractVal` | `String` | Futures face value (unit: contracts) |

## transaction.cancel_all_orders — Cancel All Orders

- Method: `POST`
- Path: `/capi/v2/order/cancelAllOrders`
- Category: `transaction`
- Weight(IP/UID): `40/50`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/CancelAllOrders

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair. If not provided, orders for all trading pairs will be cancelled |
| `cancelOrderType` | `String` | `Yes` | Order type to cancel: normal : Cancel normal orders plan : Cancel trigger/plan orders |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `orderId` | `Long` | Order ID |
| `success` | `Boolean` | Whether the order was cancelled successfully |

## transaction.cancel_order — Cancel Order

- Method: `POST`
- Path: `/capi/v2/order/cancel_order`
- Category: `transaction`
- Weight(IP/UID): `2/3`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/CancelOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `orderId` | `String` | `No` | Either Order ID or clientOid is required. |
| `clientOid` | `String` | `No` | Either Client customized ID or orderId is required. |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `order_id` | `String` | Order ID |
| `client_oid` | `String` | Client identifier |
| `result` | `Boolean` | Cancellation status |
| `err_msg` | `String` | Error message if cancellation failed |

## transaction.cancel_batch_orders — Batch Cancel Orders

- Method: `POST`
- Path: `/capi/v2/order/cancel_batch_orders`
- Category: `transaction`
- Weight(IP/UID): `5/10`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/CancelOrdersBatch

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ids` | `String[]` | `No` | Either Order ID or cids is required. |
| `cids` | `String[]` | `No` | Either Client customized ID or ids is required. |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `result` | `Boolean` | Processing result (success/failure) |
| `orderIds` | `List<String>` | List of order IDs to be cancelled |
| `clientOids` | `List<String>` | List of client order IDs |
| `cancelOrderResultList` | `List<CancelOrderResult>` | List of cancellation results |
| `failInfos` | `List<CancelOrderResult>` | List of failed cancellation info |

## transaction.cancel_plan_order — Cancel Trigger Order

- Method: `POST`
- Path: `/capi/v2/order/cancel_plan`
- Category: `transaction`
- Weight(IP/UID): `2/3`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/CancelPendingOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `orderId` | `String` | `Yes` | Order ID |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `order_id` | `String` | Order ID |
| `client_oid` | `String` | Client identifier |
| `result` | `Boolean` | Whether the cancellation was successful |
| `err_msg` | `String` | Error message if the cancellation failed |

## transaction.close_positions — Close All Positions

- Method: `POST`
- Path: `/capi/v2/order/closePositions`
- Category: `transaction`
- Weight(IP/UID): `40/50`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/ClosePositions

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair. If not provided, all positions will be closed at market price |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `positionId` | `Long` | Position ID |
| `success` | `Boolean` | Whether the position was successfully closed |
| `successOrderId` | `Long` | Order ID if successful (0 if failed) |
| `errorMessage` | `String` | Error message if the close position failed |

## transaction.get_current_orders — Get Current Orders

- Method: `GET`
- Path: `/capi/v2/order/current`
- Category: `transaction`
- Weight(IP/UID): `2/2`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/GetCurrentOrderStatus

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair |
| `orderId` | `Long` | `No` | OrderId |
| `startTime` | `Long` | `No` | The record start time for the query Unix millisecond timestamp |
| `endTime` | `Long` | `No` | The end time of the record for the query Unix millisecond timestamp |
| `limit` | `Integer` | `No` | Limit number default 100 max 100 |
| `page` | `Integer` | `No` | Page number  default 0 |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `size` | `String` | Order amount |
| `client_oid` | `String` | Client identifier |
| `createTime` | `String` | Creation time Unix millisecond timestamp |
| `filled_qty` | `String` | Filled quantity |
| `fee` | `String` | Transaction fee |
| `order_id` | `String` | Order ID |
| `price` | `String` | Order price |
| `price_avg` | `String` | Average filled price |
| `status` | `String` | Order status pending: The order has been submitted for matching, but the result has not been processed yet. open: The order has been processed by the matching engine (order placed), and may have been partially filled. filled: The order has been completely filled [final state]. canceling: The order is being canceled. canceled: The order has been canceled. It may have been partially filled. [final state]. untriggered: The conditional order has not been triggered yet. |
| `type` | `String` | Order type open_long: Open long open_short: Open short close_long: Close long close_short: Close short offset_liquidate_long: Reduce position, close long offset_liquidate_short: Reduce position, close short agreement_close_long: Agreement close long agreement_close_short: Agreement close short burst_liquidate_long: Liquidation close long burst_liquidate_short: Liquidation close short |
| `order_type` | `String` | Order type normal: Regular limit order, valid until canceled. postOnly: Maker-only order fok: Fill or kill, must be completely filled or canceled immediately. ioc: Immediate or cancel, fill as much as possible and cancel the remaining. |
| `totalProfits` | `String` | Total PnL |
| `contracts` | `Integer` | Order size in contract units |
| `filledQtyContracts` | `Integer` | Filled quantity in contract units |
| `presetTakeProfitPrice` | `String` | Preset take-profit price |
| `presetStopLossPrice` | `String` | Preset stop-loss price |

## transaction.get_current_plan_orders — Get Current Plan Orders

- Method: `GET`
- Path: `/capi/v2/order/currentPlan`
- Category: `transaction`
- Weight(IP/UID): `3/3`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/GetCurrentPendingOrders

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair |
| `orderId` | `Long` | `No` | OrderId  (The filter will be bypassed if invalid characters are input.) |
| `startTime` | `Long` | `No` | The record start time for the query Unix millisecond timestamp |
| `endTime` | `Long` | `No` | The end time of the record for the query Unix millisecond timestamp |
| `limit` | `Integer` | `No` | Limit number default 100 max 100 |
| `page` | `Integer` | `No` | Page number  default 0 |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `size` | `String` | Order amount |
| `client_oid` | `String` | Client identifier |
| `createTime` | `String` | Creation time Unix millisecond timestamp |
| `filled_qty` | `String` | Filled quantity |
| `fee` | `String` | Transaction fee |
| `order_id` | `String` | Order ID |
| `price` | `String` | Order price |
| `price_avg` | `String` | Average filled price |
| `status` | `String` | Order status: -1: Canceled. 0: Pending. 1: Partially filled. 2: Filled |
| `type` | `String` | Order Type: 1. Open long. 2: Open short. 3: Close long. 4: Close short. 5: Partial close long. 6: Partial close short. 7: Auto-deleveraging (close long). 8: Auto-deleveraging (close short). 9: Liquidation (close long). 10. Liquidation (close short). |
| `order_type` | `String` | Order type: 0: Normal order. 1: Post-only. 2: Fill-Or-Kill (FOK) order. 3: Immediate-Or-Cancel (IOC) order. |
| `totalProfits` | `String` | Total PnL |
| `triggerPrice` | `String` | Trigger price |
| `triggerPriceType` | `String` | Trigger price type |
| `triggerTime` | `String` | Trigger time Unix millisecond timestamp |
| `presetTakeProfitPrice` | `String` | Preset take-profit price |
| `presetStopLossPrice` | `String` | Preset stop-loss price |

## transaction.get_history_plan_orders — Get History Plan Orders

- Method: `GET`
- Path: `/capi/v2/order/historyPlan`
- Category: `transaction`
- Weight(IP/UID): `5/10`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/GetHistoricalPendingOrders

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `startTime` | `Long` | `No` | Start time Unix millisecond timestamp |
| `endTime` | `Long` | `No` | End time Unix millisecond timestamp |
| `delegateType` | `Integer` | `No` | Order type: 1: Open long. 2: Open short. 3: Close long. 4: Close short. |
| `pageSize` | `Integer` | `No` | Items per page, ranging from 1 to 100, default is 100. |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `size` | `String` | Order quantity |
| `client_oid` | `String` | Client identifier |
| `createTime` | `String` | Creation time Unix millisecond timestamp |
| `filled_qty` | `String` | Filled quantity |
| `fee` | `String` | Transaction fee |
| `order_id` | `String` | Order ID |
| `price` | `String` | Order price |
| `price_avg` | `String` | Average filled price |
| `status` | `String` | Order status: -1: Canceled. 0: Pending. 1: Partially filled. 2: Filled |
| `type` | `String` | Order Type: 1. Open long. 2: Open short. 3: Close long. 4: Close short. 5: Partial close long. 6: Partial close short. 7: Auto-deleveraging (close long). 8: Auto-deleveraging (close short). 9: Liquidation (close long). 10. Liquidation (close short). |
| `order_type` | `String` | Order type: 0: Normal order. 1: Post-only. 2: Fill-Or-Kill (FOK) order. 3: Immediate-Or-Cancel (IOC) order. |
| `totalProfits` | `String` | Total PnL |
| `triggerPrice` | `String` | Trigger price |
| `triggerPriceType` | `String` | Trigger price type |
| `triggerTime` | `String` | Trigger time Unix millisecond timestamp |
| `presetTakeProfitPrice` | `String` | Preset take-profit price |
| `presetStopLossPrice` | `String` | Preset stop-loss price |

## transaction.get_history_orders — Get History Orders

- Method: `GET`
- Path: `/capi/v2/order/history`
- Category: `transaction`
- Weight(IP/UID): `10/10`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/GetOrderHistory

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair |
| `pageSize` | `Integer` | `No` | Items per page |
| `createDate` | `Long` | `No` | The record start time for the query (must be ≤ 90 and cannot be negative) Unix millisecond timestamp |
| `endCreateDate` | `Long` | `No` | The end time of the record for the query (must be ≤ 90 and cannot be negative) Unix millisecond timestamp |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `Symbol` | `String` | Trading pair |
| `size` | `String` | Order amount |
| `client_oid` | `String` | Client identifier |
| `createTime` | `String` | Creation time Unix millisecond timestamp |
| `filled_qty` | `String` | Filled quantity |
| `fee` | `String` | Transaction fee |
| `order_id` | `String` | Order ID |
| `price` | `String` | Order price |
| `price_avg` | `String` | Average filled price |
| `status` | `String` | Order status pending: The order has been submitted for matching, but the result has not been processed yet. open: The order has been processed by the matching engine (order placed), and may have been partially filled. filled: The order has been completely filled [final state]. canceling: The order is being canceled. canceled: The order has been canceled. It may have been partially filled. [final state]. untriggered: The conditional order has not been triggered yet. |
| `type` | `String` | Order type open_long: Open long open_short: Open short close_long: Close long close_short: Close short offset_liquidate_long: Reduce position, close long offset_liquidate_short: Reduce position, close short agreement_close_long: Agreement close long agreement_close_short: Agreement close short burst_liquidate_long: Liquidation close long burst_liquidate_short: Liquidation close short |
| `order_type` | `String` | Order type normal: Regular limit order, valid until canceled. postOnly: Maker-only order fok: Fill or kill, must be completely filled or canceled immediately. ioc: Immediate or cancel, fill as much as possible and cancel the remaining. |
| `totalProfits` | `String` | Total PnL |
| `contracts` | `Integer` | Order size in contract units |
| `filledQtyContracts` | `Integer` | Filled quantity in contract units |
| `presetTakeProfitPrice` | `String` | Preset take-profit price |
| `presetStopLossPrice` | `String` | Preset stop-loss price |

## transaction.get_order_info — Get Order Info

- Method: `GET`
- Path: `/capi/v2/order/detail`
- Category: `transaction`
- Weight(IP/UID): `2/2`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/GetSingleOrderInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `orderId` | `String` | `Yes` | Order ID |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `symbol` | `String` | Trading pair |
| `size` | `String` | Order amount |
| `client_oid` | `String` | Client identifier |
| `createTime` | `long` | Creation time Unix millisecond timestamp |
| `filled_qty` | `String` | Filled quantity |
| `fee` | `String` | Transaction fee |
| `order_id` | `String` | Order ID |
| `price` | `String` | Order price |
| `price_avg` | `String` | Average filled price |
| `status` | `string` | Order status pending: The order has been submitted for matching, but the result has not been processed yet. open: The order has been processed by the matching engine (order placed), and may have been partially filled. filled: The order has been completely filled [final state]. canceling: The order is being canceled. canceled: The order has been canceled. It may have been partially filled. [final state]. untriggered: The conditional order has not been triggered yet. |
| `type` | `string` | Order type open_long: Open long open_short: Open short close_long: Close long close_short: Close short offset_liquidate_long: Reduce position, close long offset_liquidate_short: Reduce position, close short agreement_close_long: Agreement close long agreement_close_short: Agreement close short burst_liquidate_long: Liquidation close long burst_liquidate_short: Liquidation close short |
| `order_type` | `string` | Order type normal: Regular limit order, valid until canceled. postOnly: Maker-only order fok: Fill or kill, must be completely filled or canceled immediately. ioc: Immediate or cancel, fill as much as possible and cancel the remaining. |
| `totalProfits` | `String` | Total PnL |
| `contracts` | `Integer` | Order size in contract units |
| `filledQtyContracts` | `Integer` | Filled quantity in contract units |
| `presetTakeProfitPrice` | `String` | Preset take-profit price |
| `presetStopLossPrice` | `String` | Preset stop-loss price |

## transaction.get_fills — Get Fills

- Method: `GET`
- Path: `/capi/v2/order/fills`
- Category: `transaction`
- Weight(IP/UID): `5/5`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/GetTradeDetails

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair name |
| `orderId` | `Long` | `No` | Order ID |
| `startTime` | `Long` | `No` | Start timestamp Unix millisecond timestamp |
| `endTime` | `Long` | `No` | End timestamp Unix millisecond timestamp |
| `limit` | `Long` | `No` | Number of queries: Maximum: 100, default: 100 |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `list` | `List` | Transaction details |
| `> tradeId` | `Integer` | Filled order ID |
| `> orderId` | `Integer` | Associated order ID |
| `> symbol` | `String` | Trading pair name |
| `> marginMode` | `String` | Margin mode |
| `> separatedMode` | `String` | Separated mode |
| `> positionSide` | `String` | Position direction |
| `> orderSide` | `String` | Order direction |
| `> fillSize` | `String` | Actual filled quantity |
| `> fillValue` | `String` | Actual filled value |
| `> fillFee` | `String` | Actual trading fee |
| `> liquidateFee` | `String` | Closing fee |
| `> realizePnl` | `String` | Actual realized PnL |
| `> direction` | `String` | Actual execution direction |
| `> liquidateType` | `String` | Liquidation order type |
| `> legacyOrdeDirection` | `String` | Compatible with legacy order direction types |
| `> createdTime` | `Integer` | Timestamp Unix millisecond timestamp |
| `nextFlag` | `Boolean` | Whether more pages exist |
| `totals` | `Integer` | Total entries |

## transaction.modify_tpsl_order — Modify TP/SL Order

- Method: `POST`
- Path: `/capi/v2/order/modifyTpSlOrder`
- Category: `transaction`
- Weight(IP/UID): `2/5`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/ModifyTpSlOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `orderId` | `Long` | `Yes` | Order ID of the TP/SL order to modify |
| `triggerPrice` | `String` | `Yes` | New trigger price |
| `executePrice` | `String` | `No` | New execution price. If not provided or set to 0, market price will be used. Value > 0 means limit price |
| `triggerPriceType` | `Integer` | `No` | Trigger price type: 1: Last price 3: Mark price Default is 1 (Last price) |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `code` | `String` | Response code, "00000" indicates success |
| `msg` | `String` | Response message |
| `requestTime` | `Long` | return time Unix millisecond timestamp |
| `data` | `Object` | Response data (null for this endpoint) |

## transaction.place_order — Place Order

- Method: `POST`
- Path: `/capi/v2/order/placeOrder`
- Category: `transaction`
- Weight(IP/UID): `2/5`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/PlaceOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `client_oid` | `String` | `Yes` | Custom order ID (no more than 40 characters) |
| `size` | `String` | `Yes` | Amount (base coin) To get the decimal places of size: Get Futures Information |
| `type` | `String` | `Yes` | 1: Open long, 2: Open short, 3: Close long, 4: Close short |
| `order_type` | `String` | `Yes` | 0: Normal, 1: Post-Only, 2: Fill-Or-Kill, 3: Immediate Or Cancel |
| `match_price` | `String` | `Yes` | 0: Limit price, 1: Market price |
| `price` | `String` | `Yes` | Order price (this is required for limit orders, and its accuracy and step size follow the futures information endpoint) |
| `presetTakeProfitPrice` | `BigDecimal` | `No` | Preset take-profit price |
| `presetStopLossPrice` | `BigDecimal` | `No` | Preset stop-loss price |
| `marginMode` | `Integer` | `No` | Margin mode 1: Cross Mode 3: Isolated Mode Default is 1 (Cross Mode) |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `client_oid` | `String` | Client-generated order identifier |
| `order_id` | `String` | Order ID |

## transaction.batch_orders — Batch Orders

- Method: `POST`
- Path: `/capi/v2/order/batchOrders`
- Category: `transaction`
- Weight(IP/UID): `5/10`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/PlaceOrdersBatch

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `marginMode` | `Integer` | `No` | Margin mode 1: Cross Mode 3: Isolated Mode Default is 1 (Cross Mode) |
| `orderDataList` | `List` | `Yes` | Maximum batch processing limit of 20 orders, with the same structure as the futures placing endpoint |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `order_info` | `List` | Order list |
| `>order_id` | `String` | Order ID |
| `>client_oid` | `String` | Customize order ID |
| `>result` | `Boolean` | Order status |
| `>error_code` | `String` | Error code if order placement failed |
| `>error_message` | `String` | Error message if order placement failed |
| `result` | `Boolean` | Request result |

## transaction.place_plan_order — Place Trigger Order

- Method: `POST`
- Path: `/capi/v2/order/plan_order`
- Category: `transaction`
- Weight(IP/UID): `2/5`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/PlacePendingOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `client_oid` | `String` | `Yes` | Custom order ID (≤40 chars, no special characters), must be unique in maker ordersIf left empty, the system will automatically assign a value. |
| `size` | `String` | `Yes` | Order quantity (base coin) To get the decimal places of size: Get Futures Information |
| `type` | `String` | `Yes` | 1: Open long 2. Open short 3. Close long 4. Close short |
| `match_type` | `String` | `Yes` | 0: Limit price, 1: Market price |
| `execute_price` | `String` | `Yes` | Execution price |
| `trigger_price` | `String` | `Yes` | Trigger price |
| `marginMode` | `Integer` | `No` | Margin mode 1: Cross Mode 3: Isolated Mode Default is 1 (Cross Mode) |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `client_oid` | `` | Client identifier |
| `order_id` | `` | Conditional order ID |

## transaction.place_tpsl_order — Place TP/SL Order

- Method: `POST`
- Path: `/capi/v2/order/placeTpSlOrder`
- Category: `transaction`
- Weight(IP/UID): `2/5`
- Source: https://www.weex.com/api-doc/contract/Transaction_API/PlaceTpSlOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair |
| `clientOrderId` | `String` | `Yes` | Custom order ID (no more than 40 characters) |
| `planType` | `String` | `Yes` | TP/SL type: profit_plan : Take-profit plan order loss_plan : Stop-loss plan order |
| `triggerPrice` | `String` | `Yes` | Trigger price |
| `executePrice` | `String` | `No` | Execution price. If not provided or set to 0, market price will be used. Value > 0 means limit price |
| `size` | `String` | `Yes` | Order quantity (base coin) To get the decimal places of size: Get Futures Information |
| `positionSide` | `String` | `Yes` | Position direction: long : Long position short : Short position |
| `marginMode` | `Integer` | `No` | Margin mode: 1: Cross Mode 3: Isolated Mode Default is 1 (Cross Mode) |

### Response Parameters

| Name | Type | Description |
|---|---|---|
| `success` | `Boolean` | Whether the TP/SL order was placed successfully |
| `orderId` | `Long` | Order ID (0 if failed) |

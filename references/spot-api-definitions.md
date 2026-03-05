# WEEX Spot API Definitions (Local)

Generated from English docs on 2026-03-05.

- Base URL: `https://api-spot.weex.com`
- Total endpoints: **28**

## Index

| Key | Method | Path | Auth |
|---|---|---|---|
| `spot.account.getaccountbalance` | `GET` | `/api/v2/account/assets` | `True` |
| `spot.account.getbillrecords` | `POST` | `/api/v2/account/bills` | `True` |
| `spot.account.getfundbillrecords` | `POST` | `/api/v2/account/fundingBills` | `True` |
| `spot.account.transferrecords` | `GET` | `/api/v2/account/transferRecords` | `True` |
| `spot.config.currencyinfo` | `GET` | `/api/v2/public/currencies` | `False` |
| `spot.config.getallproductinfo` | `GET` | `/api/v2/public/products` | `False` |
| `spot.config.getproductinfo` | `GET` | `/api/v2/public/exchangeInfo` | `False` |
| `spot.config.getservertime` | `GET` | `/api/v2/public/time` | `False` |
| `spot.market.getalltickerinfo` | `GET` | `/api/v2/market/tickers` | `False` |
| `spot.market.getdepthdata` | `GET` | `/api/v2/market/depth` | `False` |
| `spot.market.getklinedata` | `GET` | `/api/v2/market/candles` | `False` |
| `spot.market.gettickerinfo` | `GET` | `/api/v2/market/ticker` | `False` |
| `spot.market.gettradedata` | `GET` | `/api/v2/market/fills` | `False` |
| `spot.order.bulkcancel` | `POST` | `/api/v2/trade/cancel-batch-orders` | `True` |
| `spot.order.bulkorder` | `POST` | `/api/v2/trade/batch-orders` | `True` |
| `spot.order.cancel_symbol_orders` | `POST` | `/api/v2/trade/cancel-symbol-order` | `True` |
| `spot.order.cancelorder` | `POST` | `/api/v2/trade/cancel-order` | `True` |
| `spot.order.historyorders` | `POST` | `/api/v2/trade/history` | `True` |
| `spot.order.orderdetails` | `POST` | `/api/v2/trade/orderInfo` | `True` |
| `spot.order.placeorder` | `POST` | `/api/v2/trade/orders` | `True` |
| `spot.order.transactiondetails` | `POST` | `/api/v2/trade/fills` | `True` |
| `spot.order.unfinishedorders` | `POST` | `/api/v2/trade/open-orders` | `True` |
| `spot.rebate.getaffiliatecommission` | `GET` | `/api/v2/rebate/affiliate/getAffiliateCommission` | `True` |
| `spot.rebate.getaffiliateuids` | `GET` | `/api/v2/rebate/affiliate/getAffiliateUIDs` | `True` |
| `spot.rebate.getchannelusertradeandasset` | `GET` | `/api/v2/rebate/affiliate/getChannelUserTradeAndAsset` | `True` |
| `spot.rebate.getinternalwithdrawalstatus` | `GET` | `/api/v2/rebate/affiliate/getInternalWithdrawalStatus` | `True` |
| `spot.rebate.internalwithdrawal` | `POST` | `/api/v2/rebate/affiliate/internalWithdrawal` | `True` |
| `spot.rebate.querysubchanneltransactions` | `POST` | `/api/v2/rebate/affiliate/querySubChannelTransactions` | `True` |

## spot.account.getaccountbalance — Get Account Assets

- Method: `GET`
- Path: `/api/v2/account/assets`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/AccountAPI/GetAccountBalance

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coinId` | `Integer` | `Crypto ID` |  |
| `coinName` | `String` | `Name of the crypto` |  |
| `available` | `String` | `Available asset` |  |
| `frozen` | `String` | `Frozen asset` |  |
| `equity` | `String` | `Total asset` |  |

## spot.account.getbillrecords — Get Spot Account Bills

- Method: `POST`
- Path: `/api/v2/account/bills`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/AccountAPI/GetBillRecords

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coinId` | `Integer` | `No` | Crypto ID |
| `bizType` | `String` | `No` | Business type deposit: Deposit withdraw: Withdrawal transfer_in: Transfer-in transfer_out: Transfer-out trade_in: Asset purchase trade_out: Asset sale rake_back_reward: Commission rebate reward airdrop_reward: Financial airdrop reward rr_agent_reward: Referral commission reward launch_pad_airdrop_in: LaunchPool airdrop transfer in launch_pad_airdrop_out: LaunchPool airdrop transfer out system_issued: System issued airdrop_reward_for_product_activity: Product activity airdrop reward red_packet_create: Red packet creation red_packet_claim: Red packet claim red_packet_refund: Red packet refund |
| `after` | `Long` | `No` | Records created AFTER this timestamp |
| `before` | `Long` | `No` | Records created BEFORE this timestamp |
| `limit` | `Integer` | `No` | Number of results, default: 10, maximum: 100. |

## spot.account.getfundbillrecords — Get Funding Account Bill

- Method: `POST`
- Path: `/api/v2/account/fundingBills`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/AccountAPI/GetFundBillRecords

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coinId` | `Integer` | `No` | Currency ID |
| `startTime` | `Long` | `No` | Records created after start time |
| `endTime` | `Long` | `No` | Records created before end time |
| `pageIndex` | `Integer` | `No` | Page number, default 1 |
| `pageSize` | `Integer` | `No` | Number of results to return, default 10, maximum 100 |

## spot.account.transferrecords — Get Transfer Record

- Method: `GET`
- Path: `/api/v2/account/transferRecords`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/AccountAPI/TransferRecords

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coinId` | `Integer` | `No` | Crypto ID |
| `fromType` | `String` | `No` | Account type (accountType) |
| `after` | `Long` | `No` | Pass to tradeTime and retrieve the data before this tradeTime. |
| `before` | `Long` | `No` | Pass to tradeTime and retrieve the data after this tradeTime. |
| `limit` | `Integer` | `No` | Number of results, default: 100, maximum: 500. |

## spot.config.currencyinfo — Basic Crypto Information

- Method: `GET`
- Path: `/api/v2/public/currencies`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/ConfigAPI/CurrencyInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `coinId` | `Crypto ID` | `` |  |
| `coinName` | `Name of the crypto` | `` |  |
| `transfer` | `Whether transfer is supported` | `` |  |
| `chains` | `Blockchain information` | `` |  |
| `> chain` | `Name of the blockchain` | `` |  |
| `> needTag` | `Whether a tag is required` | `` |  |
| `> withdrawAble` | `Whether withdrawals are enabled` | `` |  |
| `> rechargeAble` | `Whether deposits are enabled` | `` |  |
| `> withdrawFee` | `Withdrawal transaction fee` | `` |  |
| `> depositConfirm` | `Number of block confirmations required for deposits` | `` |  |
| `> withdrawConfirm` | `Number of block confirmations required for withdrawals` | `` |  |
| `> minDepositAmount` | `Minimum deposit amount` | `` |  |
| `> minWithdrawAmount` | `Minimum withdrawal amount` | `` |  |
| `> browserUrl` | `Blockchain explorer URL for the network` | `` |  |

## spot.config.getallproductinfo — API Default Symbol

- Method: `GET`
- Path: `/api/v2/public/products`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/ConfigAPI/GetAllProductInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | `array` | `Trading pairs supported for API trading` |  |

## spot.config.getproductinfo — Get Symbol Info

- Method: `GET`
- Path: `/api/v2/public/exchangeInfo`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/ConfigAPI/GetProductInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `No` | Trading pair name, e.g. BTCUSDT_SPBL |
| `symbols` | `String` | `No` | Multiple trading pair names,e.g. BTCUSDT_SPBL,ETHUSDC_SPBL |

## spot.config.getservertime — Get Server Time

- Method: `GET`
- Path: `/api/v2/public/time`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/ConfigAPI/GetServerTime

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `data` | `Long` | `Server time` |  |

## spot.market.getalltickerinfo — Get All Ticker

- Method: `GET`
- Path: `/api/v2/market/tickers`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/MarketDataAPI/GetAllTickerInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Trading pair name` |  |
| `priceChange` | `String` | `Price change amount` |  |
| `priceChangePercent` | `String` | `Price change percentage` |  |
| `trades` | `long` | `24-hour trade count` |  |
| `size` | `String` | `24-hour trading volume (quantity)` |  |
| `value` | `String` | `24-hour trading value (amount)` |  |
| `high` | `String` | `24-hour highest price` |  |
| `low` | `String` | `24-hour lowest price` |  |
| `open` | `String` | `Opening price (24-hour period)` |  |
| `close` | `String` | `Closing price (24-hour period)` |  |
| `highTime` | `long` | `Timestamp of 24-hour high` |  |
| `lowTime` | `long` | `Timestamp of 24-hour low` |  |
| `startTime` | `long` | `Start timestamp of 24-hour period` |  |
| `endTime` | `long` | `End timestamp of 24-hour period` |  |
| `lastPrice` | `String` | `Last traded price` |  |
| `openInterest` | `String` | `Open interest (for derivatives)` |  |
| `ts` | `long` | `System timestamp` |  |

## spot.market.getdepthdata — Get OrderBook Depth

- Method: `GET`
- Path: `/api/v2/market/depth`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/MarketDataAPI/GetDepthData

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Futures name |
| `type` | `String` | `No` | Default: step0: no aggregation.Values: step0, step1, step2, step3, step4, step5 |
| `limit` | `String` | `No` | Number of entries (Only 15 and 200) |

## spot.market.getklinedata — Get Candlestick Data

- Method: `GET`
- Path: `/api/v2/market/candles`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/MarketDataAPI/GetKLineData

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Futures name |
| `period` | `String` | `Yes` | Candlestick interval, valid values include: [1m,5m,15m,30m,1h,2h,4h,6h,8h,12h,1d,1w,1M] |
| `limit` | `String` | `No` | Number of results |

## spot.market.gettickerinfo — Get Single Ticker

- Method: `GET`
- Path: `/api/v2/market/ticker`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/MarketDataAPI/GetTickerInfo

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair name |

## spot.market.gettradedata — Get Trades

- Method: `GET`
- Path: `/api/v2/market/fills`
- Requires Auth: `False`
- Source: https://www.weex.com/api-doc/spot/MarketDataAPI/GetTradeData

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair ID |
| `limit` | `String` | `No` | Default: 100, max: 1,000 |

## spot.order.bulkcancel — Batch Cancel Orders

- Method: `POST`
- Path: `/api/v2/trade/cancel-batch-orders`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/BulkCancel

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair. For details, view: /products |
| `orderIds` | `String[]` | `No` | Either Order ID or clientOids is required. |
| `clientOids` | `String[]` | `No` | Either Client customized ID or orderIds is required. |

## spot.order.bulkorder — Batch Place Orders

- Method: `POST`
- Path: `/api/v2/trade/batch-orders`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/BulkOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pairs. For details, view: /products |
| `orderList` | `List` | `Yes` | Order list |

## spot.order.cancel_symbol_orders — Cancel Order by Symbol

- Method: `POST`
- Path: `/api/v2/trade/cancel-symbol-order`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/Cancel-Symbol-Orders

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair. For details, view: /products |

## spot.order.cancelorder — Cancel Order

- Method: `POST`
- Path: `/api/v2/trade/cancel-order`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/CancelOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair. For details, view: /products |
| `orderId` | `String` | `No` | Either Order ID or clientOid is required. |
| `clientOid` | `String` | `No` | Either Client customized ID or orderId is required. |

## spot.order.historyorders — Get History Orders

- Method: `POST`
- Path: `/api/v2/trade/history`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/HistoryOrders

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair. For details, view: /products |
| `after` | `Long` | `No` | Start timestamp (in milliseconds) |
| `before` | `Long` | `No` | End timestamp (in milliseconds) |
| `pageIndex` | `Integer` | `No` | Page number, starting from 0 (Default: 0) |
| `pageSize` | `Integer` | `No` | Page size, must be greater than 0 and less than or equal to 100 (Default: 10) |

## spot.order.orderdetails — Get Order Info

- Method: `POST`
- Path: `/api/v2/trade/orderInfo`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/OrderDetails

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `orderId` | `String` | `No` | Either Order ID or clientOrderId is required. |
| `clientOrderId` | `String` | `No` | Either Client customized ID or orderId is required. |

## spot.order.placeorder — Place Order

- Method: `POST`
- Path: `/api/v2/trade/orders`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/PlaceOrder

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pairs. For details, view: /products ) |
| `side` | `String` | `Yes` | Order direction buy: Buy sell: Sell |
| `orderType` | `String` | `Yes` | Order type limit: Limit order market: Market order |
| `force` | `String` | `Yes` | Order execution type (It is invalid when orderType is market) normal: Normal limit order, good till cancelled postOnly: Post-only order (maker only) fok: Fill or kill ioc: Immediate or cancel |
| `price` | `String` | `No` | Limit price  (required when orderType is 'limit') |
| `quantity` | `String` | `Yes` | Order amount |
| `clientOrderId` | `String` | `Yes` | Customizable order ID |

## spot.order.transactiondetails — Get Fills

- Method: `POST`
- Path: `/api/v2/trade/fills`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/TransactionDetails

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair. For details, view: /products |
| `orderId` | `Long` | `No` | Order ID |
| `after` | `Long` | `No` | Start timestamp (in milliseconds) |
| `before` | `Long` | `No` | End timestamp (in milliseconds) |
| `pageIndex` | `Integer` | `No` | Page number, starting from 0 (Default: 0) |
| `pageSize` | `Integer` | `No` | Page size, must be greater than 0 and less than or equal to 100 (Default: 10) |

## spot.order.unfinishedorders — Get Current Orders

- Method: `POST`
- Path: `/api/v2/trade/open-orders`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/orderApi/UnfinishedOrders

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | `String` | `Yes` | Trading pair. For details, view: /products |
| `limit` | `Integer` | `No` | Number of records to retrieve. Must be greater than 0 and less than or equal to 100. |
| `pageNo` | `Integer` | `No` | Page number (starting from 0, default 0) |

## spot.rebate.getaffiliatecommission — Get Affiliate Commission

- Method: `GET`
- Path: `/api/v2/rebate/affiliate/getAffiliateCommission`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/rebate-endpoints/GetAffiliateCommission

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | `Long` | `No` | Invited User UID |
| `startTime` | `Long` | `No` | Start timestamp in UTC (milliseconds). Default: 7 days ago,Max range: 3 months |
| `endTime` | `Long` | `No` | End timestamp in UTC (milliseconds). Default: current time,Max range: 3 months |
| `coin` | `String` | `No` | USDT or BTC |
| `productType` | `String` | `No` | SPOT or FUTURES (default SPOT) |
| `page` | `Integer` | `No` | Page number (starting from 1, default 1) |
| `pageSize` | `Integer` | `No` | Page size (default 100) |

## spot.rebate.getaffiliateuids — Get Affiliate UIDs

- Method: `GET`
- Path: `/api/v2/rebate/affiliate/getAffiliateUIDs`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/rebate-endpoints/GetAffiliateUIDs

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | `Long` | `No` | Invited User UID |
| `startTime` | `Long` | `No` | Start timestamp in UTC (milliseconds) |
| `endTime` | `Long` | `No` | End timestamp in UTC (milliseconds) |
| `page` | `Integer` | `No` | Page number (starting from 1, default 1) |
| `pageSize` | `Integer` | `No` | Page size (default 100) |

## spot.rebate.getchannelusertradeandasset — Get Affiliate Referral Data

- Method: `GET`
- Path: `/api/v2/rebate/affiliate/getChannelUserTradeAndAsset`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/rebate-endpoints/GetChannelUserTradeAndAsset

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | `Long` | `No` | Invited User UID |
| `startTime` | `Long` | `No` | Start timestamp in UTC (milliseconds) |
| `endTime` | `Long` | `No` | End timestamp in UTC (milliseconds) |
| `page` | `Integer` | `No` | Page number (starting from 1, default 1) |
| `pageSize` | `Integer` | `No` | Page size (default 100) |

## spot.rebate.getinternalwithdrawalstatus — Get Internal Withdrawal Status

- Method: `GET`
- Path: `/api/v2/rebate/affiliate/getInternalWithdrawalStatus`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/rebate-endpoints/GetInternalWithdrawalStatus

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `withdrawID` | `String` | `No` | Withdraw ID |
| `coin` | `String` | `No` | Currency type (USDT, BTC) |
| `startTime` | `Long` | `No` | Start timestamp in UTC (milliseconds) (Only data from the past month can be queried) |
| `endTime` | `Long` | `No` | End timestamp in UTC (milliseconds) (Only data from the past month can be queried) |
| `fromAccountType` | `String` | `No` | Type of the originating account (SPOT: spot wallet, FUND: funding wallet, Default: SPOT) |
| `toAccountType` | `String` | `No` | Type of the target account (SPOT: spot wallet, FUND: funding wallet, Default: SPOT) |
| `page` | `Integer` | `No` | Page number (starting from 1, default 1) |
| `pageSize` | `Integer` | `No` | Page size (default 100, max 200) |

## spot.rebate.internalwithdrawal — Internal Withdrawal

- Method: `POST`
- Path: `/api/v2/rebate/affiliate/internalWithdrawal`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/rebate-endpoints/InternalWithdrawal

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `toUserId` | `Long` | `Yes` | Transfer-in user ID |
| `coin` | `String` | `Yes` | Currency type (USDT, BTC) |
| `amount` | `String` | `Yes` | Transfer amount (Up to 6 decimal places) |
| `fromAccountType` | `String` | `No` | Type of the originating account (SPOT: spot wallet, FUND: funding wallet, Default: SPOT) |
| `toAccountType` | `String` | `No` | Type of the target account (SPOT: spot wallet, FUND: funding wallet, Default: SPOT) |

## spot.rebate.querysubchanneltransactions — Get Subaffiliates Data (affiliate only)

- Method: `POST`
- Path: `/api/v2/rebate/affiliate/querySubChannelTransactions`
- Requires Auth: `True`
- Source: https://www.weex.com/api-doc/spot/rebate-endpoints/QuerySubChannelTransactions

### Request Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subUid` | `Long` | `No` | Sub-affiliate's UID |
| `startTime` | `Long` | `No` | Start timestamp (UTC milliseconds) |
| `endTime` | `Long` | `No` | End timestamp (UTC milliseconds) |
| `productType` | `String` | `Yes` | Product type (SPOT or FUTURES) |
| `pageNum` | `Integer` | `No` | Page number (starts from 1, default 1) |
| `pageSize` | `Integer` | `No` | Items per page (default 100) |

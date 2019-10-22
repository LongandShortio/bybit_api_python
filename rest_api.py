# longandshort.io
# Implementation of https://github.com/bybit-exchange/bybit-official-api-docs/blob/master/en/README.md
import requests
import os
import websocket,time
import hmac
import hashlib
import json
import random

class Account:
    def __init__(self, api_key, secret, leverage, url="https://api-testnet.bybit.com"):
        """Use https://api.bybit.com if you do not want to use the Testnet"""
        self.api_key=api_key
        self.secret = secret
        self.leverage=leverage
        self.url=url


    def get_signature(self,param_str):
        return str(hmac.new(bytes(self.secret, "utf-8"), bytes(param_str, "utf-8"), digestmod="sha256").hexdigest())

    def auth(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }

        r = requests.post(self.url+'/user/leverage/save', data)
        return json.loads(r.text)

    def place_active_order(self, side,  qty, price,stop_loss,take_profit,order_type="Limit",time_in_force='GoodTillCancel'):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&order_type={order_type}&price={price}&qty={qty}&side={side}&stop_loss={stop_loss}&symbol=BTCUSD&take_profit={take_profit}&time_in_force={time_in_force}&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "timestamp":timestamp,

            "side":side,
            "symbol":"BTCUSD",
            "order_type":order_type,
            "qty":qty,
            "price": price,
            "time_in_force":time_in_force,
            "take_profit":take_profit,
            "stop_loss": stop_loss,
            "sign":sign
            }
        r=requests.post(self.url+'/open-api/order/create',data)
        return json.loads(r.text)

    def market_close(self, side,  qty, price="",order_type="Market",time_in_force=''):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&order_type={order_type}&price={price}&qty={qty}&side={side}&symbol=BTCUSD&time_in_force={time_in_force}&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "timestamp":timestamp,

            "side":side,
            "symbol":"BTCUSD",
            "order_type":order_type,
            "qty":qty,
            "price": price,
            "time_in_force":time_in_force,
            "sign":sign
            }
        r=requests.post(self.url+'/open-api/order/create',data)
        return json.loads(r.text)


    def get_active_order(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/open-api/order/list',data)
        return json.loads(r.text)

    def cancel_active_order(self, order_id):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&order_id={order_id}&symbol=BTCUSD&timestamp={timestamp}"
        sign=str(hmac.new(bytes(self.secret, "utf-8"), bytes(param_str, "utf-8"), digestmod="sha256").hexdigest())
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign,
            "order_id":order_id
            }
        r=requests.post(self.url+'/open-api/order/cancel',data)
        return json.loads(r.text)


    def change_leverage(self, leverage,symbol="BTCUSD"):
        timestamp=int(round(time.time())+1)*1000
        self.leverage=leverage
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":symbol,
            "leverage":self.leverage,
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.post(self.url+'/user/leverage/save',data)
        return json.loads(r.text)

    def my_position(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/position/list',data)
        return json.loads(r.text)




    def ticker(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/v2/public/tickers',data)
        return json.loads(r.text)


    def get_orderbook(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/v2/public/tickers',data)
        return json.loads(r.text)

    def replace_order(self, order_id):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&leverage={self.leverage}&order_id={order_id}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "leverage":self.leverage,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            'order_id': order_id,
            "sign":sign
            }
        r=requests.post(self.url+'/open-api/order/replace',data)
        return json.loads(r.text)

    def get_leverage(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/user/leverage',data)
        return json.loads(r.text)

    def get_wallet_fund_records(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/open-api/wallet/fund/records',data)
        return json.loads(r.text)

    def get_withdraw_records(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/open-api/wallet/withdraw/list',data)
        return json.loads(r.text)

    def get_the_last_funding_rate(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/open-api/funding/prev-funding-rate',data)
        return json.loads(r.text)

    def get_my_last_funding_fee(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/open-api/funding/prev-funding',data)
        return json.loads(r.text)

    def get_predicted_funding_rate_funding_fee(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/open-api/funding/predicted-funding',data)
        return json.loads(r.text)

    def get_trade_records(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/v2/private/execution/list',data)
        return json.loads(r.text)

    def latest_info_btc(self):
        timestamp=int(round(time.time())+1)*1000
        param_str = f"api_key={self.api_key}&symbol=BTCUSD&timestamp={timestamp}"
        sign=self.get_signature(param_str)
        data={
            "api_key":self.api_key,
            "symbol":"BTCUSD",
            "timestamp":timestamp,
            "sign":sign
            }
        r=requests.get(self.url+'/v2/public/tickers',data)
        return json.loads(r.text)

from flask import Flask, request, jsonify
from flask_cors import CORS
from price_fetcher import get_best_price
import requests

app = Flask(__name__)
CORS(app)  # Allow requests from your frontend

HIVE_ENGINE_MARKET_API = "https://api.hive-engine.com/rpc/contracts"

@app.route('/api/price', methods=['POST'])
def price():
    data = request.json
    base = data.get('base', 'PEK').upper()
    quote = data.get('quote', 'SWAP.HIVE').upper()
    price = get_best_price(base, quote)
    if not price:
        return jsonify({'error': f'Could not fetch price for {base}/{quote}'}), 400
    return jsonify({'base': base, 'quote': quote, 'price': price})

@app.route('/api/order', methods=['POST'])
def order():
    data = request.json
    username = data.get('username')
    base = data.get('base', 'PEK').upper()
    quote = data.get('quote', 'SWAP.HIVE').upper()
    amount = str(data.get('amount'))
    price = str(data.get('price'))
    side = data.get('side', 'sell').lower()  # 'buy' or 'sell'
    # For Hive Engine, 'buy' means buying base with quote, 'sell' means selling base for quote
    custom_json = {
        "contractName": "market",
        "contractAction": side,
        "contractPayload": {
            "symbol": base,
            "quantity": amount,
            "price": price
        }
    }
    return jsonify({"custom_json": custom_json})

@app.route('/api/orderbook')
def api_orderbook():
    base = request.args.get('base', 'PEK').upper()
    quote = request.args.get('quote', 'SWAP.HIVE').upper()
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getOrderBook",
        "params": {
            "symbol": f"{base}:{quote}",
            "limit": 50
        }
    }
    try:
        r = requests.post(HIVE_ENGINE_MARKET_API, json=payload, timeout=10)
        data = r.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history')
def api_history():
    base = request.args.get('base', 'PEK').upper()
    quote = request.args.get('quote', 'SWAP.HIVE').upper()
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "find",
        "params": {
            "contract": "market",
            "table": "trades",
            "query": {"symbol": f"{base}:{quote}"},
            "limit": 50,
            "sort": "desc"
        }
    }
    try:
        r = requests.post(HIVE_ENGINE_MARKET_API, json=payload, timeout=10)
        data = r.json()
        return jsonify({'result': data.get('result', [])})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

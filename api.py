from flask import Flask, request, jsonify
from flask_cors import CORS
from price_fetcher import get_best_price
import requests

app = Flask(__name__)
CORS(app)

SUPPORTED_PAIRS = [
    ("PEK", "SWAP.HIVE"),
    ("PEK", "SWAP.BTC"),
    ("PEK", "SWAP.LTC"),
    ("PEK", "SWAP.ETH"),
    ("PEK", "SWAP.DOGE"),
    ("PEK", "SWAP.MATIC"),
    ("PEK", "SWAP.HBD"),
]

HIVE_ENGINE_MARKET_API = "https://api.hive-engine.com/rpc/contracts"

@app.route('/api/pairs')
def api_pairs():
    return jsonify({
        "pairs": [
            {"base": base, "quote": quote} for base, quote in SUPPORTED_PAIRS
        ]
    })

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

@app.route('/api/order', methods=['POST'])
def api_order():
    data = request.json
    username = data.get('username')
    base = data.get('base', 'PEK').upper()
    quote = data.get('quote', 'SWAP.HIVE').upper()
    amount = str(data.get('amount'))
    price = str(data.get('price'))
    side = data.get('side', 'sell').lower()  # 'buy' or 'sell'
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

@app.route('/api/price')
def api_price():
    base = request.args.get('base', 'PEK').upper()
    quote = request.args.get('quote', 'SWAP.HIVE').upper()
    price = get_best_price(base, quote)
    if not price:
        return jsonify({'error': f'Could not fetch price for {base}/{quote}'}), 400
    return jsonify({'base': base, 'quote': quote, 'price': price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

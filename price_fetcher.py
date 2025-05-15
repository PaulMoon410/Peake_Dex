import requests

HIVE_ENGINE_API = "https://api.hive-engine.com/rpc/contracts"
NECTAR_ENGINE_API = "https://api.nectar.engine/market/ticker"  # Example, update if needed

# Fetch price from Hive Engine market
# Returns price as string or None

def get_price_hive_engine(base_symbol, quote_symbol):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "find",
        "params": {
            "contract": "market",
            "table": "metrics",
            "query": {"symbol": base_symbol}
        }
    }
    try:
        r = requests.post(HIVE_ENGINE_API, json=payload, timeout=10)
        data = r.json()
        if 'result' in data and data['result']:
            metrics = data['result'][0]
            if quote_symbol == 'SWAP.HIVE':
                return metrics.get('lastPrice')
            # Add more quote logic if needed
        return None
    except Exception as e:
        print(f"Error fetching price from Hive Engine: {e}")
        return None

# Placeholder for Nectar Engine (update endpoint/logic as needed)
def get_price_nectar_engine(base_symbol, quote_symbol):
    try:
        r = requests.get(NECTAR_ENGINE_API, timeout=10)
        data = r.json()
        # Example: data might be a dict of pairs
        pair = f"{base_symbol}_{quote_symbol}"
        if pair in data:
            return data[pair]['last']
        return None
    except Exception as e:
        print(f"Error fetching price from Nectar Engine: {e}")
        return None

# Main function to get price, tries Hive Engine first, then Nectar

def get_best_price(base_symbol, quote_symbol):
    price = get_price_hive_engine(base_symbol, quote_symbol)
    if price:
        return price
    price = get_price_nectar_engine(base_symbol, quote_symbol)
    return price

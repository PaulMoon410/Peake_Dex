# PEK Dex Backend

A Flask-based backend for the PEK DEX trading platform.

## Features

- Trading pair management with account mapping
- Order placement and matching
- SQLite order storage
- FTP backup/restore functionality
- CORS-enabled API for frontend integration
- Background order matching

## Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**
   Set up your Hive account private keys:
   ```bash
   export PEAKECOIN_MATIC_ACTIVE_KEY="your_key_here"
   export PEAKECOIN_BNB_ACTIVE_KEY="your_key_here"
   export PEAKECOIN_ACTIVE_KEY="your_key_here"
   ```

3. **Run the Server**
   ```bash
   python app.py
   ```

The server will start on `http://0.0.0.0:5000`

## API Endpoints

- `GET /api/pairs` - Get supported trading pairs
- `GET /api/orderbook` - Get order book for a pair
- `GET /api/history` - Get trade history for a pair
- `POST /api/order` - Place a new order
- `GET /api/orders` - List orders (optionally by username)
- `POST /api/ftp/config` - Set FTP configuration
- `GET /api/ftp/config` - Get FTP configuration
- `DELETE /api/ftp/config` - Delete FTP configuration
- `POST /api/ftp/upload` - Upload orders to FTP
- `POST /api/ftp/download` - Download orders from FTP
- `POST /api/ftp/erase` - Erase orders on FTP
- `POST /api/ftp/import` - Import orders from FTP to database

## Account Mapping

Different trading pairs use different backend accounts:
- `SWAP.MATIC` pairs → `peakecoin.matic`
- `SWAP.BNB` pairs → `peakecoin.bnb` 
- `SWAP.HBD` pairs → `peakecoin`
- All others → `peakecoin.matic` (default)

## Production Deployment

For production on your server (74.208.146.37):

1. Upload files to your server
2. Set up virtual environment
3. Configure firewall to allow port 5000
4. Set environment variables for private keys
5. Run with a process manager like systemd or pm2

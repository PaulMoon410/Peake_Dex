# PEK DEX - Decentralized Exchange

A full-stack decentralized exchange (DEX) for trading PEK tokens on the Hive blockchain, featuring automated order matching, multi-token support, and seamless Hive Keychain integration.

## 🌟 Features

### Frontend (Static HTML/CSS/JavaScript)
- **Multi-pair Trading**: Support for PEK/SWAP.HIVE, PEK/SWAP.BTC, PEK/SWAP.LTC, PEK/SWAP.ETH, PEK/SWAP.DOGE
- **Real-time Order Book**: Live display of buy/sell orders
- **Trade History**: Complete transaction history with timestamps
- **Hive Keychain Integration**: Secure transaction signing
- **Responsive Design**: Mobile-friendly interface
- **CORS Proxy Support**: Cross-origin request handling for HTTPS deployment

### Backend (Python Flask)
- **RESTful API**: Clean API endpoints for all trading operations
- **Automated Order Matching**: Background process for executing trades
- **Multi-account Management**: Separate Hive accounts per quote asset
- **Database Integration**: SQLite for order storage and history
- **FTP Backup**: Automatic database backup to external server
- **Hive Blockchain Integration**: Direct interaction via Beem library
- **CORS Enabled**: Cross-origin support for frontend deployment

## 🏗️ Architecture

```
PEK DEX/
├── frontend/          # Static frontend for Geocities hosting
│   ├── index.html     # Main trading pairs page
│   ├── config.js      # API configuration
│   ├── pairs/
│   │   └── pair.html  # Individual trading pair interface
│   └── README.md      # Frontend deployment guide
│
├── backend/           # Python Flask API server
│   ├── app.py         # Main application with all endpoints
│   ├── requirements.txt # Python dependencies
│   ├── deploy.sh      # Production deployment script
│   ├── deploy-simple.sh # Simple deployment script
│   ├── peake-dex.service # Systemd service configuration
│   └── README.md      # Backend setup guide
│
├── README.md          # This file
└── LICENSE            # MIT License
```

## 🚀 Quick Start

### Frontend Deployment (Geocities)
1. Upload all files from `frontend/` to your Geocities account
2. Set `index.html` as your main page
3. Update `config.js` with your backend server URL
4. Access via `https://geocities.ws/yourusername/`

### Backend Deployment (Linux Server)
1. Clone repository to your server
2. Install Python dependencies: `pip install -r backend/requirements.txt`
3. Configure Hive private keys in environment variables
4. Run: `python backend/app.py`
5. Open firewall port: `sudo ufw allow 8080`

## 📡 API Endpoints

### Public Endpoints
- `GET /api/pairs` - Available trading pairs
- `GET /api/orderbook?base=PEK&quote=SWAP.HIVE` - Order book data
- `GET /api/history?base=PEK&quote=SWAP.HIVE` - Trade history

### Trading Endpoints  
- `POST /api/order` - Place new order (requires Hive Keychain)

## 🔐 Security Features

- **No Private Key Storage**: Uses Hive Keychain for transaction signing
- **Account Validation**: Verifies Hive account existence before orders
- **CORS Protection**: Configurable cross-origin policies
- **Input Validation**: Sanitized user inputs and parameters
- **Error Handling**: Comprehensive error responses

## 🛠️ Technology Stack

### Frontend
- **HTML5/CSS3/JavaScript** - Pure vanilla implementation
- **Fetch API** - Modern HTTP requests
- **Hive Keychain** - Blockchain transaction signing
- **CORS Proxies** - Cross-origin request handling

### Backend
- **Python 3.9+** - Core runtime
- **Flask** - Web framework
- **Beem** - Hive blockchain library
- **SQLite** - Local database
- **Threading** - Background order matching
- **FTP** - Remote backup functionality

## 🌐 Deployment Options

### Option 1: Split Deployment (Recommended)
- **Frontend**: Geocities (free static hosting)
- **Backend**: VPS/Dedicated server (Linux recommended)
- **Benefits**: Cost-effective, scalable, reliable

### Option 2: Single Server
- **Both**: Same Linux server with nginx
- **Benefits**: Simplified management, no CORS issues

### Option 3: Development
- **Both**: Local development environment
- **Benefits**: Fast testing, no deployment overhead

## 📋 Requirements

### Frontend Requirements
- Modern web browser with JavaScript enabled
- Hive Keychain browser extension
- HTTPS/HTTP compatible hosting

### Backend Requirements
- Python 3.9 or higher
- Linux/Windows server with internet access
- Hive blockchain account with active key access
- 50MB+ storage space for database
- Network connectivity on port 8080

## 🔧 Configuration

### Environment Variables (Backend)
```bash
export PEK_SWAP_HIVE_KEY="your_private_active_key"
export PEK_SWAP_BTC_KEY="your_private_active_key"
export PEK_SWAP_LTC_KEY="your_private_active_key"
export PEK_SWAP_ETH_KEY="your_private_active_key"
export PEK_SWAP_DOGE_KEY="your_private_active_key"
```

### Frontend Configuration
```javascript
// frontend/config.js
const CONFIG = {
    API_BASE_URL: 'http://your-server-ip:8080'
};
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Support

For issues and questions:
- Check existing issues in the repository
- Create a new issue with detailed description
- Include error logs and configuration details

## 🚨 Disclaimer

This software is provided "as is" without warranty. Users are responsible for:
- Securing their private keys and accounts
- Testing thoroughly before production use
- Complying with local financial regulations
- Understanding blockchain transaction risks

## 🏆 Acknowledgments

- **Hive Blockchain** - Underlying blockchain infrastructure
- **Beem Library** - Python Hive blockchain interface
- **Geocities** - Free static hosting platform
- **Flask Community** - Web framework and ecosystem

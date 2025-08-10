# PEK Dex Frontend

A static HTML/CSS/JavaScript frontend for the PEK DEX trading platform.

## Features

- Trading pair selection
- Order placement interface
- Real-time order book display
- Trade history viewing
- Hive Keychain integration
- Responsive design

## Configuration

Update the API endpoint in `config.js`:

```javascript
const CONFIG = {
    API_BASE_URL: 'http://74.208.146.37:8080',  // Your backend server
};
```

## Files

- `index.html` - Main page with trading pair list
- `pairs/pair.html` - Individual trading pair page
- `config.js` - Configuration file for API endpoints

## Deployment to Geocities

1. **Upload Files**: Upload all files in this folder to your Geocities account
2. **Set Main Page**: Make sure `index.html` is your main page
3. **Update Config**: Ensure `config.js` points to your backend server
4. **Test**: Verify the frontend can connect to your backend API

## File Structure for Geocities

```
your-geocities-site/
├── index.html          (main page)
├── config.js           (API configuration)
└── pairs/
    └── pair.html       (trading pair page)
```

## Backend Requirements

The frontend expects these API endpoints from your backend:

- `GET /api/pairs` - Trading pairs list
- `GET /api/orderbook?base=X&quote=Y` - Order book data
- `GET /api/history?base=X&quote=Y` - Trade history
- `POST /api/order` - Place new order

## Browser Requirements

- Modern browser with JavaScript enabled
- Hive Keychain extension for order placement
- CORS-enabled backend (already configured)

#!/bin/bash

# Quick fix deployment script for PEK Dex Backend
# Run this on your server (74.208.146.37)

echo "Setting up PEK Dex Backend..."

# Install dependencies in current directory (no venv for now)
pip3 install flask flask-cors requests

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set your environment variables:"
echo "   export PEAKECOIN_MATIC_ACTIVE_KEY='your_key'"
echo "   export PEAKECOIN_BNB_ACTIVE_KEY='your_key'"
echo "   export PEAKECOIN_ACTIVE_KEY='your_key'"
echo ""
echo "2. Run the application:"
echo "   python3 app.py"
echo ""
echo "3. Configure firewall:"
echo "   sudo ufw allow 5000"

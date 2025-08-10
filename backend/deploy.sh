#!/bin/bash

# Production deployment script for PEK Dex Backend
# Run this on your server (74.208.146.37)

echo "Setting up PEK Dex Backend..."

# Update system
sudo apt update
sudo apt install -y python3 python3-pip python3-venv

# Create application directory
mkdir -p ~/peake-dex-backend
cd ~/peake-dex-backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Set your environment variables:"
echo "   export PEAKECOIN_MATIC_ACTIVE_KEY='your_key'"
echo "   export PEAKECOIN_BNB_ACTIVE_KEY='your_key'"
echo "   export PEAKECOIN_ACTIVE_KEY='your_key'"
echo ""
echo "2. Run the application:"
echo "   python app.py"
echo ""
echo "3. Configure firewall:"
echo "   sudo ufw allow 5000"

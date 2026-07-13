#!/bin/bash

# Test script to run all examples

echo ""
echo "#================================================#"
echo "# CloudPedagogy PPT Export - Example Tests"
echo "#================================================#"
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found!${NC}"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo -e "${GREEN}✅ Python 3 found$(python3 --version)${NC}"
echo ""

# Check dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Run installation test
echo "Running installation test..."
python3 test_installation.py

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Installation test failed${NC}"
    exit 1
fi

echo ""

# Run examples
echo "#================================================#"
echo "# Running Examples"
echo "#================================================#"
echo ""

echo "Running: Grade 7 Biology Unit Example"
echo "-" * 50

cd examples 2>/dev/null || {
    echo -e "${RED}❌ Examples directory not found${NC}"
    exit 1
}

python3 biology_unit_template.py

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Example completed successfully!${NC}"
    echo ""
    echo "Generated files:"
    ls -lh *.pptx 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
    echo ""
else
    echo -e "${RED}❌ Example failed${NC}"
    exit 1
fi

cd ..

echo ""
echo "#================================================#"
echo "# Test Summary"
echo "#================================================#"
echo ""
echo -e "${GREEN}✅ All tests passed!${NC}"
echo ""
echo "Next steps:"
echo "1. Create your own presentation (see QUICKSTART.md)"
echo "2. Integrate with CloudPedagogy (see INTEGRATION.md)"
echo "3. Customize for your needs (see README.md)"
echo ""

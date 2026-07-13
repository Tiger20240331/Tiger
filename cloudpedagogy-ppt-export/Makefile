# Makefile for CloudPedagogy PPT Export Module

.PHONY: install test test-install run-example clean help docs

help:
	@echo "CloudPedagogy PPT Export Module - Commands"
	@echo ""
	@echo "Installation:"
	@echo "  make install       Install dependencies"
	@echo "  make test-install  Test installation"
	@echo ""
	@echo "Examples & Testing:"
	@echo "  make run-example   Run Grade 7 Biology example"
	@echo "  make test          Run all tests"
	@echo ""
	@echo "Development:"
	@echo "  make docs          Generate documentation"
	@echo "  make clean         Remove generated files"
	@echo ""

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	@echo "✅ Installation complete"

test-install:
	@echo "Testing installation..."
	python3 test_installation.py

run-example:
	@echo "Running Grade 7 Biology Unit example..."
	cd examples && python3 biology_unit_template.py
	@echo ""
	@echo "✅ Example completed. Check current directory for .pptx file"

test: test-install run-example
	@echo "✅ All tests passed!"

docs:
	@echo "Documentation files:"
	@echo "  README.md         - Full documentation"
	@echo "  QUICKSTART.md     - Quick start guide"
	@echo "  INSTALLATION.md   - Installation instructions"
	@echo "  INTEGRATION.md    - CloudPedagogy integration"

clean:
	@echo "Cleaning up..."
	rm -f *.pptx
	rm -f examples/*.pptx
	rm -rf __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "✅ Cleanup complete"

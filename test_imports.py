#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Import test script for CANDataConverter
このスクリプトでインポートが正しく動作するかテストします
"""

import sys
import os

print("=" * 50)
print("Import Test for CANDataConverter")
print("=" * 50)
print()

# Current directory
print(f"Current directory: {os.getcwd()}")
print()

# Python version
print(f"Python version: {sys.version}")
print()

# Test standard imports
print("Testing standard library imports...")
try:
    import tkinter as tk
    print("✓ tkinter")
except ImportError as e:
    print(f"✗ tkinter: {e}")

# Test third-party imports
print("\nTesting third-party imports...")
required_packages = [
    'pandas',
    'numpy',
    'scipy',
    'cantools',
    'can',
]

for package in required_packages:
    try:
        __import__(package)
        print(f"✓ {package}")
    except ImportError as e:
        print(f"✗ {package}: {e}")

# Test local imports
print("\nTesting local imports...")
try:
    import CDW
    print("✓ CDW")
except ImportError as e:
    print(f"✗ CDW: {e}")

try:
    from tool import CAN_Extractor
    print("✓ tool.CAN_Extractor")
except ImportError as e:
    print(f"✗ tool.CAN_Extractor: {e}")

try:
    from tool import CDW as tool_CDW
    print("✓ tool.CDW")
except ImportError as e:
    print(f"✗ tool.CDW: {e}")

# Test CAN_Extractor functionality
print("\nTesting CAN_Extractor module...")
try:
    from tool import CAN_Extractor
    # Check if main function exists
    if hasattr(CAN_Extractor, 'main'):
        print("✓ CAN_Extractor.main() exists")
    else:
        print("✗ CAN_Extractor.main() not found")
except Exception as e:
    print(f"✗ CAN_Extractor test failed: {e}")

print()
print("=" * 50)
print("Import test completed!")
print("=" * 50)

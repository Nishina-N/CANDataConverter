#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Dependency analyzer for CANDataConverter
実際に必要な依存関係を分析します
"""

import sys
import importlib
import pkgutil

print("=" * 60)
print("Dependency Analysis for CANDataConverter")
print("=" * 60)
print()

# CANdata2matcsv.pyで使われているimport文を解析
required_modules = {
    # 標準ライブラリ
    'os': 'stdlib',
    'datetime': 'stdlib',
    'tkinter': 'stdlib',
    'math': 'stdlib',
    'time': 'stdlib',
    'csv': 'stdlib',
    'pickle': 'stdlib',
    'sys': 'stdlib',
    'webbrowser': 'stdlib',
    
    # サードパーティ
    'pandas': 'third-party',
    'cantools': 'third-party',
    'scipy': 'third-party',
    'numpy': 'third-party',
    'can': 'third-party',  # python-can
    
    # ローカル
    'CDW': 'local',
    'tool': 'local',
}

print("Required modules:")
print("-" * 60)

installed = []
missing = []

for module, category in required_modules.items():
    try:
        mod = importlib.import_module(module)
        status = "✓ Installed"
        installed.append(module)
        
        # バージョン情報を取得
        version = "unknown"
        if hasattr(mod, '__version__'):
            version = mod.__version__
        
        print(f"{status:15} {module:20} ({category:12}) v{version}")
        
    except ImportError:
        status = "✗ MISSING"
        missing.append(module)
        print(f"{status:15} {module:20} ({category:12})")

print()
print("=" * 60)
print(f"Total required: {len(required_modules)}")
print(f"Installed: {len(installed)}")
print(f"Missing: {len(missing)}")

if missing:
    print()
    print("⚠️  Missing modules:")
    for m in missing:
        print(f"  - {m}")
    print()
    print("Install with: pip install -r requirements.txt")
else:
    print()
    print("✅ All required modules are installed!")

print("=" * 60)
print()

# サイズ推定
print("Estimated package sizes (approximate):")
print("-" * 60)

size_estimates = {
    'pandas': '~50 MB',
    'numpy': '~30 MB',
    'scipy': '~60 MB',
    'cantools': '~5 MB',
    'can': '~10 MB',
    'tkinter': '~5 MB (included in Python)',
}

total_estimated = 0
for module, size in size_estimates.items():
    if module in installed:
        print(f"  {module:20} {size}")

print()
print("Expected total size: ~150-200 MB (compressed with UPX)")
print("=" * 60)

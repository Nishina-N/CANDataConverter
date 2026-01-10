# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['CANdata2matcsv.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ico', 'ico'),
        ('tool', 'tool'),
        ('CDW.py', '.'),
    ],
    hiddenimports=[
        'tool.CAN_Extractor',
        'tool.CDW',
        'CDW',
        'can.io.blf',
        'can.io.asc',
        'can.io',
        'cantools',
        'cantools.database',
        'cantools.database.can',
        'cantools.database.can.database',
        'pandas',
        'numpy',
        'scipy.io',
        'pickle',
        'csv',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CANDataConverter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # UPX圧縮を無効化（これが原因の可能性）
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUIモード
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='ico\\candata2matcsv.ico',
)

# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/python/PyQt/projects/diplom/editing-of-technological-maps/authenticate_window.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/python/PyQt/projects/diplom/editing-of-technological-maps/', '.')],
    hiddenimports=['cryptography', 'psycopg2', 'openpyxl', 'PyQt5', 'python-docx'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='authenticate_window',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='authenticate_window',
)

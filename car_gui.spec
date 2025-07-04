# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['car_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('car_price_model.pkl', '.'), ('car_features.pkl', '.')],
    hiddenimports=['sklearn', 'sklearn.ensemble._forest', 'sklearn.utils._cython_blas', 'sklearn.neighbors._typedefs', 'sklearn.neighbors._ball_tree', 'sklearn.neighbors._distance_metric'],
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
    a.binaries,
    a.datas,
    [],
    name='car_gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

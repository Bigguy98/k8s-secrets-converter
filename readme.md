## How to run

**Create python virtual environment**
```Bash
python -m venv converter
```

**Active python virtual environment**
```Bash
source converter/Scripts/activate
```

```Powershell
.\converter\Scripts\Activate.ps1
```

**Install libraries**
```
pip install -r requirements.txt
```

**`[OPTIONAL]` To create a desktop shortcut for your application**
```
python make_shortcut.py
```

**Package as .exe file**
```
pyinstaller --onefile main.py
```

Update your main.spec file
```
# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py', 'make_shortcut.py'],
    pat
    binaries=[],
    datas=[('converter.ico', '.')],
    hiddenimports=[],
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
    name='K8sSecretConverter',
    debug=False,hex=[],
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

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='K8sSecretConverter',
)
```

Rebuild app
```
pyinstaller main.spec
```

After this step, K8sSecretConverter.exe file will be created at `./dist` folder
You can run K8sSecretConverter.exe file directly. 
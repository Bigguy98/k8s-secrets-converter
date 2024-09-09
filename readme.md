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
pyinstaller main.spec
```
After this step, K8sSecretConverter.exe file will be created at `./dist` folder
You can run K8sSecretConverter.exe file directly. 
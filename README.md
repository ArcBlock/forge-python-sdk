##Forge-python-sdk
Forge-python-sdk is a sdk for [Forge](https://github.com/ArcBlock/forge).

##Installation
```sh
pip install forge-python-sdk
```

##Usage
First get your Forge running on local with [Forge Cli](https://github.com/ArcBlock/forge-js/tree/master/packages/forge-cli)

Then init your ForgeSdk with default config.
```python
from forge import ForgeSdk
sdk = ForgeSdk()
rpc = sdk.rpc
```
Now you can start with simple rpc calls!

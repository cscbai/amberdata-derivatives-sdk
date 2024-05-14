# Amberdata Derivatives SDK

amberdata-derivatives is a Python library to access the [Amberdata Derivatives API](https://docs.amberdata.io/reference/derivatives-information).

---

**Documentation**: https://docs.amberdata.io/reference/derivatives-information

---

## Installation

```bash
pip install git+https://github.com/amberdata/amberdata-derivatives-sdk.git
```

## Integration

```python
from amberdata_derivatives import AmberdataDerivatives

amberdata_client = AmberdataDerivatives(api_key="ENTER YOUR AD API KEY HERE")
amberdata_client.get_term_structure_constant(currency='BTC', exchange='deribit')
```

Rather than hardcoding the API key, it can be stored in an environment file and loaded dynamically at runtime.

```bash
$ cat .env
API_KEY=<Enter your API key here>
```

```python
from amberdata_derivatives import AmberdataDerivatives

from dotenv import load_dotenv
load_dotenv()

amberdata_client = AmberdataDerivatives(api_key=os.getenv("API_KEY"))
amberdata_client.get_term_structure_constant(currency='BTC', exchange='deribit')
```

## Unit tests

```python
python3 -m unittest -v tests/*.py
```

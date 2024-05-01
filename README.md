# amberdata-derivatives

amberdata-derivatives is a Python library to access the [Amberdata Derivatives API](https://docs.amberdata.io/reference/information).

---

**Documentation**: https://docs.amberdata.io/reference/information

---

## Install

```bash
pip install git+https://github.com/amberdata/amberdata-derivatives-sdk.git
```

## Demo

```python
from amberdata_derivatives import AmberdataDerivatives

amberdata_client = AmberdataDerivatives(api_key="ENTER YOUR AD API KEY HERE")
amberdata_client.get_term_structure(currency='BTC', exchange='deribit')
```

# Python bindings for the Resurs Bank E-Commerce Platform Simplified Flow API

The Resurs Bank Python library provides convenient access to the E-Commerce Platform Simplified Flow API from applications written in the Python language. 

## Documentation

See the [API docs](https://test.resurs.com/docs/display/ecom/Simplified+Flow+API).

## Requirements

-  Python 3.6+

## Installation

* Install from source with:

```sh
python setup.py install
```

## Configuring 

```python
import resurs_bank

resurs_bank.client_id = ''
resurs_bank.client_id = ''
resurs_bank.api_url = 'https://test.resurs.com/ecommerce-test/ws/V4/SimplifiedShopFlowService?wsdl'
```

## Usage

```python
import resurs_bank

client = resurs_bank.ApiClient()
resp = client.getPaymentMethods();
```§
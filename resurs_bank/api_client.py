from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from .config import *

class ApiClient:
    client = None
   
    def __init__(self):
        session = Session()
        session.auth = HTTPBasicAuth(client_id, client_secret)
        self.client = Client(api_url, transport=Transport(session=session))

    def getPaymentMethods(self):
        request_data = {
            'language': "fi",
            'customerType':'NATURAL'
        }
        response = self.client.service.getPaymentMethods(**request_data)
        return response

    def bookPayment( self, reqData ):
        print('bookPayment')
        response = self.client.service.bookPayment(**reqData)
        return response

    def bookSignedPayment( self, paymentId):
        paymentId = {
            'paymentId': paymentId
        }
        response = self.client.service.bookSignedPayment(**paymentId)
        return response

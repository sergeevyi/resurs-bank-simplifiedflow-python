import resurs_bank

print("Book payment...")

client = resurs_bank.ApiClient()
customerData = {
    'governmentId': '311280-999J',
    'address': {
        'fullName':  'Test Testsson',
        'firstName': 'Test',
        'lastName':  'Testsson',
        'addressRow1': 'TEST',
        'postalArea': 'Helsinki',
        'postalCode': 25220,
        'country': 'FI'
    },
    'phone': '042-121212',
    'email': 'test@test.com',
    'type': 'NATURAL'
}    

paymentData = {
    'paymentMethodId': "PARTPAYMENT",
    'customerIpAddress':'127.0.0.1',
}    

specLines = {
    'id': 1,
    'artNo': 1,
    'description': 'test',
    'quantity': 1,
    'unitMeasure': 'st',
    'unitAmountWithoutVat': 100,
    'vatPct': 10,
    'totalVatAmount': 10,
    'totalAmount': 110
}

signingData = {
    'successUrl': 'https://localhost:8080/success',
    'failUrl':  'https://localhost:8080/failure'
}

orderData = {
    'specLines': [specLines],
    'totalAmount': 110,
    'totalVatAmount': 10
}

request_data ={
    'paymentData': paymentData,
    'customer': customerData,
    'signing': signingData,
    'orderData':orderData
}    

resp = client.bookPayment(request_data);
print("bookPayment Success: %r" % (resp))

resp = client.bookSignedPayment(resp['paymentId']);
print("bookSignedPayment Success: %r" % (resp))
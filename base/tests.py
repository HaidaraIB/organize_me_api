from django.test import TestCase

# Create your tests here.
import requests
DOMAIN = 'https://haidaraib.pythonanywhere.com'
class AddUserTestCase(TestCase):
    def test_add_user(self):
        requests.post(
            url=f"{DOMAIN}/addUser/",
            data={
                'phone':'11'
            },
        )

class AddBillTestCase(TestCase):
    def test_add_el_bill(self):
        requests.post(
            url=f"{DOMAIN}/addBill/el/",
            data={
                "payment_amount": 10,
                "commission_amount": 10,
                "date": '2010-10-10',
                "provider": 'SyriatelSEP',
                "operation_number": "10",
                "gov": "A",
                "billing_number": "10",
                "invoice_number": "10",
                "subscription_number": "10",
                "user": "1",
            },
        )


    def test_add_wa_bill(self):
        requests.post(
            url=f"{DOMAIN}/addBill/wa/",
            data={
                "payment_amount": 10,
                "commission_amount": 10,
                "date": '2010-10-10',
                "provider": 'SyriatelSEP',
                "operation_number": "10",
                "gov": "A",
                "receipt_number": "10",
                "barcode_number": "10",
                "counter_number": "10",
                "user": "1",
            },
        )
    
    def test_add_tel_bill(self):
        requests.post(
            url=f"{DOMAIN}/addBill/tel/",
            data={
                "payment_amount": 10,
                "commission_amount": 10,
                "date": '2010-10-10',
                "provider": 'SyriatelSEP',
                "operation_number": "10",
                "phone_number_email": "10",
                "invoice_number": "10",
                "subscription_number": "10",
                "user": "1",
            },
        )


class GetBillsTestCase(TestCase):
    def test_get_el_bills(self):
        requests.get(
            url=f"{DOMAIN}/getBills/el/19/",
        )

        requests.get(
            url=f"{DOMAIN}/getBills/el/1/",
        )

    def test_get_wa_bills(self):
        requests.get(
            url=f"{DOMAIN}/getBills/wa/19/",
        )

        requests.get(
            url=f"{DOMAIN}/getBills/wa/1/",
        )

    def test_get_tel_bills(self):
        requests.get(
            url=f"{DOMAIN}/getBills/tel/19/",
        )

        requests.get(
            url=f"{DOMAIN}/getBills/tel/1/",
        )

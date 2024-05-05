from django.test import TestCase

# Create your tests here.
import requests

# DOMAIN = "http://127.0.0.1:8000/"
DOMAIN = "https://haidaraib.pythonanywhere.com"


class AddUserTestCase(TestCase):
    def test_add_user(self):
        r = requests.post(
            url=f"{DOMAIN}/addUser/",
            data={
                "email": "test@gmail.com",
                "password": "12345",
                "username": "test",
            },
        )
        print(f'AddUserTestCase {r.status_code}')


class LoginTestCase(TestCase):
    def test_login(self):
        r = requests.post(
            url=f"{DOMAIN}/login/",
            data={
                "email": "test@gmail.com",
                "password": "12345",
            },
        )
        print(f"LoginTestCase {r.status_code}")


class AddBillTestCase(TestCase):
    def test_add_el_bill(self):
        r = requests.post(
            url=f"{DOMAIN}/addBill/el/",
            data={
                "payment_amount": 10,
                "commission_amount": 10,
                "date": "2010-10-10",
                "time": "11:11",
                "provider": "SyriatelSEP",
                "operation_number": "10",
                "gov": "A",
                "billing_number": "10",
                "invoice_number": "10",
                "subscription_number": "10",
                "user": "1",
            },
        )
        print(f'AddBillTestCase el {r.status_code}')

    def test_add_wa_bill(self):
        r = requests.post(
            url=f"{DOMAIN}/addBill/wa/",
            data={
                "payment_amount": 10,
                "commission_amount": 10,
                "date": "2010-10-10",
                "time": "11:11",
                "provider": "SyriatelSEP",
                "operation_number": "10",
                "gov": "A",
                "receipt_number": "10",
                "barcode_number": "10",
                "counter_number": "10",
                "user": "1",
            },
        )
        print(f'AddBillTestCase wa {r.status_code}')

    def test_add_tel_bill(self):
        r = requests.post(
            url=f"{DOMAIN}/addBill/tel/",
            data={
                "payment_amount": 10,
                "commission_amount": 10,
                "date": "2010-10-10",
                "time": "11:11",
                "provider": "SyriatelSEP",
                "operation_number": "10",
                "phone_number_email": "10",
                "invoice_number": "10",
                "user": "1",
            },
        )
        print(f'AddBillTestCase tel {r.status_code}')


class AddBillsTestCase(TestCase):
    def test_add_tel_bills(self):
        r = requests.post(
            url=f"{DOMAIN}/addBills/tel/",
            json=[
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "phone_number_email": "10",
                    "invoice_number": "10",
                    "user": "1",
                },
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "phone_number_email": "10",
                    "invoice_number": "10",
                    "user": "1",
                },
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "phone_number_email": "10",
                    "invoice_number": "10",
                    "user": "1",
                },
            ],
        )
        print(f'AddBillsTestCase tel {r.status_code}')

    def test_add_wa_bills(self):
        r = requests.post(
            url=f"{DOMAIN}/addBills/wa/",
            json=[
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "gov": "A",
                    "receipt_number": "10",
                    "barcode_number": "10",
                    "counter_number": "10",
                    "user": "1",
                },
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "gov": "A",
                    "receipt_number": "10",
                    "barcode_number": "10",
                    "counter_number": "10",
                    "user": "1",
                },
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "gov": "A",
                    "receipt_number": "10",
                    "barcode_number": "10",
                    "counter_number": "10",
                    "user": "1",
                },
            ],
        )
        print(f'AddBillsTestCase wa {r.status_code}')

    def test_add_el_bills(self):
        r = requests.post(
            url=f"{DOMAIN}/addBills/el/",
            json=[
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "gov": "A",
                    "billing_number": "10",
                    "invoice_number": "10",
                    "subscription_number": "10",
                    "user": "1",
                },
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "gov": "A",
                    "billing_number": "10",
                    "invoice_number": "10",
                    "subscription_number": "10",
                    "user": "1",
                },
                {
                    "payment_amount": 10,
                    "commission_amount": 10,
                    "date": "2010-10-10",
                    "time": "11:11",
                    "provider": "SyriatelSEP",
                    "operation_number": "10",
                    "gov": "A",
                    "billing_number": "10",
                    "invoice_number": "10",
                    "subscription_number": "10",
                    "user": "1",
                },
            ],
        )
        print(f'AddBillsTestCase el {r.status_code}')


class GetBillsTestCase(TestCase):
    def test_get_el_bills(self):
        r = requests.get(
            url=f"{DOMAIN}/getBills/el/19/",
        )
        print(f'GetBillsTestCase el {r.status_code}')

        r = requests.get(
            url=f"{DOMAIN}/getBills/el/1/",
        )
        print(f'GetBillsTestCase el {r.status_code}')

    def test_get_wa_bills(self):
        r = requests.get(
            url=f"{DOMAIN}/getBills/wa/19/",
        )
        print(f'GetBillsTestCase wa {r.status_code}')

        r = requests.get(
            url=f"{DOMAIN}/getBills/wa/1/",
        )
        print(f'GetBillsTestCase wa {r.status_code}')

    def test_get_tel_bills(self):
        r = requests.get(
            url=f"{DOMAIN}/getBills/tel/19/",
        )
        print(f'GetBillsTestCase tel {r.status_code}')

        r = requests.get(
            url=f"{DOMAIN}/getBills/tel/1/",
        )
        print(f'GetBillsTestCase tel {r.status_code}')

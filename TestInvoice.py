# Chris Donohue - 801030506
import math

import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_CanAddProduct(invoice):
       qnt = 5
       price = 2
       discount = 5
       invoice.addProduct(qnt,price,discount)
       assert invoice.items['qnt'] == 5
       assert invoice.items['unit_price'] == 2
       assert invoice.items['discount'] == 5

def test_inputNumber(invoice):
   assert invoice.inputNumber('Enter something')
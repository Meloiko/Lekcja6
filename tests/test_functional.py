import pytest
from src.manager import Manager
from src.models import Parameters

def test_total_due_integrity():

    manager = Manager(Parameters())

    apartment_key = "apart-polanka"
    year = 2024
    month = 1

    settlement = manager.get_settlement(apartment_key, year, month)

    tenant_settlements = manager.create_tenants_settlements(settlement)
    total_tenants_sum = sum(ts.total_due_pln for ts in tenant_settlements)

    assert round(total_tenants_sum, 2) == round(settlement.total_due_pln, 2)

def test_tax_calculation():
    manager = Manager(Parameters())
    
    tax = manager.get_tax(2024, 1, 0.085)

    assert isinstance(tax, int)

def test_missing_bills_detection():
    manager = Manager(Parameters())
    missing = manager.find_apartments_without_bills(2024, 1)

    assert isinstance(missing, list)
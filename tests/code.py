import pytest
from src import masks, processing, widget


@pytest.mark.parametrize("card_or_account_info,expected", [("Maestro 1596837868705199", 'Maestro 1596 83** **** 5199'),
                                                           ("Visa Classic 6831982476737658",
                                                            'Visa Classic 6831 98** **** 7658'),
                                                           ("Счет 73654108430135874305", 'Счет **4305'),
                                                           ('Maestro 159683786870519', 'Error')])
def test_mask_account_card(card_or_account_info, expected):
    assert widget.mask_account_card(card_or_account_info) == expected


@pytest.mark.parametrize("numbers_info,expected", [("1596837868705199", '1596 83** **** 5199'),
                                                   ("6831982476737658", '6831 98** **** 7658'),
                                                   ('897304958f7290kj', 'Error'),
                                                   ('394075', 'Error')])
def test_mask_card_number(numbers_info, expected):
    assert masks.get_mask_card_number(numbers_info) == expected


@pytest.mark.parametrize('date,expected', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                           ('2025-02-10T02:26:18.671407', '10.02.2025'),
                                           ('200-03-11T02:26:18.671407', 'Error')])
def test_get_date(date, expected):
    assert widget.get_date(date) == expected


@pytest.mark.parametrize('numbers,expected', [('73654108430135874305', '**4305'),
                                              ('19861059860492865092', '**5092'),
                                              ('saigq54298dfgjkh895h', 'Error'),
                                              ('23576908536', 'Error')])
def test_get_mask_account(numbers, expected):
    assert masks.get_mask_account(numbers) == expected

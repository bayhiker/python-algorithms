from .lc0121_stock import get_profit_recursive,get_profit_dp_bottom_up

def test_stock_recursive():
    assert get_profit_recursive([7,1,5,3,6,4])[0] == 5
    assert get_profit_recursive([7,6,4,3,1])[0] == 0
    assert get_profit_dp_bottom_up([7,1,5,3,6,4]) == 5
    assert get_profit_dp_bottom_up([7,6,4,3,1]) == 0

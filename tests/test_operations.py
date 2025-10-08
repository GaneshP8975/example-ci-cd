from src.math_operation import add,sub,mul,div

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert sub(5,3)==2

def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1

def test_mul():
    assert mul(2,3)==6
    assert mul(5,1)==5
    assert mul(5,3)==15

def test_div():
    assert div(24,8)==3
    assert div(35,7)==5
    assert div(56,7)==8
import pytest

# fixture参数scope="module"，module作用是整个.py文件都会生效，用例调用时，参数写上函数名称就行
@pytest.fixture(scope='module')
def open():
    pass

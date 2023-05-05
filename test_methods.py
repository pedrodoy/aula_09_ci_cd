import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sum():
    value1 = 4
    value2 = 7

    output = methods.soma(value1, value2)

    assert output == 10

def test_mult():
    value1 = 1
    value2 = 8

    output = methods.multiplicacao(value1, value2)

    assert output == 15

def test_div():
    value1 = 9
    value2 = 3

    output = methods.divisao(value1, value2)

    assert output == 2

def test_sub():
    value1 = 4
    value2 = 7

    output = methods.subtracao(value1, value2)

    assert output == 2
#egg

def egg():
    x = 63
    while (x%8 != 1 or x%6 != 3 or x%5 != 4 or x%4 != 1):
        x = x + 63
    print(x)
        
egg()
    
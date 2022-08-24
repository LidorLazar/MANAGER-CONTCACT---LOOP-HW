def bizbuz_for_loop():
    for i in range(100):
        if (i % 15 == 0):
            print('bizzbuz')
        elif (i % 5 == 0):
            print('bizz')
        elif (i % 3 == 0):
            print('buz')
        else:
            print(i)
bizbuz_for_loop()

def bizbuz_while_loop():
    i = 0 
    while i <= 100:
        if (i % 15 == 0):
            print('bizzbuz')
        elif (i % 5 == 0):
            print('bizz')
        elif (i % 3 == 0):
            print('buz')
        else:
            print(i)
bizbuz_while_loop()


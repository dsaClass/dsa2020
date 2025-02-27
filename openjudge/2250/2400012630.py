while True :
    try :
        print('{0:b}'.format(int(input())))
    except EOFError :
        break
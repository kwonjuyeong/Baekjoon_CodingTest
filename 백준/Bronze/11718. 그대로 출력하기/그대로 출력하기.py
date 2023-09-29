while True:
    try:
        things = input()
        if not things:
            break
        print(things)
    except EOFError:
        break    
    
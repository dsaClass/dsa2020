def search(s) :
    for item in s :
        if s.count(item)==1 :
            print(item)
            return
    print("no")
    return

s=input()
search(s)
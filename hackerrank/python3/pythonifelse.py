if __name__ == '__main__':
    n = int(input())
    r = range(1,5)
    t = range(6,20)
    
    if n % 2 == 1:
        print("Weird")
    elif n in r:
        print("Not Weird")
    elif n in t:
        print("Weird")
    elif n > 20:
        print("Not Weird")

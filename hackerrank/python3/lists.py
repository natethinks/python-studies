if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        user_input = input().split()
        print(user_input)
        if user_input[0] != 'print':
            cmd = user_input[0]
            args = user_input[1:]
            cmd += "(" + ",".join(args) + ")"
            eval("l."+cmd)
        else:
            print(l)

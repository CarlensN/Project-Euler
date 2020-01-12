borneSup = 20
def check_div(n):
    for i in range(1, borneSup+1):
        if n % i == 0:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    num = 10
    while not check_div(num):
        num+=10
    print(num)

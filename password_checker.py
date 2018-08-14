def main():
    MIN_LENGTH = 6
    password = get_password(MIN_LENGTH)
    print('*' * len(password))

def get_password(MIN_LENGTH):
    password = input("enter password, it must be {} character long".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("enter password, it must be {} character long".format(MIN_LENGTH))
    return(password)


main()



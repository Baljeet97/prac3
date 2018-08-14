def main():
    MIN_LENGTH = 6
password = str(input("enter password, it must be {} character long".format(MIN_LENGTH)))
while len(password) < MIN_LENGTH:
    password = str(input("enter password, it must be {} character long".format(MIN_LENGTH)))

print('*' * len(password))
main()
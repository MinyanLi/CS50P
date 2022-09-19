import validators

def main():
    e = email_validator(input("What's your email address? ").strip())
    if e == True:
        print("Valid")
    else:
        print("Invalid")


def email_validator(s):
    if validators.email(s):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
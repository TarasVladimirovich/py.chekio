# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    if len(password) > 9:
        return True
    print(len(password) > 6 )
    return len(password) > 6 and any(char.isdigit() for char in password) and not password.isdigit()


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short54'))


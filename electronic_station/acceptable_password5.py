def is_acceptable_password(password: str) -> bool:
    if len(set(list(password))) <= 3:
        return False
    if password.lower().find('password') != -1:
        return False
    if len(password) > 9:
        return True
    return len(password) > 6 and any(char.isdigit() for char in password) and not password.isdigit()


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('password12345'))


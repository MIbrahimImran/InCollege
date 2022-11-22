
def is_password_valid(password):
    special_characters = "!@#$%^&*()_+{}|:<>?[]\;',./`~"
    if len(password) < 8 or len(password) > 12:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char in special_characters for char in password):
        return False
    return True

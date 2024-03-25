MIN_PASSWORD_LENGTH = 8
PASSWORD_COMPLEXITY_ERROR = 'Password setidaknya {} karakter dan mengandung setidaknya satu huruf besar, satu huruf kecil, dan satu angka atau spesial karakter'.format(MIN_PASSWORD_LENGTH)

def validate_password(password):
    # Check if the password meets the requirements
    if len(password) < MIN_PASSWORD_LENGTH:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() or not char.isalnum() for char in password):
        return False
    return True
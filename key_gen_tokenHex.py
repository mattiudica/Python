import string
import secrets
alphabet = string.ascii_letters + string.digits
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break

print(secrets.token_hex(7))
# print("Generate a secure token using a secrets", (secrets.token_hex(16)[0:lengthString]))

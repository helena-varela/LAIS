import random
import string

senha = "".join(random.choices(string.ascii_letters + string.digits, k=8))

print(senha)

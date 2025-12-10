import random
import string


def randomString():
    source_str = string.ascii_letters + string.digits
    pwd = ''.join(random.choice(source_str) for _ in range(20))
    return pwd


print(randomString())
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [
    {"name" : random_string("name", 5),
    "job" : random_string("job", 5)},

    {"name" : " ",
     "job" : random_string("job", 5)},

    {"name" : random_string("name", 5),
     "job" : " "}
]


table = [None] * 8


def hashf(s):
    b = s.encode()

    total = 0

    for i in b:
        total += 1

    return total


def get_index(key):
    index_value = hashf(key)
    index_value %= len(table)

    return index_value
    print(hash_value)


def put(key, value):
    index = get_index(key)

    table[index] = value


def get(key):
    pass


def delete(key):
    pass


put('neej', 3490)

print(hashf('beej'))
print(table)
# return hash_value

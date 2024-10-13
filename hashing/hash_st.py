def hash_str(key):
    hashed_value = 0
    for i in key:
        hashed_value+=hash(i)
    return hashed_value
print(ord('A'))
print(hash_str("arjun"))
print(hash("Arjun"))


tuple_data = (1, 2, 3)
hashed_tuple = hash(tuple_data)
print(f"Hash of the tuple {tuple_data}: {hashed_tuple}")

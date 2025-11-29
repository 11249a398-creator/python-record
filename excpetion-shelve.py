try:
    with shelve.open('my_data.db', 'r') as shelf:
        print(f"Is Student (after deletion): {shelf['is_student']}")
except KeyError:
    print("'is_student' variable not found after deletion.")


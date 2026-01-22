def find_duplicate(numbers):
    """Finds and returns a list of duplicate numbers from the input list."""
    seen = set()
    duplicates = set()
    
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    
    return list(duplicates)

example_list = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8, 1]
print("Duplicate numbers:", find_duplicate(example_list))
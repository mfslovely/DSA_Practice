# Rule one: alwayes calculate  time complexity in worst case scenario.
# Rule two: ignore constant time complexity.
# Rule three: avoid lower bound


# rule 1:

age = 10

if age >= 80:
    print("You are old")
elif age >= 60:
    print("You are senior citizen")
elif age >= 18:
    print("You are adult")
else:
    print("You are minor")

# best case is 2 opertions
# worst case is 4 opertions

# rule 2: avoid constant time complexity
for i in range(100):
    print(i)
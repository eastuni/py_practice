for ele in 10, 9, 7, 5, 6:
    print(ele)

print("\n===")
data = 'korea', 'japan', 'china'
for ele in data:
    print(ele)

print("\n===")
for ele in range(5):
    print(ele, end = ' ')

print("\n===")

for ele in range(3, 9, 2):
    print(ele, end = ' ')

print("\n===")
for ele in range(10, 2 , -1):
    print(ele, end = ' ')

for outer in range(4):
    print("outer",outer)
    for inner in range(5,9):
        print(">>inner:",inner)


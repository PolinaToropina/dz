# a = 2
# b = 5
#
# c = b
#
# print("Start app")
#
# d = c - a
#
# div = a / d
#
# print(f"{div}")

# a = 5
# b = 2
# sum1 = a + b
# print(f"{sum1}")
#
# c = 3
# d = 5
# sum2 = c + d
# print(f"{sum2}")

# def sumInt(a, b):
#     print("sum of Int values: ")
#
#     sum = a + b
#     print(sum)
#
# sumInt(2, 3)

def divInt(a : int, b : int) -> int:
    if b == 0:
        print(f"divive by {b} not possible")
        return 0

    return int(a / b)

#=============CLIENT CODE=============#

value1 = float(input('enter value1 -> '))
value2 = float(input('enter value2 -> '))

sum = divInt(value1, value2);

print(f"sum of Int values: {sum}")



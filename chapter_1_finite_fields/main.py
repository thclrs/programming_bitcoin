# from ecc import FieldElement
#
# a = FieldElement(7,13)
# b = FieldElement(11,13)
# print(a-b)

# # EXERCISE 4
# prime = 97
# print((95 * 45 * 31) % prime)
# print((17 * 13 * 19 * 44) % prime)
# print((pow(12, 7) * pow(77, 49)) % prime)
#
# # EXERCISE 5
# prime = 19
# for k in [1, 3, 7, 13, 18]:
# # for k in range(2,3):
#     print([k * i % prime for i in range(prime)])
#     print(sorted([k * i % prime for i in range(prime)]))
#
# # exercise 8
# prime = 31
# print(3 * pow(24, prime - 2, prime) % prime)
# print(pow(17, 3 * (prime - 2), prime))
# print(11 * pow(4, 4 * (prime - 2)) % prime)

# exercise 9
from ecc import FieldElement

a = FieldElement(3, 31)
b = FieldElement(24, 31)
print(a/b)

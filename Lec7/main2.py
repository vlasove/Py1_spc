"""
D3: M solution
"""
n = int(input())
# 2 -> (-2, -1, 0, 1, 2)
# 3 -> (-3, -2, -1, 0, 1, 2, 3)
for i in range(-n, n + 1 ,1):
    print("Квадрат числа", i, "равен", i**2)
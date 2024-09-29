# Compare the largest and smallest numbers without if,else and min max and >,<,== 
print("so sánh số lớn nhất và nhỏ nhất:")
a = int(input("nhập vào số thứ nhất: "))
b = int(input("nhập vào số thứ hai: "))
# Tính toán
result = ( a+b + abs(b - a)) / 2
# In kết quả
print(f" Số lớn nhất là : {result}")

# # Compare the largest and smallest numbers without if,else and min max and >,<,== 
# print("so sánh số lớn nhất và nhỏ nhất:")
# a = int(input("nhập vào số thứ nhất: "))
# b = int(input("nhập vào số thứ hai: "))
# # Tính toán
# result = ( a+b + abs(b - a)) / 2
# # In kết quả
# print(f" Số lớn nhất là : {result}")

# DO MAT KHAU
## Người dùng nhập mật khẩu bí mật của họ
user_password = int(input("Hãy nhập mật khẩu bất kỳ: "))

# Bắt đầu dò từ 0
attempt = 0

while True:
    print(f"Đang dò: {attempt}")
    
    # Kiểm tra nếu mật khẩu hiện tại khớp với mật khẩu của người dùng
    if attempt == user_password:
        print(f"Đã tìm thấy mật khẩu! Mật khẩu là: {attempt}")
        break
    attempt += 1  # Tăng mật khẩu dò lên 1 để tiếp tục thử


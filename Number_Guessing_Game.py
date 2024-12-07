import random

PASSWORD = "12345"

def login():
    return any(input(f"Nhập mật khẩu (còn {3 - i} lần): ") == PASSWORD for i in range(3)) or print("Truy cập bị từ chối.")

def calculator():
    ops = {'1': ('+', lambda a, b: a + b), 
           '2': ('-', lambda a, b: a - b), 
           '3': ('*', lambda a, b: a * b), 
           '4': ('/', lambda a, b: a / b if b else "Lỗi chia 0")}
    choice = input("Chọn phép toán (1:+, 2:-, 3:*, 4:/): ")
    if choice in ops:
        try:
            a, b = map(float, input("Nhập hai số cách nhau khoảng trắng: ").split())
            print(f"Kết quả: {a} {ops[choice][0]} {b} = {ops[choice][1](a, b)}")
        except ValueError:
            print("Dữ liệu không hợp lệ.")
    else:
        print("Lựa chọn không hợp lệ.")

def number_guessing_game():
    max_attempts = {'1': 10, '2': 7, '3': 5}.get(input("Chọn độ khó (1: Dễ, 2: TB, 3: Khó): "))
    if not max_attempts: 
        return print("Lựa chọn không hợp lệ.")
    secret = random.randint(1, 100)
    print("Tôi đã chọn số từ 1-100, hãy đoán!")
    for i in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Thử lần {i}: "))
            if guess == secret:
                return print(f"Đúng! Số là {secret}, bạn đoán {i} lần.")
            print("Quá lớn!" if guess > secret else "Quá nhỏ!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
    print(f"Hết lượt! Số là {secret}.")

if __name__ == "__main__":
    if login():
        while (choice := input("\n1: Máy tính, 2: Đoán số, 3: Thoát. Chọn: ")) != '3':
            {'1': calculator, '2': number_guessing_game}.get(choice, lambda: print("Lựa chọn không hợp lệ."))()
        print("Tạm biệt!")

### Sửa đổi:
# 1. **Sửa lỗi phép nhân**: Thêm `'*'` vào từ điển `ops`.
# 2. **Tối ưu xử lý lỗi**:
#    - Bảo đảm kiểm tra lựa chọn phép toán (`choice`) và mức độ khó (`difficulty`) đầy đủ.
#    - Thông báo lỗi ngắn gọn nhưng rõ ràng.
# 3. **Tính năng không đổi**: Mã vẫn ngắn gọn, dễ đọc, và có thể mở rộng thêm tính năng khi cần.
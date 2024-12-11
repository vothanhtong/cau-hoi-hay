import random

PASSWORD = "12345"

# Đăng nhập
def login():
    for attempt in range(3):
        remaining = 2 - attempt
        if input(f"Nhập mật khẩu (còn {remaining + 1} lần): ") == PASSWORD:
            print("Đăng nhập thành công!")
            return True
        print("Sai mật khẩu.")
    print("Truy cập bị từ chối.")
    return False

# Máy tính
def calculator():
    operations = {
        '1': ('+', lambda a, b: a + b),
        '2': ('-', lambda a, b: a - b),
        '3': ('*', lambda a, b: a * b),
        '4': ('/', lambda a, b: a / b if b != 0 else "Lỗi chia 0")
    }
    choice = input("Chọn phép toán (1:+, 2:-, 3:*, 4:/): ")
    if choice in operations:
        try:
            a, b = map(float, input("Nhập hai số cách nhau khoảng trắng: ").split())
            op_symbol, op_func = operations[choice]
            result = op_func(a, b)
            print(f"Kết quả: {a} {op_symbol} {b} = {result}")
        except ValueError:
            print("Dữ liệu không hợp lệ. Vui lòng nhập lại.")
    else:
        print("Lựa chọn không hợp lệ.")

# Trò chơi đoán số
def number_guessing_game():
    difficulty_levels = {
        '1': 10,  # Dễ
        '2': 7,   # Trung bình
        '3': 5    # Khó
    }
    difficulty = input("Chọn độ khó (1: Dễ, 2: TB, 3: Khó): ")
    max_attempts = difficulty_levels.get(difficulty)
    
    if not max_attempts:
        print("Lựa chọn không hợp lệ.")
        return
    
    secret = random.randint(1, 100)
    print("Tôi đã chọn số từ 1-100, hãy đoán!")
    
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Thử lần {attempt}: "))
            if guess == secret:
                print(f"Chúc mừng! Bạn đã đoán đúng số {secret} sau {attempt} lần thử.")
                return
            print("Quá lớn!" if guess > secret else "Quá nhỏ!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    
    print(f"Hết lượt! Số bí mật là {secret}.")

# Chương trình chính
def main():
    print("=== Hệ thống đăng nhập ===")
    if not login():
        return
    
    while True:
        print("\nMenu:")
        print("1: Máy tính")
        print("2: Trò chơi đoán số")
        print("3: Thoát")
        choice = input("Chọn một tùy chọn: ")
        
        actions = {
            '1': calculator,
            '2': number_guessing_game
        }
        if choice == '3':
            print("Tạm biệt!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

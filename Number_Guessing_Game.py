import random

# Định nghĩa mật khẩu
PASSWORD = "12345"

# Hàm đăng nhập
def login():
    attempts = 3  # Số lần nhập sai tối đa
    while attempts > 0:
        password = input("Nhập mật khẩu: ")
        if password == PASSWORD:
            print("Đăng nhập thành công!")
            return True
        else:
            attempts -= 1
            print(f"Mật khẩu không đúng! Bạn còn {attempts} lần thử.")
    print("Đăng nhập thất bại. Truy cập bị từ chối.")
    return False

# 1. Máy tính Cơ bản với Đăng nhập
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Không thể chia cho 0"

# Hàm chính để chạy máy tính
def calculator():
    if not login():
        return  # Kết thúc nếu đăng nhập thất bại
    
    print("Chọn phép toán:")
    print("1 - Cộng")
    print("2 - Trừ")
    print("3 - Nhân")
    print("4 - Chia")
    
    choice = input("Nhập phím (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
            
            if choice == '1':
                print(f"Kết quả: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Kết quả: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Kết quả: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Kết quả: {num1} / {num2} = {divide(num1, num2)}")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
    else:
        print("Vui lòng chọn một phép toán hợp lệ (1, 2, 3 hoặc 4).")

# 2. Game Đoán Số với Đăng nhập
def number_guessing_game():
    if not login():
        return  # Kết thúc nếu đăng nhập thất bại

    best_score = float('inf')  # Điểm cao nhất

    while True:
        print("\nChọn mức độ khó:")
        print("1. Dễ (10 lần đoán)")
        print("2. Trung bình (7 lần đoán)")
        print("3. Khó (5 lần đoán)")
        difficulty = input("Nhập mức độ (1/2/3): ")
        
        # Xác định số lượt đoán tối đa dựa trên mức độ khó
        if difficulty == '1':
            max_attempts = 10
        elif difficulty == '2':
            max_attempts = 7
        elif difficulty == '3':
            max_attempts = 5
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
        
        secret_number = random.randint(1, 100)  # Số bí mật từ 1 đến 100
        attempts = 0  # Biến đếm số lần đoán

        print("\nTôi đã chọn một số từ 1 đến 100. Hãy đoán nó nhé!")
        
        while attempts < max_attempts:
            try:
                guess = int(input("Nhập số bạn đoán: "))
                attempts += 1

                if guess < secret_number:
                    print("Số của bạn nhỏ hơn số bí mật. Hãy thử lại!")
                elif guess > secret_number:
                    print("Số của bạn lớn hơn số bí mật. Hãy thử lại!")
                else:
                    print(f"Chúc mừng! Bạn đã đoán đúng số {secret_number} sau {attempts} lần thử.")
                    
                    if attempts < best_score:
                        best_score = attempts
                        print(f"Chúc mừng! Bạn đã đạt kỷ lục mới với {attempts} lần thử.")
                    break

                print(f"Bạn còn {max_attempts - attempts} lần đoán.")
                
            except ValueError:
                print("Vui lòng nhập một số hợp lệ.")
        
        else:
            print(f"Rất tiếc, bạn đã hết lượt đoán. Số bí mật là: {secret_number}")

        print(f"\nĐiểm cao nhất hiện tại: {best_score} lần đoán.")
        
        play_again = input("\nBạn có muốn chơi lại không? (c/k): ")
        if play_again.lower() != 'c':
            print("Cảm ơn bạn đã chơi trò chơi Đoán Số. Hẹn gặp lại!")
            break

# Chạy chương trình máy tính
calculator()

# Chạy trò chơi Đoán Số
number_guessing_game()

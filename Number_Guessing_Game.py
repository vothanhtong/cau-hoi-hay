# - Addition (cộng)
# - Subtraction (trừ)
# - Multiplication (nhân)
# - Division (chia)

# CACH 1 ;
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

def calculator():
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

# Chạy chương trình
calculator()

# CACH 2:
def calculator():
    # Cố định phép toán và các số để chạy thử nghiệm
    choice = 1  # 1: Cộng, 2: Trừ, 3: Nhân, 4: Chia
    num1 = 10
    num2 = 5

    # Thực hiện phép toán dựa trên lựa chọn
    if choice == 1:
        result = num1 + num2
        operation = "Cộng"
    elif choice == 2:
        result = num1 - num2
        operation = "Trừ"
    elif choice == 3:
        result = num1 * num2
        operation = "Nhân"
    elif choice == 4:
        result = num1 / num2
        operation = "Chia"
    else:
        print("Lựa chọn không hợp lệ!")
        return

    # Hiển thị kết quả
    print(f"Kết quả của phép {operation} giữa {num1} và {num2} là: {result}")

# Chạy chương trình
calculator()


#                 Number Guessing Game
import random

def number_guessing_game():
    # Chọn một số ngẫu nhiên trong khoảng 1 đến 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Số lần đoán

    print("Chào mừng bạn đến với trò chơi Đoán Số!")
    print("Tôi đã chọn một số từ 1 đến 100. Hãy cố gắng đoán nó nhé!")

    while True:
        try:
            # Người chơi nhập số đoán
            guess = int(input("Nhập số bạn đoán: "))
            attempts += 1

            if guess < secret_number:
                print("Số của bạn nhỏ hơn số bí mật. Hãy thử lại!")
            elif guess > secret_number:
                print("Số của bạn lớn hơn số bí mật. Hãy thử lại!")
            else:
                print(f"Chúc mừng! Bạn đã đoán đúng số {secret_number} sau {attempts} lần thử.")
                break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

# Chạy trò chơi
number_guessing_game()

# C2:
import random

def number_guessing_game():
    # Điểm cao nhất ban đầu là vô cực (sẽ cập nhật khi có điểm mới)
    best_score = float('inf')

    while True:
        # Chọn mức độ khó
        print("\nChọn mức độ khó:")
        print("1. Dễ (10 lần đoán)")
        print("2. Trung bình (7 lần đoán)")
        print("3. Khó (5 lần đoán)")
        difficulty = input("Nhập mức độ (1/2/3): ")
        
        if difficulty == '1':
            max_attempts = 10
        elif difficulty == '2':
            max_attempts = 7
        elif difficulty == '3':
            max_attempts = 5
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
        
        # Tạo số bí mật và đặt lại số lần đoán
        secret_number = random.randint(1, 100)
        attempts = 0

        print("\nTôi đã chọn một số từ 1 đến 100. Hãy đoán nó nhé!")
        
        while attempts < max_attempts:
            try:
                # Người chơi nhập số đoán
                guess = int(input("Nhập số bạn đoán: "))
                attempts += 1

                if guess < secret_number:
                    print("Số của bạn nhỏ hơn số bí mật. Hãy thử lại!")
                elif guess > secret_number:
                    print("Số của bạn lớn hơn số bí mật. Hãy thử lại!")
                else:
                    print(f"Chúc mừng! Bạn đã đoán đúng số {secret_number} sau {attempts} lần thử.")
                    
                    # Cập nhật điểm cao nhất
                    if attempts < best_score:
                        best_score = attempts
                        print(f"Chúc mừng! Bạn đã đạt kỷ lục mới với {attempts} lần thử.")

                    break

                # Thông báo số lần đoán còn lại
                print(f"Bạn còn {max_attempts - attempts} lần đoán.")
                
            except ValueError:
                print("Vui lòng nhập một số hợp lệ.")
        
        else:
            # Thông báo khi hết lượt đoán
            print(f"Rất tiếc, bạn đã hết lượt đoán. Số bí mật là: {secret_number}")

        # Hiển thị điểm cao nhất
        print(f"\nĐiểm cao nhất hiện tại: {best_score} lần đoán.")
        
        # Hỏi người chơi có muốn chơi lại không
        play_again = input("\nBạn có muốn chơi lại không? (c/k): ")
        if play_again.lower() != 'c':
            print("Cảm ơn bạn đã chơi trò chơi Đoán Số. Hẹn gặp lại!")
            break

# Chạy trò chơi
number_guessing_game()

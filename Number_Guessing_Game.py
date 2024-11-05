## 1. **Máy tính Cơ bản (Basic Calculator)**
### Cách 1: Máy tính yêu cầu người dùng nhập lựa chọn và hai số
# - Mục tiêu: Tạo một máy tính thực hiện các phép toán cơ bản (cộng, trừ, nhân, chia) dựa trên lựa chọn của người dùng.
# - Chức năng chính:
#   - Máy tính có bốn hàm cho các phép toán riêng biệt (`add`, `subtract`, `multiply`, `divide`).
#   - Người dùng nhập lựa chọn cho phép toán và hai số.
#   - Máy tính sẽ thực hiện phép tính và trả về kết quả.

#### Mã nguồn:
# Định nghĩa các hàm tính toán
def add(a, b):       # Hàm cộng
    return a + b

def subtract(a, b):  # Hàm trừ
    return a - b

def multiply(a, b):  # Hàm nhân
    return a * b

def divide(a, b):    # Hàm chia (kiểm tra nếu mẫu bằng 0)
    if b != 0:
        return a / b
    else:
        return "Không thể chia cho 0"

# Hàm chính để chạy máy tính
def calculator():
    print("Chọn phép toán:")
    print("1 - Cộng")
    print("2 - Trừ")
    print("3 - Nhân")
    print("4 - Chia")
    
    choice = input("Nhập phím (1/2/3/4): ")
    
    # Kiểm tra lựa chọn của người dùng
    if choice in ['1', '2', '3', '4']:
        try:
            # Người dùng nhập hai số
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
            
            # Thực hiện phép toán dựa trên lựa chọn
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

# Chạy chương trình máy tính
calculator()

### **Cách 2: Máy tính đơn giản với giá trị cố định**
# - Mục tiêu: Thực hiện phép tính với các giá trị và phép toán cố định, không cần tương tác từ người dùng.
# - Cách hoạt động: 
#   - Dùng sẵn các giá trị (`num1 = 10`, `num2 = 5`) và lựa chọn phép toán (`choice = 1`).
#   - Hiển thị kết quả của phép tính dựa trên giá trị cố định.

#### Mã nguồn:
def calculator():
    choice = 1   # Cố định phép toán (1: cộng, 2: trừ, 3: nhân, 4: chia)
    num1 = 10
    num2 = 5

    # Thực hiện phép toán và hiển thị kết quả
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
        retur
    print(f"Kết quả của phép {operation} giữa {num1} và {num2} là: {result}")

# Chạy chương trình
calculator()

## 2. Game Đoán Số (Number Guessing Game)

### Cách 1: Game Đoán Số Cơ Bản
# - Mục tiêu: Người chơi cố gắng đoán một số ngẫu nhiên trong khoảng từ 1 đến 100.
# - Cách chơi:
#   - Máy sẽ chọn một số ngẫu nhiên từ 1 đến 100.
#   - Người chơi nhập số đoán, máy sẽ trả lời xem số đoán thấp hơn, cao hơn hay đúng với số bí mật.
#   - Nếu đoán đúng, trò chơi kết thúc và hiển thị số lần đoán.
import random

def number_guessing_game():
    # Chọn một số ngẫu nhiên trong khoảng 1 đến 100
    secret_number = random.randint(1, 100)
    attempts = 0  # Số lần đoán

    print("Chào mừng bạn đến với trò chơi Đoán Số!")
    print("Tôi đã chọn một số từ 1 đến 100. Hãy cố gắng đoán nó nhé!")

    while True:
        try:
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
### Cách 2: Game Đoán Số với Mức Độ Khó và Điểm Cao Nhất**
# - Mục tiêu: Người chơi chọn mức độ khó (Dễ, Trung bình, Khó) với số lần đoán khác nhau, và điểm cao nhất được lưu lại.
# - Cách chơi:
#   - Người chơi chọn mức độ khó:
#     - Dễ: 10 lần đoán.
#     - Trung bình: 7 lần đoán.
#     - Khó: 5 lần đoán.
#   - Sau mỗi lượt chơi, máy hiển thị số lần đoán còn lại. Nếu đoán hết lượt mà không đoán đúng, trò chơi kết thúc và tiết lộ số bí mật.
#   - Điểm cao nhất sẽ được lưu lại khi người chơi đoán đúng với số lần ít nhất.

import random

def number_guessing_game():
    best_score = float('inf')  # Điểm cao nhất

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
        
        secret_number = random.randint(1, 100)
        attempts = 0

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
                    
                    # Cập nhật điểm cao nhất nếu có
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

# Chạy trò chơi
number_guessing_game()



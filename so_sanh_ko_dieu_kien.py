#                                                         Compare the largest and smallest numbers without if,else and min max and >,<,== 
print("so sánh số lớn nhất và nhỏ nhất:")
a = int(input("nhập vào số thứ nhất: "))
b = int(input("nhập vào số thứ hai: "))
# Tính toán
result = ( a+b + abs(b - a)) / 2
# In kết quả
print(f" Số lớn nhất là : {result}")


#                                                                               DOI MAT KHAU
# Người dùng nhập mật khẩu bí mật của họ
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

# 1. Tính tổng các số nguyên từ 1 đến n
def tinh_tong(n):
    return sum(range(1, n + 1))

# Ví dụ sử dụng
n = 10
print(f"Tong cac so tu 1 den {n}: {tinh_tong(n)}")

# 2. Tìm số lớn nhất trong một danh sách
def tim_so_lon_nhat(danh_sach):
    return max(danh_sach)

# Ví dụ sử dụng
danh_sach = [3, 7, 2, 9, 4]
print(f"So lon nhat trong danh sach: {tim_so_lon_nhat(danh_sach)}")


# 3. Đếm số lượng từ trong một chuỗi
def dem_so_luong_tu(chuoi):
    return len(chuoi.split())

# Ví dụ sử dụng
chuoi = "Hello world this is Python"
print(f"Số lượng từ trong chuỗi: {dem_so_luong_tu(chuoi)}")


# 4. Kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ví dụ sử dụng
num = 29
print(f"{num} là số nguyên tố: {kiem_tra_so_nguyen_to(num)}")


# 5. Tạo dãy Fibonacci
def tao_day_fibonacci(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo[:n]

# Ví dụ sử dụng
n = 10
print(f"Dãy Fibonacci đến {n} số: {tao_day_fibonacci(n)}")


# 6. Tính giai thừa của một số
def tinh_giai_thua(num):
    if num == 0:
        return 1
    return num * tinh_giai_thua(num - 1)

# Ví dụ sử dụng
num = 5
print(f"Giai thừa của {num} là: {tinh_giai_thua(num)}")

# 7. Đảo ngược chuỗi
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

# Ví dụ sử dụng
chuoi = "Python"
print(f"Chuỗi đảo ngược: {dao_nguoc_chuoi(chuoi)}")


# 8. Tính diện tích hình tròn
import math

def tinh_dien_tich_hinh_tron(ban_kinh):
    return math.pi * (ban_kinh ** 2)

# Ví dụ sử dụng
ban_kinh = 5
print(f"Diện tích hình tròn với bán kính {ban_kinh}: {tinh_dien_tich_hinh_tron(ban_kinh)}")


# 9. Chuyển đổi danh sách thành chuỗi
def chuyen_danh_sach_sang_chuoi(danh_sach):
    return ', '.join(danh_sach)

# Ví dụ sử dụng
danh_sach = ['apple', 'banana', 'cherry']
print(f"Danh sách dưới dạng chuỗi: {chuyen_danh_sach_sang_chuoi(danh_sach)}")


# 10. Lấy phần tử duy nhất từ danh sách
def lay_phan_tu_duy_nhat(danh_sach):
    return list(set(danh_sach))

# Ví dụ sử dụng
danh_sach = [1, 2, 2, 3, 4, 4, 5]
print(f"Các phần tử duy nhất trong danh sách: {lay_phan_tu_duy_nhat(danh_sach)}")


# CARO 9X9

# Chương trình cờ caro 9x9

def create_board(size):
    return [[' ' for _ in range(size)] for _ in range(size)]

def print_board(board):
    print("  " + " ".join([str(i) for i in range(len(board))]))
    for idx, row in enumerate(board):
        print(idx, "|", " ".join(row))

def check_winner(board, player):
    size = len(board)
    # Kiểm tra hàng ngang, hàng dọc và đường chéo
    for i in range(size):
        for j in range(size):
            if j <= size - 5 and all(board[i][j + k] == player for k in range(5)):
                return True
            if i <= size - 5 and all(board[i + k][j] == player for k in range(5)):
                return True
            if i <= size - 5 and j <= size - 5 and all(board[i + k][j + k] == player for k in range(5)):
                return True
            if i >= 4 and j <= size - 5 and all(board[i - k][j + k] == player for k in range(5)):
                return True
    return False

def main():
    size = 9
    board = create_board(size)
    current_player = 'X'

    for turn in range(size * size):
        print_board(board)
        print(f"Lượt của người chơi {current_player}:")
        row, col = map(int, input("Nhập hàng và cột (cách nhau bởi dấu cách, từ 0 đến 8): ").split())

        if board[row][col] != ' ':
            print("Ô này đã có quân cờ, hãy chọn ô khác!")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Chúc mừng! Người chơi {current_player} đã thắng!")
            break

        current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Trò chơi kết thúc! Hòa!")

if __name__ == "__main__":
    main()



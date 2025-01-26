import re
import time
import hashlib
from random import randint
from getpass import getpass  # Để nhập mật khẩu an toàn hơn


def hash_password(password, salt=""):
    """Mã hóa mật khẩu với SHA-256 và salt."""
    return hashlib.sha256((password + salt).encode()).hexdigest()


def validate(username, password):
    """Kiểm tra tính hợp lệ của tên tài khoản và mật khẩu."""
    if len(username.split()) < 2:
        print("Tên tài khoản phải bao gồm họ và tên.")
        return False
    if len(password) < 8:
        print("Mật khẩu phải có ít nhất 8 ký tự.")
        return False
    if not re.search(r'[A-Z]', password):
        print("Mật khẩu phải chứa ít nhất 1 chữ hoa.")
        return False
    if not re.search(r'[a-z]', password):
        print("Mật khẩu phải chứa ít nhất 1 chữ thường.")
        return False
    if not re.search(r'\d', password):
        print("Mật khẩu phải chứa ít nhất 1 chữ số.")
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt.")
        return False
    return True


def create_account():
    """Tạo tài khoản mới."""
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        password = getpass("Nhập mật khẩu (ít nhất 8 ký tự, chứa ký tự đặc biệt): ").strip()
        if validate(username, password):
            confirm_password = getpass("Nhập lại mật khẩu để xác nhận: ").strip()
            if password == confirm_password:
                print("Tạo tài khoản thành công!")
                salt = str(randint(1000, 9999))  # Tạo salt ngẫu nhiên
                return username, hash_password(password, salt), salt
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")


def login(username, hashed_password, salt):
    """Đăng nhập với số lần thử giới hạn."""
    attempts = 3
    while attempts > 0:
        input_username = input("Nhập tên tài khoản: ").strip()
        input_password = hash_password(getpass("Nhập mật khẩu: ").strip(), salt)
        if input_username == username and input_password == hashed_password:
            print("Đăng nhập thành công!")
            return True
        attempts -= 1
        print(f"Sai tài khoản hoặc mật khẩu. Còn {attempts} lần thử.")
    print("Tài khoản bị khóa tạm thời. Vui lòng thử lại sau.")
    return False


def menu():
    """Hiển thị menu chính."""
    print("\n=== MENU CHÍNH ===")
    print("1. Tìm giao điểm của 2 danh sách")
    print("2. Kiểm tra số nguyên tố")
    print("3. Xáo trộn danh sách")
    print("4. Sắp xếp danh sách (Bubble Sort)")
    print("5. Thoát")
    return input("Chọn một chức năng (1-5): ").strip()


def main():
    """Chương trình chính."""
    print("=== Thiết lập tài khoản ===")
    user, hashed_pw, salt = create_account()

    print("\n=== Đăng nhập ===")
    if not login(user, hashed_pw, salt):
        return

    while True:
        choice = menu()
        if choice == "1":
            list1 = list(map(int, input("Nhập danh sách 1 (cách nhau bởi dấu cách): ").split()))
            list2 = list(map(int, input("Nhập danh sách 2 (cách nhau bởi dấu cách): ").split()))
            print("Giao điểm:", sorted(set(list1) & set(list2)))
        elif choice == "2":
            n = int(input("Nhập số cần kiểm tra: "))
            print(f"{n} {'là' if is_prime(n) else 'không phải là'} số nguyên tố.")
        elif choice == "3":
            lst = list(map(int, input("Nhập danh sách cần xáo trộn (cách nhau bởi dấu cách): ").split()))
            print("Danh sách sau khi xáo trộn:", shuffle_list(lst))
        elif choice == "4":
            arr = list(map(int, input("Nhập danh sách cần sắp xếp (cách nhau bởi dấu cách): ").split()))
            order = input("Sắp xếp tăng dần (t/n)? ").strip().lower() == "t"
            print("Danh sách đã sắp xếp:", bubble_sort(arr, reverse=not order))
        elif choice == "5":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()

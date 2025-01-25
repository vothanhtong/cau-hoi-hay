import re
import time
import hashlib
from random import randint


def hash_password(password):
    """Mã hóa mật khẩu."""
    return hashlib.sha256(password.encode()).hexdigest()


def validate(username, password):
    """Kiểm tra tính hợp lệ của tên tài khoản và mật khẩu."""
    if len(username.split()) < 2:
        print("Tên tài khoản phải bao gồm họ và tên.")
        return False
    if len(password) < 8:
        print("Mật khẩu phải có ít nhất 8 ký tự.")
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        print("Mật khẩu phải chứa ít nhất 1 ký tự đặc biệt.")
        return False
    return True


def create_account():
    """Tạo tài khoản mới."""
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        password = input("Nhập mật khẩu (ít nhất 8 ký tự, chứa ký tự đặc biệt): ").strip()
        if validate(username, password):
            confirm_password = input("Nhập lại mật khẩu để xác nhận: ").strip()
            if password == confirm_password:
                print("Tạo tài khoản thành công!")
                return username, hash_password(password)
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")


def login(username, hashed_password):
    """Đăng nhập."""
    while True:
        input_username = input("Nhập tên tài khoản: ").strip()
        input_password = hash_password(input("Nhập mật khẩu: ").strip())
        if input_username == username and input_password == hashed_password:
            print("Đăng nhập thành công!")
            break
        print("Sai tài khoản hoặc mật khẩu. Vui lòng thử lại.")


def intersection(list1, list2):
    """Tìm giao điểm của hai danh sách."""
    return sorted(set(list1) & set(list2))


def is_prime(n):
    """Kiểm tra số nguyên tố."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def custom_random(seed=None):
    """Sinh số ngẫu nhiên."""
    seed = seed or int(time.time() * 1000)
    seed = (214013 * seed + 2531011) % (2**31)
    return seed / (2**31)


def shuffle_list(lst):
    """Xáo trộn danh sách."""
    for i in range(len(lst) - 1, 0, -1):
        j = randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst


def bubble_sort(arr, reverse=False):
    """Sắp xếp danh sách bằng Bubble Sort."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Nếu không có hoán vị nào, dừng sớm
            break
    return arr


def main():
    """Chương trình chính."""
    print("=== Thiết lập tài khoản ===")
    user, hashed_pw = create_account()

    print("\n=== Đăng nhập ===")
    login(user, hashed_pw)

    print("\n=== Các chức năng khác ===")
    print("Giao điểm:", intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("29 là số nguyên tố:", is_prime(29))
    print("Danh sách xáo trộn:", shuffle_list([1, 2, 3, 4, 5]))
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Tăng dần:", bubble_sort(arr.copy()))
    print("Giảm dần:", bubble_sort(arr.copy(), reverse=True))


if __name__ == "__main__":
    main()

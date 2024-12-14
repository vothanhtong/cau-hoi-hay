import re
import time

def validate(username, password):
    """Kiểm tra tính hợp lệ của tên tài khoản và mật khẩu."""
    return (
        len(username.split()) >= 2 and
        len(password) >= 8 and
        re.search(r'[^A-Za-z0-9]', password)
    )

def create_account():
    """Tạo tài khoản mới."""
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        password = input("Nhập mật khẩu (ít nhất 8 ký tự, chứa ký tự đặc biệt): ").strip()
        if validate(username, password):
            if password == input("Nhập lại mật khẩu để xác nhận: ").strip():
                print("Tạo tài khoản thành công!")
                return username, password
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")

def login(username, password):
    """Đăng nhập."""
    while True:
        if input("Nhập tên tài khoản: ").strip() == username and \
           input("Nhập mật khẩu: ").strip() == password:
            print("Đăng nhập thành công!")
            break
        print("Sai tài khoản hoặc mật khẩu. Vui lòng thử lại.")

def intersection(list1, list2):
    """Tìm giao điểm của hai danh sách."""
    return sorted(set(list1) & set(list2))

def is_prime(n):
    """Kiểm tra số nguyên tố."""
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    return all(n % i and n % (i + 2) for i in range(5, int(n**0.5) + 1, 6))

def custom_random(seed=None):
    """Sinh số ngẫu nhiên."""
    seed = (214013 * (seed or int(time.time() * 1000)) + 2531011) % (2**31)
    return seed / (2**31)

def shuffle_list(lst):
    """Xáo trộn danh sách."""
    for i in range(len(lst) - 1, 0, -1):
        j = int(custom_random() * (i + 1))
        lst[i], lst[j] = lst[j], lst[i]
    return lst

def bubble_sort(arr, reverse=False):
    """Sắp xếp danh sách bằng Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    """Chương trình chính."""
    print("=== Thiết lập tài khoản ===")
    user, pw = create_account()
    print("\n=== Đăng nhập ===")
    login(user, pw)

    print("\n=== Các chức năng khác ===")
    print("Giao điểm:", intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
    print("29 là số nguyên tố:", is_prime(29))
    print("Danh sách xáo trộn:", shuffle_list([1, 2, 3, 4, 5]))
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Tăng dần:", bubble_sort(arr.copy()))
    print("Giảm dần:", bubble_sort(arr.copy(), reverse=True))

if __name__ == "__main__":
    main()

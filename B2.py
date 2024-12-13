import re
import time

def validate(username, password):
    """
    Kiểm tra tính hợp lệ của tên tài khoản và mật khẩu.
    
    Args:
        username (str): Tên tài khoản.
        password (str): Mật khẩu.

    Returns:
        bool: True nếu hợp lệ, False nếu không.
    """
    return (
        len(username.split()) >= 2 and
        len(password) >= 8 and
        re.search(r'[^A-Za-z0-9]', password)
    )

def create_account():
    """
    Tạo một tài khoản mới bằng cách nhập tên tài khoản và mật khẩu.
    
    Returns:
        tuple: Tên tài khoản và mật khẩu hợp lệ.
    """
    while True:
        username = input("Nhập tên tài khoản (phải có họ và tên): ").strip()
        password = input("Nhập mật khẩu (ít nhất 8 ký tự, chứa ký tự đặc biệt): ").strip()
        
        if not validate(username, password):
            print("Tên tài khoản hoặc mật khẩu không hợp lệ. Vui lòng thử lại.")
            continue
        
        confirm_password = input("Nhập lại mật khẩu để xác nhận: ").strip()
        if password != confirm_password:
            print("Mật khẩu không khớp. Vui lòng thử lại.")
        else:
            print("Tạo tài khoản thành công!")
            return username, password

def login(username, password):
    """
    Đăng nhập bằng cách kiểm tra tên tài khoản và mật khẩu.
    
    Args:
        username (str): Tên tài khoản đã đăng ký.
        password (str): Mật khẩu đã đăng ký.
    """
    while True:
        entered_username = input("Nhập tên tài khoản: ").strip()
        entered_password = input("Nhập mật khẩu: ").strip()
        
        if entered_username == username and entered_password == password:
            print("Đăng nhập thành công!")
            break
        else:
            print("Sai tài khoản hoặc mật khẩu. Vui lòng thử lại.")

def intersection(list1, list2):
    """
    Tìm giao điểm của hai danh sách.

    Args:
        list1 (list): Danh sách đầu tiên.
        list2 (list): Danh sách thứ hai.

    Returns:
        list: Giao điểm của hai danh sách, được sắp xếp.
    """
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")
    return sorted(set(list1).intersection(list2))

def is_prime(n):
    """
    Kiểm tra một số có phải là số nguyên tố hay không.

    Args:
        n (int): Số cần kiểm tra.

    Returns:
        bool: True nếu là số nguyên tố, False nếu không.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def custom_random(seed=None):
    """
    Sinh số ngẫu nhiên dựa trên thuật toán tuyến tính.

    Args:
        seed (int): Giá trị khởi tạo. Nếu không có, sẽ lấy từ thời gian hiện tại.

    Returns:
        float: Số ngẫu nhiên trong khoảng [0, 1).
    """
    if seed is None:
        seed = int(time.time() * 1000)
    seed = (214013 * seed + 2531011) % (2**31)
    return seed / (2**31)

def shuffle_list(lst):
    """
    Xáo trộn danh sách bằng thuật toán Fisher-Yates.

    Args:
        lst (list): Danh sách cần xáo trộn.

    Returns:
        list: Danh sách đã được xáo trộn.
    """
    for i in range(len(lst) - 1, 0, -1):
        j = int(custom_random() * (i + 1))
        lst[i], lst[j] = lst[j], lst[i]
    return lst

def bubble_sort(arr, reverse=False):
    """
    Sắp xếp danh sách bằng thuật toán Bubble Sort.

    Args:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True nếu sắp xếp giảm dần, False nếu sắp xếp tăng dần.

    Returns:
        list: Danh sách đã được sắp xếp.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:  # XOR để kiểm soát hướng
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    """
    Chương trình chính để quản lý tài khoản và đăng nhập.
    """
    print("=== Thiết lập tài khoản ===")
    user, pw = create_account()
    
    print("\n=== Đăng nhập ===")
    login(user, pw)

    print("\n=== Các chức năng khác ===")

    # Câu hỏi 1: Giao điểm
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    print("Giao điểm:", intersection(list1, list2))

    # Câu hỏi 2: Số nguyên tố
    num = 29
    print(f"{num} là số nguyên tố:", is_prime(num))

    # Câu hỏi 3: Xáo trộn
    lst = [1, 2, 3, 4, 5]
    print("Danh sách xáo trộn:", shuffle_list(lst))

    # Câu hỏi 4: Sắp xếp
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Tăng dần:", bubble_sort(arr.copy()))
    print("Giảm dần:", bubble_sort(arr.copy(), reverse=True))

if __name__ == "__main__":
    main()

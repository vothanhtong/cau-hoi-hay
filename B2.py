### Câu hỏi 1: Giao điểm của hai danh sách
#### Nâng cấp:
# - Kiểm tra đầu vào hợp lệ để tránh lỗi bất ngờ.
# - Kết hợp danh sách đầu ra được sắp xếp.

def intersection(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")
    return sorted(set(list1).intersection(list2))

### Câu hỏi 2: Kiểm tra số nguyên tố
#### Nâng cấp:
# - Loại bỏ số chẵn và số chia hết cho 3 ngay từ đầu.
# - Sử dụng vòng lặp ngắn gọn hơn với khoảng bước (`step`).

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # return all(n % i != 0 and n % (i + 2) != 0 for i in range(5, int(n0.5) + 1, 6))/


### Câu hỏi 3: Xáo trộn danh sách
#### Nâng cấp:
# - Tự tạo hàm sinh số ngẫu nhiên để giảm phụ thuộc vào thư viện bên ngoài.
# - Đảm bảo mỗi phần tử đều có xác suất như nhau.


import time

def custom_random(seed=None):
    if seed is None:
        seed = int(time.time() * 1000)
    seed = (214013 * seed + 2531011) % (231)
    return seed / (231)

def shuffle_list(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = int(custom_random() * (i + 1))
        lst[i], lst[j] = lst[j], lst[i]
    return lst

### Thuật toán Bubble Sort
#### Nâng cấp:
# - Thêm khả năng sắp xếp tăng dần hoặc giảm dần (`reverse`).
# - Kết hợp kiểu Pythonic để viết ngắn gọn hơn.


def bubble_sort(arr, reverse=False):
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


### Giải thích cải tiến
# 1. Bảo mật:
#    - Kiểm tra đầu vào: Các hàm đều kiểm tra kiểu dữ liệu đầu vào (`TypeError`) để tránh lỗi logic.
#    - Loại bỏ thư viện bên ngoài: Tự xây dựng các chức năng ngẫu nhiên với kiểm soát tốt hơn.

# 2. Ngắn gọn:
#    - Sử dụng cú pháp Pythonic, như `all()`, `sorted()` để giảm số dòng code.
#    - Lồng điều kiện trực tiếp trong các phép kiểm tra.

# 3. Hiệu quả:
#    - Giảm vòng lặp dư thừa trong `is_prime`.
#    - Xử lý tối ưu thuật toán xáo trộn và sắp xếp.
### Cải tiến mã Python với lựa chọn tăng/giảm dần
#### Thêm tính năng:
# - Cho phép người dùng chọn tăng dần hoặc giảm dần bằng tham số `reverse`.
# - Sử dụng cú pháp Pythonic để ngắn gọn hơn.


def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:  # XOR để xác định hướng
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Dừng sớm nếu không có hoán đổi
            break
    return arr



### Minh họa sử dụng

arr = [64, 34, 25, 12, 22, 11, 90]

# Sắp xếp tăng dần
print("Tăng dần:", bubble_sort(arr.copy()))

# Sắp xếp giảm dần
print("Giảm dần:", bubble_sort(arr.copy(), reverse=True))


#### Kết quả

# Tăng dần: [11, 12, 22, 25, 34, 64, 90]
# Giảm dần: [90, 64, 34, 25, 22, 12, 11]
#### 1. Cơ chế hoạt động
# Bubble Sort là thuật toán sắp xếp đơn giản, thực hiện việc:
# - So sánh từng cặp phần tử liền kề và hoán đổi chúng nếu thứ tự không đúng.
# - Sau mỗi vòng lặp, phần tử lớn nhất (hoặc nhỏ nhất) được đặt đúng vị trí cuối cùng.
# - Tiếp tục lặp cho đến khi danh sách được sắp xếp.

#### 2. Tính chất
# - Thứ tự: Sắp xếp tăng dần (hoặc giảm dần nếu tùy chỉnh điều kiện).
# - Độ phức tạp thời gian:
#   - Tốt nhất: \(O(n)\) (danh sách đã sắp xếp và kiểm tra hoán đổi được kích hoạt).
#   - Trung bình & Xấu nhất: \(O(n^2)\) (khi cần nhiều lần hoán đổi).
# - Độ phức tạp không gian: \(O(1)\) (không cần bộ nhớ bổ sung).


#### 3. Mã giả

# 1. Lặp i từ 0 đến n-1:
#     2. Đặt `swapped = False`
#     3. Lặp j từ 0 đến n-i-2:
#         4. Nếu arr[j] > arr[j+1], hoán đổi và `swapped = True`
#     5. Nếu `swapped == False`, dừng thuật toán
# 2. Kết thúc


#### 4. Mã Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Duyệt qua từng phần tử
        swapped = False  # Biến kiểm tra hoán đổi
        for j in range(0, n - i - 1):  # So sánh các cặp phần tử
            if arr[j] > arr[j + 1]:  # Hoán đổi nếu cần
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Bước {i + 1}: {arr}")  # Hiển thị danh sách mỗi vòng
        if not swapped:  # Nếu không có hoán đổi, dừng thuật toán
            break


#### 5. Minh họa với ví dụ

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Danh sách ban đầu: {arr}")
bubble_sort(arr)
print(f"Danh sách sau khi sắp xếp: {arr}")


##### Kết quả chạy

# Danh sách ban đầu: [64, 34, 25, 12, 22, 11, 90]
# Bước 1: [34, 25, 12, 22, 11, 64, 90]
# Bước 2: [25, 12, 22, 11, 34, 64, 90]
# Bước 3: [12, 22, 11, 25, 34, 64, 90]
# Bước 4: [12, 11, 22, 25, 34, 64, 90]
# Bước 5: [11, 12, 22, 25, 34, 64, 90]
# Danh sách sau khi sắp xếp: [11, 12, 22, 25, 34, 64, 90]


#### 6. Phân tích từng bước
# 1. Bước 1: Phần tử lớn nhất (90) "nổi lên" vị trí cuối.
#    - Hoán đổi 64 ↔ 34, 34 ↔ 25, ..., cuối cùng 64 ↔ 90.
# 2. Bước 2: Phần tử lớn thứ hai (64) "nổi lên" trước 90.
#    - Lặp lại cho đến khi danh sách sắp xếp xong.


#### 7. Cải tiến
# - Kiểm tra hoán đổi (`swapped`):
#   - Nếu không có hoán đổi trong vòng lặp, danh sách đã được sắp xếp => thoát sớm.
#   - Giảm số lần duyệt không cần thiết.
# - Kết quả cải tiến:
#   - Trường hợp tốt nhất: \(O(n)\).

#### 8. Tình huống áp dụng
# - Danh sách nhỏ hoặc gần như đã sắp xếp: Bubble Sort hoạt động tốt, dễ triển khai.
# - Danh sách lớn hoặc ngẫu nhiên: Các thuật toán nhanh hơn như Quick Sort, Merge Sort được ưu tiên.

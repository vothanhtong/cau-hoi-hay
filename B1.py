### Tổng quan thuật toán
# - Cơ chế hoạt động: Bubble Sort so sánh từng cặp phần tử liền kề trong danh sách và hoán đổi chúng nếu phần tử trước lớn hơn phần tử sau. Quá trình này lặp lại cho đến khi không cần thực hiện thêm hoán đổi nào.
# - Tính chất:
#   - Thứ tự: Tăng dần (hoặc giảm dần nếu được tùy chỉnh).
#   - Độ phức tạp thời gian:
#     - Trường hợp xấu nhất và trung bình: \(O(n^2)\) (do duyệt lặp đi lặp lại).
#     - Trường hợp tốt nhất (khi đã sắp xếp): \(O(n)\) với cải tiến kiểm tra hoán đổi.

### Mã giả (Pseudocode):
# text
# 1. Bắt đầu từ i = 0 đến n-1:
#     2. So sánh từng cặp phần tử liền kề từ j = 0 đến n-i-2:
#         3. Nếu arr[j] > arr[j+1], hoán đổi chúng.
#     4. Nếu không có hoán đổi nào trong bước này, thoát khỏi vòng lặp.
# 5. Kết thúc.

### Phân tích mã 


def bubble_sort(arr):
    n = len(arr)
    # Duyệt qua tất cả các phần tử của danh sách
    for i in range(n):
        swapped = False  # Kiểm tra có hoán đổi không
        # Duyệt từ 0 đến n-i-1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # So sánh 2 phần tử liền kề
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Hoán đổi
                swapped = True
        # In danh sách sau mỗi bước
        print(f"Bước {i + 1}: {arr}")
        if not swapped:  # Nếu không có hoán đổi, dừng thuật toán
            break


#### Ví dụ minh họa

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Danh sách ban đầu: {arr}")
bubble_sort(arr)
print(f"Danh sách sau khi sắp xếp: {arr}")

#### Kết quả
# Danh sách ban đầu: [64, 34, 25, 12, 22, 11, 90]
# Bước 1: [34, 25, 12, 22, 11, 64, 90]
# Bước 2: [25, 12, 22, 11, 34, 64, 90]
# Bước 3: [12, 22, 11, 25, 34, 64, 90]
# Bước 4: [12, 11, 22, 25, 34, 64, 90]
# Bước 5: [11, 12, 22, 25, 34, 64, 90]
# Danh sách sau khi sắp xếp: [11, 12, 22, 25, 34, 64, 90]


### Giải thích từng bước
# 1. Bước 1: Phần tử lớn nhất "nổi" lên cuối danh sách.
#    - 64 → 90 được hoán đổi, kết quả: `[34, 25, 12, 22, 11, 64, 90]`.
# 2. Bước 2: Tiếp tục nổi phần tử lớn thứ hai lên trước 90.
#    - 64 → 34 → 11 → 64 "nổi lên", kết quả: `[25, 12, 22, 11, 34, 64, 90]`.
# 3. Các bước sau giảm dần số lần duyệt do các phần tử đã được sắp xếp.

### Cải tiến Bubble Sort
# Nếu thêm kiểm tra hoán đổi (`swapped`), thuật toán có thể thoát sớm khi danh sách đã được sắp xếp.

# if not swapped:
#     break


# Điều này giúp giảm số vòng lặp không cần thiết.



### Tình huống áp dụng
# - Bubble Sort hiệu quả cho danh sách nhỏ hoặc gần như đã sắp xếp.
# - Đối với danh sách lớn hoặc dữ liệu ngẫu nhiên, các thuật toán khác như Quick Sort, Merge Sort sẽ hiệu quả hơn.


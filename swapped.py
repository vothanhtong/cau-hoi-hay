def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Kiểm tra có hoán đổi không
        # Duyệt từ 0 đến n-i-1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # So sánh 2 phần tử liền kề
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Hoán đổi
                swapped = True
        # In danh sách sau mỗi bước (tùy chọn)
        print(f"Bước {i + 1}: {arr}")
        if not swapped:  # Nếu không có hoán đổi, dừng thuật toán
            break
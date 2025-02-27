def bubble_sort(arr):
    n = len(arr)  # Lấy độ dài mảng
    for i in range(n):  # Vòng lặp cho mỗi bước sắp xếp
        swapped = False  # Biến kiểm tra có hoán đổi không
        for j in range(0, n - i - 1):  # Vòng lặp so sánh các cặp phần tử
            if arr[j] > arr[j + 1]:  # Nếu phần tử trước lớn hơn phần tử sau
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Hoán đổi vị trí
                swapped = True  # Đánh dấu đã hoán đổi
        print(f"Bước {i + 1}: {arr}")  # In mảng sau mỗi bước (tùy chọn)
        if not swapped:  # Nếu không có hoán đổi, mảng đã sắp xếp xong
            break  # Thoát khỏi vòng lặp
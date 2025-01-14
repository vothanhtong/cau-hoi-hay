def bubble_sort(arr, reverse=False):
    """
    Sắp xếp danh sách bằng thuật toán Bubble Sort.

    Tham số:
        arr (list): Danh sách cần sắp xếp (không thay đổi).
        reverse (bool): True nếu sắp xếp giảm dần, False nếu sắp xếp tăng dần.

    Trả về:
        list: Danh sách đã được sắp xếp.
    """
    arr = arr[:]  # Tạo bản sao để bảo vệ danh sách gốc
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]) ^ reverse:  # XOR để kiểm tra hướng sắp xếp
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Minh họa sử dụng
if __name__ == "__main__":
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], False, "Tăng dần"),
        ([64, 34, 25, 12, 22, 11, 90], True, "Giảm dần"),
        ([], False, "Danh sách rỗng"),
        ([42], False, "Danh sách một phần tử"),
        ([5, 5, 5, 5], False, "Danh sách giá trị giống nhau"),
    ]

    for arr, reverse, desc in test_cases:
        print(f"{desc}: {bubble_sort(arr, reverse)}")

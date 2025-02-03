from functools import cmp_to_key

def bubble_sort(arr, reverse=False, key=None, inplace=False, verbose=False):
    """
    Sắp xếp danh sách bằng thuật toán Bubble Sort (Tối ưu hóa).

    Tham số:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True nếu sắp xếp giảm dần, False nếu sắp xếp tăng dần.
        key (callable, optional): Hàm để lấy giá trị so sánh từ phần tử.
        inplace (bool): True nếu sắp xếp trên danh sách gốc, False để tạo bản sao.
        verbose (bool): True nếu muốn in ra quá trình sắp xếp.

    Trả về:
        list: Danh sách đã được sắp xếp.

    Raises:
        TypeError: Nếu tham số `arr` không phải là danh sách hoặc `key` không hợp lệ.
        ValueError: Nếu danh sách chứa các phần tử không thể so sánh.
    """
    if not isinstance(arr, list):
        raise TypeError("Tham số 'arr' phải là danh sách.")

    if key is not None and not callable(key):
        raise TypeError("Tham số 'key' phải là một callable (hàm).")

    if not inplace:
        arr = arr[:]  # Tạo bản sao nếu không muốn thay đổi danh sách gốc

    # Mặc định key là identity function (trả về chính phần tử đó)
    key = key or (lambda x: x)

    # Kiểm tra kiểu dữ liệu của các phần tử trong danh sách
    try:
        _ = [key(x) for x in arr]  # Thử trích xuất key từ tất cả phần tử
    except Exception as e:
        raise ValueError("Danh sách chứa phần tử không thể so sánh hoặc key không hợp lệ.") from e

    n = len(arr)
    for i in range(n - 1):
        swaps = [
            (j, j + 1) for j in range(n - i - 1)
            if (key(arr[j]) > key(arr[j + 1])) ^ reverse
        ]

        if not swaps:
            if verbose:
                print(f"Không còn hoán đổi ở vòng lặp {i + 1}. Kết thúc sớm!")
            break

        for j, k in swaps:
            arr[j], arr[k] = arr[k], arr[j]
            if verbose:
                print(f"Hoán đổi: {arr[j]} ↔ {arr[k]} -> {arr}")

    if verbose:
        print(f"Danh sách đã được sắp xếp: {arr}")

    return arr


# Minh họa sử dụng
if __name__ == "__main__":
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], False, None, False, "Tăng dần"),
        ([64, 34, 25, 12, 22, 11, 90], True, None, False, "Giảm dần"),
        ([("a", 3), ("b", 1), ("c", 2)], False, lambda x: x[1], False, "Sắp xếp theo giá trị trong tuple"),
        ([("x", 3), ("y", 1), ("z", 2)], False, None, False, "Sắp xếp tuple khi không có key"),
        ([], False, None, False, "Danh sách rỗng"),
        ([42], False, None, False, "Danh sách một phần tử"),
        ([5, 5, 5, 5], False, None, False, "Danh sách giá trị giống nhau"),
        ([3.1, 2.4, 5.6, 1.2], True, None, True, "Danh sách số thực giảm dần"),
    ]

    for arr, reverse, key, verbose, desc in test_cases:
        print(f"{desc}: {bubble_sort(arr, reverse=reverse, key=key, verbose=verbose)}")

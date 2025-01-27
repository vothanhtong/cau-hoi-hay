def bubble_sort(arr, reverse=False, key=None, inplace=False, verbose=False, stability=False):
    """
    Sắp xếp danh sách bằng thuật toán Bubble Sort.

    Tham số:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True nếu sắp xếp giảm dần, False nếu sắp xếp tăng dần.
        key (callable, optional): Hàm để lấy giá trị so sánh từ phần tử.
        inplace (bool): True nếu sắp xếp trên danh sách gốc, False để tạo bản sao.
        verbose (bool): True nếu muốn in ra quá trình sắp xếp.
        stability (bool): True nếu muốn đảm bảo tính ổn định của thuật toán.

    Trả về:
        list: Danh sách đã được sắp xếp.

    Raises:
        TypeError: Nếu tham số `arr` không phải là danh sách hoặc `key` không hợp lệ.
        ValueError: Nếu danh sách chứa các phần tử không thể so sánh.
    """
    # Kiểm tra đầu vào
    if not isinstance(arr, list):
        raise TypeError("Tham số 'arr' phải là danh sách.")

    if key is not None and not callable(key):
        raise TypeError("Tham số 'key' phải là một callable (hàm).")

    if not inplace:
        arr = arr[:]  # Tạo bản sao nếu không muốn thay đổi danh sách gốc

    key = key or (lambda x: x)  # Mặc định không dùng key

    try:
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                # So sánh dựa trên key và hướng sắp xếp
                if (key(arr[j]) > key(arr[j + 1])) ^ reverse:
                    # Đảm bảo tính ổn định (không hoán đổi nếu hai phần tử bằng nhau và stability = True)
                    if stability and key(arr[j]) == key(arr[j + 1]):
                        continue
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    if verbose:
                        print(f"Hoán đổi: {arr[j]} ↔ {arr[j+1]} -> {arr}")

            if not swapped:  # Nếu không còn hoán đổi, kết thúc sớm
                if verbose:
                    print(f"Không còn hoán đổi ở vòng lặp {i + 1}. Kết thúc sớm!")
                break

        if verbose:
            print(f"Danh sách đã được sắp xếp: {arr}")

        return arr

    except TypeError as e:
        raise ValueError("Danh sách chứa phần tử không thể so sánh hoặc key không hợp lệ.") from e


# Minh họa sử dụng
if __name__ == "__main__":
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], False, None, False, "Tăng dần"),
        ([64, 34, 25, 12, 22, 11, 90], True, None, False, "Giảm dần"),
        ([("a", 3), ("b", 1), ("c", 2)], False, lambda x: x[1], False, "Sắp xếp theo giá trị trong tuple"),
        ([], False, None, False, "Danh sách rỗng"),
        ([42], False, None, False, "Danh sách một phần tử"),
        ([5, 5, 5, 5], False, None, False, "Danh sách giá trị giống nhau"),
        ([3.1, 2.4, 5.6, 1.2], True, None, True, "Danh sách số thực giảm dần"),
        ([("x", 2), ("y", 2), ("z", 1)], False, lambda x: x[1], True, "Sắp xếp với tính ổn định")
    ]

    for arr, reverse, key, verbose, desc in test_cases:
        print(f"{desc}: {bubble_sort(arr, reverse=reverse, key=key, verbose=verbose, stability=True)}")

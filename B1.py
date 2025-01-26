def bubble_sort(arr, reverse=False, key=None, inplace=False, verbose=False):
    """
    Sắp xếp danh sách bằng thuật toán Bubble Sort.

    Tham số:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True nếu sắp xếp giảm dần, False nếu sắp xếp tăng dần.
        key (callable, optional): Hàm để lấy giá trị so sánh từ phần tử.
        inplace (bool): True nếu sắp xếp trên danh sách gốc, False để tạo bản sao.
        verbose (bool): True nếu muốn in ra quá trình sắp xếp.

    Trả về:
        list: Danh sách đã được sắp xếp.
    """
    if not inplace:
        arr = arr[:]  # Tạo bản sao nếu không muốn thay đổi danh sách gốc

    if key is None:
        key = lambda x: x  # Mặc định không dùng key

    try:
        n = len(arr)
        for i in range(n - 1):
            swapped = False
            for j in range(n - i - 1):
                # So sánh dựa trên key và hướng sắp xếp
                if (key(arr[j]) > key(arr[j + 1])) ^ reverse:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                    if verbose:
                        print(f"Hoán đổi: {arr[j]} ↔ {arr[j+1]} -> {arr}")
            if not swapped:
                if verbose:
                    print(f"Không còn hoán đổi ở vòng lặp {i + 1}. Kết thúc sớm!")
                break
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
    ]

    for arr, reverse, key, verbose, desc in test_cases:
        print(f"{desc}: {bubble_sort(arr, reverse=reverse, key=key, verbose=verbose)}")

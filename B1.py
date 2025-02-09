from functools import cmp_to_key

def cocktail_shaker_sort(arr, reverse=False, key=None, inplace=False, verbose=False):
    """
    Sắp xếp danh sách bằng thuật toán Cocktail Shaker Sort (cải tiến Bubble Sort).

    Tham số:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True nếu sắp xếp giảm dần, False nếu tăng dần.
        key (callable, optional): Hàm để lấy giá trị so sánh từ phần tử.
        inplace (bool): True nếu sắp xếp trên danh sách gốc, False để tạo bản sao.
        verbose (bool): True nếu muốn in ra quá trình sắp xếp.

    Trả về:
        list: Danh sách đã được sắp xếp.
    """
    if not isinstance(arr, list):
        raise TypeError("Tham số 'arr' phải là danh sách.")
    if key is not None and not callable(key):
        raise TypeError("Tham số 'key' phải là một callable (hàm).")
    
    if not inplace:
        arr = arr[:]
    
    key = key or (lambda x: x)
    
    try:
        _ = [key(x) for x in arr]
    except Exception as e:
        raise ValueError("Danh sách chứa phần tử không thể so sánh hoặc key không hợp lệ.") from e
    
    left = 0
    right = len(arr) - 1
    swapped = True
    
    while left < right and swapped:
        swapped = False
        
        # Duyệt từ trái sang phải
        for i in range(left, right):
            if (key(arr[i]) > key(arr[i + 1])) ^ reverse:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                if verbose:
                    print(f"Hoán đổi: {arr[i]} ↔ {arr[i + 1]} -> {arr}")
        
        right -= 1  # Giảm phạm vi duyệt
        
        # Duyệt từ phải sang trái
        for i in range(right, left, -1):
            if (key(arr[i - 1]) > key(arr[i])) ^ reverse:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
                if verbose:
                    print(f"Hoán đổi: {arr[i]} ↔ {arr[i - 1]} -> {arr}")
        
        left += 1  # Tăng phạm vi duyệt
    
    if verbose:
        print(f"Danh sách đã được sắp xếp: {arr}")
    
    return arr

# Minh họa sử dụng
if __name__ == "__main__":
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], False, None, False, "Tăng dần"),
        ([64, 34, 25, 12, 22, 11, 90], True, None, False, "Giảm dần"),
        ([("a", 3), ("b", 1), ("c", 2)], False, lambda x: x[1], False, "Sắp xếp theo giá trị trong tuple"),
        ([3.1, 2.4, 5.6, 1.2], True, None, True, "Danh sách số thực giảm dần"),
    ]
    
    for arr, reverse, key, verbose, desc in test_cases:
        print(f"{desc}: {cocktail_shaker_sort(arr, reverse=reverse, key=key, verbose=verbose)}")

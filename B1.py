from functools import cmp_to_key
from typing import List, Callable, Any, Tuple
import time

def cocktail_shaker_sort(
    arr: List[Any],
    reverse: bool = False,
    key: Callable[[Any], Any] | None = None,
    cmp: Callable[[Any, Any], int] | None = None,
    inplace: bool = False,
    verbose: bool = False,
    stats: bool = False
) -> List[Any]:
    """
    Sắp xếp danh sách bằng thuật toán Cocktail Shaker Sort (cải tiến Bubble Sort).

    Tham số:
        arr (list): Danh sách cần sắp xếp.
        reverse (bool): True để sắp xếp giảm dần, False để tăng dần (mặc định).
        key (callable, optional): Hàm trả về giá trị so sánh từ phần tử.
        cmp (callable, optional): Hàm so sánh tùy chỉnh (trả về -1, 0, 1).
        inplace (bool): True để sửa đổi danh sách gốc, False để trả về bản sao.
        verbose (bool): True để in chi tiết quá trình sắp xếp.
        stats (bool): True để hiển thị thống kê hiệu suất (thời gian, số phép so sánh).

    Trả về:
        list: Danh sách đã được sắp xếp.

    Ngoại lệ:
        TypeError: Nếu arr không phải list hoặc key không phải callable.
        ValueError: Nếu phần tử không thể so sánh với key hoặc cmp.
    """
    # Kiểm tra kiểu dữ liệu đầu vào
    if not isinstance(arr, list):
        raise TypeError("Tham số 'arr' phải là một danh sách (list).")
    if key is not None and not callable(key):
        raise TypeError("Tham số 'key' phải là một callable (hàm).")
    if cmp is not None and not callable(cmp):
        raise TypeError("Tham số 'cmp' phải là một callable (hàm).")

    # Tạo bản sao nếu không sắp xếp tại chỗ
    result = arr if inplace else arr()
    if not result:  # Danh sách rỗng thì trả về ngay
        return result

    # Xử lý hàm key và cmp
    key_func = key if key else (lambda x: x)
    cmp_func = cmp if cmp else (lambda a, b: (a > b) - (a < b))

    # Kiểm tra khả năng so sánh của các phần tử
    try:
        sample = [key_func(x) for x in result]
    except Exception as e:
        raise ValueError("Phần tử trong danh sách không thể so sánh hoặc key không hợp lệ.") from e

    # Khởi tạo biến
    left, right = 0, len(result) - 1
    swapped = True
    comparisons = 0  # Đếm số phép so sánh
    start_time = time.perf_counter() if stats else None

    # Vòng lặp chính của Cocktail Sort
    while left < right and swapped:
        swapped = False
        last_swap = left  # Theo dõi vị trí cuối cùng mà hoán đổi xảy ra

        # Duyệt từ trái sang phải
        for i in range(left, right):
            comparisons += 1
            left_val, right_val = key_func(result[i]), key_func(result[i + 1])
            if (cmp_func(left_val, right_val) > 0) ^ reverse:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
                last_swap = i
                if verbose:
                    print(f"Hoán đổi ( trái -> phải): {result[i]} ↔ {result[i + 1]} -> {result}")

        right = last_swap  # Thu hẹp phạm vi

        # Duyệt từ phải sang trái
        for i in range(right, left, -1):
            comparisons += 1
            left_val, right_val = key_func(result[i - 1]), key_func(result[i])
            if (cmp_func(left_val, right_val) > 0) ^ reverse:
                result[i], result[i - 1] = result[i - 1], result[i]
                swapped = True
                last_swap = i
                if verbose:
                    print(f"Hoán đổi (phải -> trái): {result[i]} ↔ {result[i - 1]} -> {result}")

        left = last_swap  # Thu hẹp phạm vi

    # Hiển thị kết quả và thống kê
    if verbose:
        print(f"Kết quả sắp xếp: {result}")
    
    if stats:
        elapsed_time = time.perf_counter() - start_time
        print(f"Thống kê: {comparisons} phép so sánh, {elapsed_time:.6f} giây")

    return result

# Minh họa sử dụng với các trường hợp kiểm tra
if __name__ == "__main__":
    # Danh sách kiểm tra với mô tả
    test_cases = [
        ([64, 34, 25, 12, 22, 11, 90], False, None, None, False, True, False, "Sắp xếp tăng dần"),
        ([64, 34, 25, 12, 22, 11, 90], True, None, None, False, True, False, "Sắp xếp giảm dần"),
        ([("a", 3), ("b", 1), ("c", 2)], False, lambda x: x[1], None, False, True, False, "Sắp xếp theo giá trị tuple"),
        ([3.1, 2.4, 5.6, 1.2], True, None, None, True, True, True, "Số thực giảm dần, tại chỗ"),
        ([], False, None, None, False, True, False, "Danh sách rỗng"),
        ([1], True, None, None, False, True, False, "Danh sách 1 phần tử"),
        (["z", "a", "c", "b"], False, str.lower, None, False, True, True, "Chuỗi theo thứ tự chữ cái"),
        ([64, 34, 25, 12, 22, 11, 90], False, None, lambda a, b: (a > b) - (a < b), False, True, False, "Sắp xếp tăng dần với cmp"),
    ]

    # Chạy từng trường hợp
    for arr, reverse, key, cmp, inplace, verbose, stats, desc in test_cases:
        print(f"\n=== {desc} ===")
        print(f"Trước: {arr}")
        try:
            sorted_arr = cocktail_shaker_sort(
                arr, reverse=reverse, key=key, cmp=cmp, inplace=inplace, verbose=verbose, stats=stats
            )
            print(f"Sau: {sorted_arr}")
        except (TypeError, ValueError) as e:
            print(f"Lỗi: {e}")

    # Trường hợp lỗi mẫu
    print("\n=== Trường hợp lỗi ===")
    try:
        cocktail_shaker_sort("not a list")  # Truyền chuỗi thay vì danh sách
    except TypeError as e:
        print(f"Lỗi: {e}")


# sorted_arr = cocktail_shaker_sort(arr, cmp=lambda a, b: (a > b) - (a < b))
# Sắp xếp giảm dần với key:



# sorted_arr = cocktail_shaker_sort(arr, key=lambda x: x[1], reverse=True)
# Sắp xếp tại chỗ với thống kê:



# sorted_arr = cocktail_shaker_sort(arr, inplace=True, stats=True)
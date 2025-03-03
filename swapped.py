from typing import List, Optional

def bubble_sort(arr: List[int], verbose: bool = False) -> List[int]:
    """
    Sắp xếp mảng số nguyên bằng thuật toán Bubble Sort.

    :param arr: Mảng số nguyên cần sắp xếp.
    :param verbose: Nếu True, in ra mảng sau mỗi bước sắp xếp.
    :return: Mảng đã được sắp xếp.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if verbose:
            print(f"Bước {i + 1}: {arr}")
        if not swapped:
            break
    return arr

# Ví dụ sử dụng
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Mảng ban đầu:", arr)
    sorted_arr = bubble_sort(arr, verbose=True)
    print("Mảng sau khi sắp xếp:", sorted_arr)
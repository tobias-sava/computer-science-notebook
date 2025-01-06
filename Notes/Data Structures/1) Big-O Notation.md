Big-O Notation - 01/01/2025

Big O notation is a way to describe how the performance of a computer 
program or algorithm changes as the amount of work it has to do increases.

-

Big-O Properties and Examples

0(n + c) = 0(n)
0(cn) = 0(n), c > 0

n = The size of the input

! Constant Time = 0(1)

    numbers = [1, 2, 3, 4, 5]
    print(numbers[2])  # Always takes the same amount of time.

! Logarithmic Time = 0(log(n))

    def binary_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    numbers = [1, 2, 3, 4, 5]
    print(binary_search(numbers, 4))  # Search halves each time.

! Linear Time = 0(n)

    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num)  # Time grows with the size of the list.

! Linearithmic Time = 0(nlog(n))

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        sorted_arr = []
        while left and right:
            if left[0] < right[0]:
                sorted_arr.append(left.pop(0))
            else:
                sorted_arr.append(right.pop(0))
        return sorted_arr + left + right

    numbers = [5, 3, 1, 4, 2]
    print(merge_sort(numbers))  # Divides and sorts.

! Quadric Time = 0(n^2)

    numbers = [1, 2, 3]
    for i in numbers:
        for j in numbers:
            print(i, j)  # Time grows with the square of the input size.

! Cubic Time = 0(n^3)

    numbers = [1, 2, 3]
    for i in numbers:
        for j in numbers:
            for k in numbers:
                print(i, j, k)  # Time grows with the cube of the input size.

! Exponential Time = 0(b^n)

    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)  # Calls double each step.

    print(fib(5))  # Time doubles with each step.

! Factorial Time = 0(n!)
                   
    from itertools import permutations

    numbers = [1, 2, 3]
    for perm in permutations(numbers):
        print(perm)  # Time grows as factorial of input size.













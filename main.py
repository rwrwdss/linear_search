import random
import time


def linear_search(nums, x):
    for i, v in enumerate(nums):
        if v == x:
            return i
    return -1


def binary_search(nums, x):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == x:
            return mid
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def bubble_sort(nums):
    a = list(nums)
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def linear_find_student_by_name(students, name):
    for i, s in enumerate(students):
        if s["name"] == name:
            return i
    return -1


def binary_find_student_by_gpa(students_sorted_by_gpa, gpa):
    lo, hi = 0, len(students_sorted_by_gpa) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        m = students_sorted_by_gpa[mid]["gpa"]
        if m == gpa:
            return mid
        if m < gpa:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def task1():
    print("Задача 1")
    size = 1_000_000
    data = [random.randint(0, 10**9) for _ in range(size)]
    target = data[random.randrange(size)]

    t0 = time.perf_counter()
    linear_search(data, target)
    t_lin = time.perf_counter() - t0

    t0 = time.perf_counter()
    data.sort()
    t_sort = time.perf_counter() - t0

    t0 = time.perf_counter()
    binary_search(data, target)
    t_bin = time.perf_counter() - t0

    print(f"линейный поиск: {t_lin:.6f} с")
    print(f"сортировка: {t_sort:.6f} с")
    print(f"бинарный поиск: {t_bin:.6f} с")


def task2():
    print("Задача 2")
    size = 10_000
    data = [random.randint(0, 10**5) for _ in range(size)]

    t0 = time.perf_counter()
    bubble_sort(data)
    t_bub = time.perf_counter() - t0

    t0 = time.perf_counter()
    sorted(data)
    t_builtin = time.perf_counter() - t0

    print(f"пузырёк: {t_bub:.6f} с")
    print(f"встроенная: {t_builtin:.6f} с")


def task3():
    print("Задача 3")
    random.seed(42)
    names = ["Анна", "Борис", "Вера", "Глеб", "Дина", "Егор", "Жанна", "Илья"]
    groups = ["ИС-101", "ИС-102", "МТ-201"]
    students = []
    for _ in range(5000):
        students.append(
            {
                "name": random.choice(names),
                "group": random.choice(groups),
                "gpa": round(random.uniform(2.0, 5.0), 2),
            }
        )

    name_target = students[1234]["name"]
    t0 = time.perf_counter()
    linear_find_student_by_name(students, name_target)
    t_name = time.perf_counter() - t0

    by_gpa = sorted(students, key=lambda s: s["gpa"])
    gpa_target = by_gpa[2500]["gpa"]
    t0 = time.perf_counter()
    binary_find_student_by_gpa(by_gpa, gpa_target)
    t_gpa = time.perf_counter() - t0

    print(f"поиск по имени (линейный): {t_name:.6f} с")
    print(f"поиск по баллу (бинарный): {t_gpa:.6f} с")


if __name__ == "__main__":
    task1()
    task2()
    task3()

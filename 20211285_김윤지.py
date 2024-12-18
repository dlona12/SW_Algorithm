import random
import time  # 실행 시간 측정 추가 

# 정렬 알고리즘
def selection_sort(arr, key, ascending=True):
    n = len(arr)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if (arr[j][key] < arr[least][key]) == ascending:
                least = j
        arr[i], arr[least] = arr[least], arr[i]

def insertion_sort(arr, key, ascending=True):
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        j = i - 1
        while j >= 0 and (arr[j][key] > current[key]) == ascending:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

def quick_sort(arr, key, ascending=True, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left < right:
        pivot = partition(arr, key, ascending, left, right)
        quick_sort(arr, key, ascending, left, pivot-1)
        quick_sort(arr, key, ascending, pivot+1, right)

def partition(arr, key, ascending, left, right):
    pivot = arr[left][key]
    low = left + 1
    high = right
    while low <= high:
        while low <= high and (arr[low][key] <= pivot) == ascending:
            low += 1
        while low <= high and (arr[high][key] > pivot) == ascending:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[left], arr[high] = arr[high], arr[left]
    return high

def radix_sort(arr, key):
    max_val = max(student[key] for student in arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, key, exp)
        exp *= 10

def counting_sort_radix(arr, key, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for student in arr:
        index = (student[key] // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for student in reversed(arr):
        index = (student[key] // exp) % 10
        output[count[index] - 1] = student
        count[index] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]

# 평균 및 통계 정보 계산 기능
def calculate_statistics(students):
    scores = [student["성적"] for student in students]
    average = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    print("\n[성적 통계 정보]")
    print(f"평균 성적: {average:.2f}")
    print(f"최고 성적: {max_score}")
    print(f"최저 성적: {min_score}")

# 정렬 알고리즘 성능 비교 기능 추가 
def compare_sorting_algorithms(students):
    import copy  
    
    algorithms = {
        "선택 정렬": selection_sort,
        "삽입 정렬": insertion_sort,
        "퀵 정렬": quick_sort,
        "기수 정렬": radix_sort
    }
    
    print("\n[정렬 알고리즘 성능 비교]")
    for name, algorithm in algorithms.items():
        # 데이터 복사본을 생성하여 원본 데이터를 보존
        students_copy = copy.deepcopy(students)
        
        # 시간 측정 시작
        start_time = time.time()
        
        # 성적을 기준으로 정렬 (기수 정렬만 key='성적')
        if name == "기수 정렬":
            algorithm(students_copy, "성적")
        else:
            algorithm(students_copy, "성적", ascending=True)
        
        # 시간 측정 종료
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"{name}: {elapsed_time:.6f}초")

# 데이터 생성
def generate_students(num=30):
    students = []
    for _ in range(num):
        name = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students

def display_students(students):
    print("\n학생 목록:")
    print("이름\t나이\t성적")
    for student in students:
        print(f"{student['이름']}\t{student['나이']}\t{student['성적']}")
    print()

# 메인 메뉴
def main():
    students = generate_students()
    print("\n[생성된 학생 정보]")
    display_students(students)
    calculate_statistics(students)  # 평균 정보 계산 기능
    
    while True:
        print("메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 정렬 알고리즘 성능 비교")
        print("5. 프로그램 종료")
        choice = input("정렬 기준을 선택하세요 (1, 2, 3, 4, 5): ")

        if choice == "5":
            print("프로그램을 종료합니다.")
            break

        if choice == "4":
            compare_sorting_algorithms(students)
            continue

        sort_order = input("오름차순 정렬은 1, 내림차순 정렬은 2를 입력하세요: ")
        ascending = sort_order == "1"

        print("\n정렬 알고리즘 선택:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬 (성적 기준만)")
        algorithm = input("알고리즘을 선택하세요 (1, 2, 3, 4): ")

        if choice == "1":
            key = "이름"
        elif choice == "2":
            key = "나이"
        elif choice == "3":
            key = "성적"
        else:
            print("잘못된 입력입니다.")
            continue

        if algorithm == "1":
            selection_sort(students, key, ascending)
        elif algorithm == "2":
            insertion_sort(students, key, ascending)
        elif algorithm == "3":
            quick_sort(students, key, ascending)
        elif algorithm == "4" and key == "성적":
            radix_sort(students, key)
        else:
            print("기수 정렬은 성적 기준일 때만 사용 가능합니다.")
            continue

        print(f"\n[정렬된 결과 - 기준: {key}, {'오름차순' if ascending else '내림차순'}]")
        display_students(students)

if __name__ == "__main__":
    main()

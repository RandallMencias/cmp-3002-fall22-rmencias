import random
import time

def clock(func):
    def inner(*arg, **kwargs):
        start = time.time() * 10 ** 3
        answer = func(*arg, **kwargs)
        time.sleep(0.1)
        end = time.time() * 10 ** 3
        #print("Execution Time:" + str(end - start))
        return answer, (end - start)

    return inner

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = int(len(nums) / 2)
    left = merge_sort(nums[0:pivot])
    right = merge_sort(nums[pivot:])
    return merge(left, right)


def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    sorted_list = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            sorted_list.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_list.append(right[right_pointer])
            right_pointer += 1

    sorted_list.extend(left[left_pointer:])
    sorted_list.extend(right[right_pointer:])

    return sorted_list

def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list.pop()
    l1 = []
    l2 = []
    for i in list:
        if i <= pivot:
            l1.append(i)
        else:
            l2.append(i)

    return quicksort(l1) + [pivot] + quicksort(l2)



def generate_random_list():
    return [random.randint(1, 1000) for i in range(1000)]

def main():
    lists = [generate_random_list() for i in range(2)]
    merge_sort_time = [merge_sort(i)[1] for i in lists]
    print(merge_sort_time)
    quicksort_time = [quicksort(i) for i in lists]
    # print(merge_sort_time, quicksort_time)

if __name__ == "__main__":
    main()




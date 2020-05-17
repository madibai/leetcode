from itertools import product


def easy_TwoSum1(nums, target):
    a = [2, 7, 11, 15]
    a.sort()
    arr = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:   continue
        s2 = i + 1
        while len(arr) == 0:
            sums = nums[i] + nums[s2]
            if sums == target:
                arr.append([nums[i], nums[s2]])
                a1 = i
                a2 = s2
                break
            if sums < target:
                s2 += 1
            else:
                i -= 1
    print([a1, a2])
    print(target)


def easy_TwoSum2(nums, target):
    complement = {}
    for i, v in enumerate(nums):
        # if v = nums[i] in complement, we find a solution
        if v in complement:
            return complement[v], i
        # if v = nums[i] not in complement, we store the element into the dictionary.
        else:
            complement[target - v] = i
    return -1


def valid_parentheses20(s) -> bool:
    braces = {')': '(', '}': '{', ']': '['}
    stack = []
    for i, c in enumerate(s, start=1):
        if c in braces.values():
            stack.append((c, i))
        if c in braces and (not stack or braces[c] != stack.pop()[0]):
            return False
    return True if len(stack) == 0 else False


def simplify_path(s) -> str:
    elements = [p for p in s.split("/") if p != "." and p != ""]
    stack = []
    for p in elements:
        if p == "..":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(p)
    return "/" + "/".join(stack)


def simplfpath2(s) -> str:
    stack_slash = []
    stack_dots = []
    answer = ''
    for i in s:
        if i == '/':
            if len(answer) == 0:
                answer += i
                # stack_slash.append(i)
            elif answer[-1] == '/':
                answer
                # stack_slash.pop()
            elif answer[-1] == '.':
                answer = answer[:-1]
            else:
                answer += i
        elif i == '.':
            if answer[-1] == '.':
                answer = answer[:-3]
                # stack_dots.pop()
            else:
                answer += i
                # stack_dots.append(i)
        else:
            answer += i
    return answer[:-1] if (answer[-1] == '/' or answer[-1] == '.') and len(answer) > 1 else answer


def check_circular_queue(k):
    class circular_queue:

        def __init__(self, k: int):
            """
            Initialize your data structure here. Set the size of the queue to be k.
            """
            self.q = [None] * k
            self.len = k
            self.front = 0
            self.rear = 0

        def enQueue(self, value: int) -> bool:
            """
            Insert an element into the circular queue. Return true if the operation is successful.
            """
            if self.q[self.rear] is None:
                self.q[self.rear] = value
                self.rear = (self.rear + 1) % self.len
                return True
            else:
                return False

        def deQueue(self) -> bool:
            """
            Delete an element from the circular queue. Return true if the operation is successful.
            """
            if self.q[self.front] is None:
                return False
            else:
                self.q[self.front] = None
                self.front = (self.front + 1) % self.len
                return True

        def Front(self) -> int:
            """
            Get the front item from the queue.
            """
            return -1 if self.q[self.front] is None else self.q[self.front]

        def Rear(self) -> int:
            """
            Get the last item from the queue.
            """
            return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

        def isEmpty(self) -> bool:
            """
            Checks whether the circular queue is empty or not.
            """
            return self.front == self.rear and self.q[self.front] is None

        def isFull(self) -> bool:
            """
            Checks whether the circular queue is full or not.
            """
            return self.front == self.rear and self.q[self.front] is not None

    circularQueue = circular_queue(k)
    print(circularQueue.enQueue(1))
    print(circularQueue.enQueue(2))
    print(circularQueue.enQueue(3))
    print(circularQueue.enQueue(4))
    print(circularQueue.enQueue(5))
    print(circularQueue.enQueue(6))
    print(circularQueue.Rear())
    print(circularQueue.isFull())
    print(circularQueue.deQueue())
    print(circularQueue.enQueue(4))
    print(circularQueue.Rear())


def letter_combinations_of_a_phone_number(digits):
    map_dict = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    cmb = [''] if digits else []
    for d in digits:
        cmb = [p + q for p in cmb for q in map_dict[d]]
    return cmb


def delete_duplicates_in_sorted_array(arr):
    a = list(dict.fromkeys(arr))
    print(*a)
    print(len(list(dict.fromkeys(arr))))
    if len(arr) == 0:
        return 0
    j = 1
    i = 0
    while j < len(arr):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
        j += 1
    answer = i + 1
    return len(a), answer


def python_lambda():
    def to_upper_case(s):
        return str(s).upper()
    aa = map(to_upper_case, 'abc')
    print(*aa)

    map_iterator = map(to_upper_case, ['a', 'b', 'c'])
    my_list = list(map_iterator)
    map_iterator = map(to_upper_case, ['a', 'b', 'c'])
    my_set = set(map_iterator)
    map_iterator = map(to_upper_case, ['a', 'b', 'c'])
    my_tuple = tuple(map_iterator)
    print(my_list, my_set, my_tuple)

    list_numbers = [1, 2, 3, 4]

    map_iterator1 = map(lambda x: x * 2, list_numbers)
    map_iterator2 = lambda x: x * 2, list_numbers
    print(*map_iterator1)
    print(*map_iterator2)

    list_numbers = [1, 2, 3, 4]
    tuple_numbers = (5, 6, 7, 8)
    map_iterator = map(lambda x, y: x - y, list_numbers, tuple_numbers)
    print(*map_iterator)

    l = ['sata', 'badt', 'cats', 'amat']
    test = list(map(list, l))
    print(test)

    return 0


def easy_kids_test():
    #   1431. Kids With the Greatest Number of Candies
    print(easy_kids([2,3,5,1,3], 3))


def easy_kids(candies, extraCandies):
    tmp = max(candies)
    res = [candy + extraCandies >= tmp for candy in candies]
    return res


def query_permu_test():
    #   1409. Queries on a Permutation With Key
    print(query_permu([3,1,2,1], 5))
    print(query_permu([4,1,2,2], 4))
    print(query_permu([7,5,5,8,3], 8))


def query_permu(queries, m):
    tmp = list(range(1, m+1))
    res = []
    for i in queries:
        res.append(tmp.index(i))
        tmp.insert(0, tmp.pop(tmp.index(i)))
    return res


def count_number_test():
    #   1395. Count Number of Teams
    print(count_number([2,5,3,4,1]))
    print(count_number([2,1,3]))
    print(count_number([1,2,3,4]))


def count_number(rating):
    asc = dsc = 0
    for i, v in enumerate(rating):
        llc = rgc = lgc = rlc = 0
        for l in rating[:i]:
            if l < v:
                llc += 1
            if l > v:
                lgc += 1
        for r in rating[i + 1:]:
            if r > v:
                rgc += 1
            if r < v:
                rlc += 1
        asc += llc * rgc
        dsc += lgc * rlc
    return asc + dsc


if __name__ == '__main__':
    #   easy_TwoSum1()
    #   easy_TwoSum2()
    #   print(valid_parentheses20(''))
    #   print(simplify_path('/../'))
    #   print(simplify_path('/a//b////c/d//././/..'))
    #   print(simplify_path('/a/../../b/../c//.//'))
    #   check_circular_queue(5)
    #   print(letter_combinations_of_a_phone_number('23'))
    #   print(delete_duplicates_in_sorted_array([0,0,1,1,1,2,2,3,3,4]))
    #   python_lambda()
    #   easy_kids_test()
    #   query_permu_test()
    count_number_test()


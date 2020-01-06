from itertools import product


def easy_TwoSum1(nums, target):
    a = [2, 7, 11, 15]
    a.sort()
    arr = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:   continue
        s2 = i + 1
        while len(arr)==0:
            sums = nums[i]+nums[s2]
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
                #stack_slash.append(i)
            elif answer[-1] == '/':
                answer
                #stack_slash.pop()
            elif answer[-1] == '.':
                answer = answer[:-1]
            else:
                answer += i
        elif i == '.':
            if answer[-1] == '.':
                answer = answer[:-3]
                #stack_dots.pop()
            else:
                answer += i
                #stack_dots.append(i)
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


if __name__ == '__main__':
    #  easy_TwoSum1()
    #  easy_TwoSum2()
    #  print(valid_parentheses20(''))
    #  print(simplify_path('/../'))
    #  print(simplify_path('/a//b////c/d//././/..'))
    #  print(simplify_path('/a/../../b/../c//.//'))
    check_circular_queue(5)


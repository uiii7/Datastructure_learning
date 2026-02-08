from Day3_dequeue import Deque


class SlidingWindow:
    def __init__(self, nums, size):
        self.windowSize = size
        self.nums = nums

    def solve(self, nums):
        q = Deque()
        ans = []

        for i in range(len(nums)):
            q.addFront(nums[i])

            if q.size() > self.windowSize:
                q.removeRear()

            if q.size() == self.windowSize:
                ans.append(max(q.iterable()))

        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(SlidingWindow(nums, k).solve(nums))

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        fm = defaultdict(int)
        top = SortedList()
        low = SortedList()
        curr = 0

        def change(num, count):
            nonlocal curr
            prev = (fm[num], num)

            # Remove old value if present
            if fm[num]:
                if prev in low:
                    low.discard(prev)
                else:
                    top.discard(prev)
                    curr -= fm[num] * num

            # Update frequency
            fm[num] += count

            # Add new frequency if > 0
            if fm[num]:
                low.add((fm[num], num))

            # Move top x frequent elements to 'top'
            while len(top) < x and low:
                freq, key = low.pop(-1)
                curr += freq * key
                top.add((freq, key))

            # Balance: make sure all elements in top are more frequent (or larger) than in low
            while low and top and low[-1] > top[0]:
                freq, key = low.pop(-1)
                xfreq, xkey = top.pop(0)
                curr = curr - xfreq * xkey + freq * key
                low.add((xfreq, xkey))
                top.add((freq, key))

        # Sliding window
        for i in range(n):
            change(nums[i], 1)
            if i >= k:
                change(nums[i - k], -1)
            if i >= k - 1:
                res.append(curr)

        return res

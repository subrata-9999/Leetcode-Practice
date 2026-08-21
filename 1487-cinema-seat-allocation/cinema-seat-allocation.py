from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(set)

        for row, col in reservedSeats:
            rows[row].add(col)

        ans = (n - len(rows)) * 2

        for seats in rows.values():

            left = True
            for x in [2, 3, 4, 5]:
                if x in seats:
                    left = False

            right = True
            for x in [6, 7, 8, 9]:
                if x in seats:
                    right = False

            if left and right:
                ans += 2
            else:
                middle = True
                for x in [4, 5, 6, 7]:
                    if x in seats:
                        middle = False

                if left or right or middle:
                    ans += 1

        return ans
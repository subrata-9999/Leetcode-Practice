class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        unique_perms = set(itertools.permutations(digits, 3))
        even_numbers = [
            p for p in unique_perms
            if p[0] != 0          # Condition 1: Avoid starting with zero
            and p[-1] % 2 == 0    # Condition 2: Must be an even number (ends in 0, 2, 4, 6, 8)
        ]

        return len(even_numbers)
        
        
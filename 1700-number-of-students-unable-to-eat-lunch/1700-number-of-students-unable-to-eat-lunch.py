class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # tc: O(n) | sc: O(1)

        res = len(students)
        count = Counter(students)

        for sandwich in sandwiches:
            if count[sandwich] > 0:
                res -= 1
                count[sandwich] -= 1
            else:
                return res

        return res
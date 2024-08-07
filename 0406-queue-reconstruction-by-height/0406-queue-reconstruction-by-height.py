class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Greedy | tc: O(nlog n + n^2) | sc: O(n)

        # Sort by height (descending) and k (ascending)
        people.sort(key=lambda x: (-x[0], x[1]))
        que = []

        # Insert each person into the queue based on their k value
        for person in people:
            que.insert(person[1], person) # Insert person p at index p[1]

        return que

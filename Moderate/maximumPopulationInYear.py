class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        life_span = [0] * 101
        for birth,death in range(len(logs)):
            life_span[birth-1950] += 1
            life_span[death-1950] -= 1
        current_year = 0
        max_year = 0
        year = 0
        for i in range(101):
            if current_year > max_year:
                max_year = current_year
                year = i+1950
        return year

        
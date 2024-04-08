# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while sandwiches and students:
            possible = False
            for student in students:
                if student == sandwiches[0]:
                    possible = True
            if possible:
                if sandwiches[0] == students[0]:
                    sandwiches.pop(0)
                    students.pop(0)
                else:
                    s = students.pop(0)
                    students.append(s)
            else:
                break
        return len(sandwiches)

# 2nd/ optimal sln
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        pref = [0, 0]
        for student in students:
            pref[student] += 1
        
        for sandwich in sandwiches:
            if pref[sandwich] == 0:
                return sum(pref)
            pref[sandwich] -= 1 
        return 0

        

"""
Given a list of courses that a student needs to take to complete their major and a map of courses 
to their prerequisites, return a valid order for them to take their courses assuming they
only take one course for their major at once.

Could do topological sort or dfs
"""

from collections import deque


def prereqCourses(listOfCourses, courseMap):
    for course in listOfCourses:
        if course not in courseMap:
            courseMap[course] = []

    order = []
    path = set()
    visited = set()

    def dfs(co):
        # return if course has already been visited
        if co in path or co in visited:
            return

        visited.add(co)
        path.add(co)

        # visit prereq courses before adding the current course to the order
        for pre in courseMap[co]:
            dfs(pre)

        order.append(co)
        path.remove(co)

    for cour in listOfCourses:
        dfs(cour)

    return order



        

if __name__ == "__main__":
    listOfCourses =["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
    courseMap = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"]}
    print(prereqCourses(listOfCourses,courseMap))


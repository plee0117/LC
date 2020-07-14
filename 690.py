"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp = 0
        subs = {id}
        while subs:
            for emp in employees:
                if emp.id in subs:
                    imp += emp.importance
                    subs.remove(emp.id)
                    if emp.subordinates:
                        subs.update(emp.subordinates)
        return imp
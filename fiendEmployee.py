# Problem:
# You are given a small, unsorted list of employees 
# represented by their ID numbers. You need to write a function
# that performs a linear search to find an employee's ID. The function '
# 'should return the index of the employee if found and a special'
# ' value (like -1) if the employee's ID is not in the list.

def fiend_employee_id(employee_ids , targeted_id):

    for k in range(len(employee_ids)):
        if employee_ids[k]  == targeted_id:
            return k 
    return -1

if __name__ =="__main__":

    targeted_id = int(input())
    employee_ids =list(map(int ,input().split()))
    
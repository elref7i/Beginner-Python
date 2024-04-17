            #################### ( EX.1 ) ###############
"""
V1 = 1 #Local Scope


def fun1():
    V1 = 1     #Global Scope
    print(f"inside fun1 = {V1}")


fun1()
print(f"Outside fun1 = {V1}")

"""
'''           #################### ( EX.2 ) ###############
def fun1():
    V1 = 1  #Global Scope
    print(f"inside fun1 = {V1}")


fun1()
print(f"Outside fun1 = {V1}")  #error
'''

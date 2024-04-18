            #################### ( EX.1 ) ###############
"""
V1 = 1 #Global Scope


def fun1():
    V1 = 1     #Local Scope
    print(f"inside fun1 = {V1}")


fun1()
print(f"Outside fun1 = {V1}")

"""
            #################### ( EX.2 ) ###############
'''
V1 = 1 #Global Scope
def fun1():
    V1 = 1  #Local Scope
    V2 = 2  #Local Scope
    print(f"inside fun1 = {V1}")
    print(f"inside fun1 = {V2}")


fun1()
print(f"Outside fun1 = {V1}")
print(f"Outside fun1 = {V2}")  #error
'''


            #################### ( EX.3 ) ###############
'''
G= 2
def fun1 ():
    def fun2():
        V3 = 3
        print(G)
        print("V3")
    fun2()
# fun2() # fun2 is Local Scope
'''
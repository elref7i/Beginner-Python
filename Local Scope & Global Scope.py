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

'''
            #################### ( EX.4 ) ###############
name = 'Ahmed'
def fun():
    name = "Mohmaed"
    print(f"inside fun {name}")  #output ?
print(f'Outside fun {name}') # output ?
'''
'''
           #################### ( EX.5 ) ###############
G= 1  #Global
def fun():
    global G   ###Important
    G +=1
    print(f"inside fun {G}")  
print(f'Outside fun {G}')    
'''
#In other ways, example 5
'''
G= 1  #Global
def fun():
    print(f"inside fun {G}") # output = 1
    return G+1 ###

print(G)  # output = 1
G= fun()
print(f'Outside fun {G}')   #output = 2
'''
# Global Constant
pi = 3.14  # no change


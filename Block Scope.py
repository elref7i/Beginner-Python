 # Block Scope
'''
           ########### EX.1 ###########
V = 2
enemies = ['Skeleton','Zombie','Alien']
if V <5 :
    BL = enemies[0]   ## Block Scope
print(BL) # No error
'''
'''
 ########### EX.1 ###########
V = 2
def fun():
    enemies = ['Skeleton','Zombie','Alien']
    if V <5 :
        BL = enemies[0]   # Block Scope
    print(BL)  #NO error
fun()
print(BL) #  Error
'''


''' if you create a variable within an if block or a while loop or a for loop  
 or anything that has the indentation-->(   ) and the colon--> (:) that not local scope 
'''
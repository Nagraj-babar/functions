# Write a python program to multiply all the numbers in a list.
def f1(a):
    t=0
    i=0
    for b in a:
        if i==0:
            t=b
            i+=1
        else:
            t=t*b
    return print(t)        
o=[10,20,30]            
f1(o)            




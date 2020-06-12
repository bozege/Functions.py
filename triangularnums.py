#this function returns all of the triangular numbers including nth. 
def triangularnums(n):
    tri = []
    x = 0
    for i in range (1,n+1):
        for k in range (0,i+1):
            x += k
        tri.append(x)
        x = 0
    
    return tri


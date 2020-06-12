#This function returns the product of given parameters using karatsuba algorithm.

def karatsuba(n,m):

    strn = str(n)
    strm = str(m)

    if len(strn)%2 != 0:
        strn = "0" + strn
        
    if len(strm)%2 != 0:
        strm = "0" + strm
    
    nhalf1 = ""
    nhalf2 = ""
    mhalf1 = ""
    mhalf2 = ""
    A = 0
    B = 0
    C = 0
    
    for i in range (int(len(strn))):
        if len(nhalf1) < len(strn)/2:
            nhalf1 += strn[i]
        else:
            nhalf2 += strn[i]
            
    for i in range (int(len(strm))):
        if len(mhalf1) < len(strm)/2:
            mhalf1 += strm[i]
        else:
            mhalf2 += strm[i]
            
    A = (int(nhalf1)*int(mhalf1)) #* ((10**(int(len(nhalf1))))**2)
    B = (int(nhalf2)*int(mhalf2))       
    C = (int(nhalf1) + int(nhalf2)) * (int(mhalf1) + int(mhalf2))
    result = (A * ((10**(int(len(nhalf1))))**2)) + ((C - (A + B)) * (10**(int(len(nhalf1))))) + B
            
    return result
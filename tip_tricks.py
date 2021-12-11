#Collets Conjonctior

def oddeven(num):
    if (num % 2) == 0:  
        return True
    else:  
        return False

def start(num):
    colletsarray = []
    while num != 1:
        if num != 1:
            colletsarray.append(int(num))
            if oddeven(num) == True:
                num = num/2
            else:
                num = num*3+1
        else:
            break
    print(colletsarray)
    print("\n\nFalse Once Again")
    
if __name__ == "__main__":
    start(295147905179352825857)
        
        
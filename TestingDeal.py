v=0
def pert(n):
    global v
    if len(str(n))==1:
        #print(n)
        v=0
        return "DONE"
    
    digits = [int(i) for i in str(n)]

    result = 1 
    for j in digits:
        result *= j
    v+=1
    print(result," times: ",v)
    pert(result)

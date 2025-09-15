
def linear_search(k , li):
    
    for i in range(len(li)):
        if li[i]  == k:
            return i 
    
    return -1 

if __name__ =="__main__":
    k =int(input())
    li =list(map(int,input().split()))
    print(linear_search(k,li))

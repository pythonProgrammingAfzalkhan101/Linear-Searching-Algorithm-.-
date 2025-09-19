
def linear_search(li , size , key):
    
    if size == 0 :
        return -1 
    elif li[0] == key:
        return 0 
    elif li[size-1] == key:
        return size -1 
    
    else:
        return linear_search(li ,size-1 , key)

if __name__ =="__main__":
    li = [1,2,3,4,5]
    size = 5 
    key = 10 
    print(linear_search(li , size , key))

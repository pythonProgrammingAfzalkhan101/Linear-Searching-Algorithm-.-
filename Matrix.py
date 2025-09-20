def linear_search_with_matrix(matrix , row , col , key ):

    for i in range(len(row)):
        for j in range(len(col)):
            if matrix[i][j] == key:
                return (i , j)
    
    return -1 

if __name__ =="__main__":

    row =int(input())
    col =int(input())
    matirx  = []
    key =int(input())
    
    for i in range(row):
        add_value =list(map(int,input().split()))
        matirx.append(add_value)
    print(linear_search_with_matrix(matirx , row , col , key))


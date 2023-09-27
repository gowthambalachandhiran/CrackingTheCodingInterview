def foo(array):
    sum = 0
    product = 1
    for i in range(len(array)):
        sum += array[i]
    for i in range(len(array)):
        product *= array[i]
    
    print(str(sum)+" "+str(product))
    
    
##This take only o(n) iteration no matter two loops

foo([1,2,3,4,5])



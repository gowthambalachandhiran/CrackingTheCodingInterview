def swap_without_temp(a,b):
    print("Before swap:",(a,b))
    a ^= b
    b ^= a
    a ^= b
    print("After swap:",(a,b))
    
    
print(swap_without_temp(3,9))


def swap_without_temp_another_method(a,b):
    print("Before swap:",(a,b))
    a = a + b
    b  = a - b
    a = a - b
    print("After swap:",(a,b))
    
    

print("\n")
print(swap_without_temp_another_method(3,9))

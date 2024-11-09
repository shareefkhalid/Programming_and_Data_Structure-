my_list =[7 , 1.2 ,'A', 6 , True]
x = 0
def safe_print_list(my_list=[],x=0):
    count = 0
    
    
    try:
        for i in range(x):
            print(my_list[i],end="")
            count +=1
    except IndexError:
        pass
    finally:
        print()
        return count

print(f"item nuber{safe_print_list(my_list,x=3)}")


   






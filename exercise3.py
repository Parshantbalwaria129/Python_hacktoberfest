#code with harry guess the no. exercise
print("guess the number")
count=9

while (count<=9):
    num=int(input("enter a number= "))
        
    if num>18:
        print("try a smaller number")
    
    elif num<18:
        print("try a greater number")
    
    else:
        print("you win")
        break
    count=count-1
    print("no. of chances left", count)
    if count==0:
        print("game over")
        break
        
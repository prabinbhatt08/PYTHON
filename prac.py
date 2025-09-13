#nums = (1, 4, 9, 25, 36, 49, 64, 81, 100)

#x=81
#i=0
#while i<len(nums):
    #if(nums[i]== x):
        #print("Fount at idx", i)
    #i += 1


names = ("Prabin", "Yogesh","Surendra","Sandhya", "Gaurav", "Bikash")
  
x = "Gaurav"

i = 1 #iteration
while i<len(names):
    if(names[i] == x):
        print("Found at index: ",i)
        break
    else:
        print("Not found at index")
        i += 1

print("End of loop")
      





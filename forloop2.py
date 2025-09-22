list = [1, 4, 9, 25, 36, 49, 64, 81, 100]

x = 9

idx = 0
for nums in list:
    if(nums == x):
        print("Number found at idx: ", idx)
    idx += 1
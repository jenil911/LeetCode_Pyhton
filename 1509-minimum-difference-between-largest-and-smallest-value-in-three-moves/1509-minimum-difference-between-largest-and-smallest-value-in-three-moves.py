def minDifference(nums):
    if len(nums) <= 4:
        return 0
    nums.sort()
    #mi = float("inf") 
    return min(
        nums[-1] - nums[3],  # Remove the three smallest elements
        nums[-2] - nums[2],  # Remove the two smallest and one largest element
        nums[-3] - nums[1],  # Remove the one smallest and two largest elements
        nums[-4] - nums[0]   # Remove the three largest elements
    )

f = open('user.out','w')
for i in map(loads,stdin):
    f.write(f'{minDifference(i)}\n') 
f.flush()
exit(0)
        
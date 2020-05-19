def main():
    nums = [3,7,2,5,1]
    print(nums)
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                change = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = change
    print(nums)
if __name__ == '__main__':
    main()
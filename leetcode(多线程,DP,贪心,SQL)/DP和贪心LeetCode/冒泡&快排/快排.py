def quick_sort(nums, start, end):
     if start <= end:
         key = nums[start]
         i = start
         j = end
         while i < j:
             while i < j and key <= nums[j]:
                 j -= 1
             nums[i] = nums[j]
             while i < j and nums[i] <= key:
                 i += 1
             nums[j] = nums[i]
         nums[i] = key
         quick_sort(nums, start, i - 1)
         quick_sort(nums, i + 1, end)

def main():
    nums = [7, 4, 3, 9, 2]
    quick_sort(nums, 0, len(nums)-1)
    print(nums)

if __name__ == '__main__':
    main()
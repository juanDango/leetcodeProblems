def print_menu_two_pointers():
    print("Ejercicios de two pointers seleccione uno: ")
    print("125. Valid Palindrome")
    print("167. Two Sum II - Input Array Is Sorted")
    print("15. 3Sum")
    print("11. Container With Most Water")

    entrada = input("Seleccione el número de problema: ")
    if entrada == "125":
        isPalindrome_menu()
    if entrada == "167":
        twoSum_menu()
    if entrada == "15":
        threeSum_menu()
    if entrada == "11":
        maxArea_menu()

def isPalindrome_menu():
    string = input("Ingrese el string a verificar: ")

    print("SI" if isPalindrome(string) else "NO")

def isPalindrome(s):
    """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

        Given a string s, return true if it is a palindrome, or false otherwise.

        

        Example 1:

        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.
        Example 2:

        Input: s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.
        Example 3:

        Input: s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric characters.
        Since an empty string reads the same forward and backward, it is a palindrome.
        

        Constraints:

        1 <= s.length <= 2 * 105
        s consists only of printable ASCII characters.
    """
    s = s.lower()
    mod_s = [i for i in s if i.isalnum()]
    L, R = 0, len(mod_s) - 1
    while L < R:
        if mod_s[L] != mod_s[R]:
            return False
        L += 1
        R -= 1
    return True

def twoSum_menu():
    s = input("Inserte los numeros separados por coma: ")

    array = [int(i.strip()) for i in s.split(",")]
    t = int(input("Ingrese el target: "))
    print(twoSum(sorted(array), t))

def twoSum(numbers, target):
    """
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        Your solution must use only constant extra space.

        

        Example 1:

        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
        Example 2:

        Input: numbers = [2,3,4], target = 6
        Output: [1,3]
        Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
        Example 3:

        Input: numbers = [-1,0], target = -1
        Output: [1,2]
        Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
        

        Constraints:

        2 <= numbers.length <= 3 * 104
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.
    """
    L, R = 0, len(numbers) - 1
    while L < R:
        suma = numbers[L] + numbers[R]
        if suma > target:
            R -= 1
        elif suma < target:
            L += 1
        else:
            return [L + 1, R + 1]
        

def threeSum_menu():
    s = input("Inserte los numeros separados por coma: ")

    array = [int(i.strip()) for i in s.split(",")]
    print(threeSum(array))

def threeSum(nums):
    """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        

        Example 1:

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.
        Example 2:

        Input: nums = [0,1,1]
        Output: []
        Explanation: The only possible triplet does not sum up to 0.
        Example 3:

        Input: nums = [0,0,0]
        Output: [[0,0,0]]
        Explanation: The only possible triplet sums up to 0.
        

        Constraints:

        3 <= nums.length <= 3000
        -105 <= nums[i] <= 105
    """
    ret = set()

    d = {n: i for i, n in enumerate(nums)}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            z = -(nums[i]+nums[j])
            if z in d and d[z] != i and d[z] != j:
                pair = tuple(sorted([nums[i], nums[j], z]))
                ret.add(pair)

    return ret

def maxArea_menu():
    s = input("Inserte los numeros separados por coma: ")

    array = [int(i.strip()) for i in s.split(",")]
    print(maxArea(array))

def maxArea(height):
    """
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.
        
        Example 1:

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
        Example 2:

        Input: height = [1,1]
        Output: 1
        

        Constraints:

        n == height.length
        2 <= n <= 105
        0 <= height[i] <= 104
    """
    L, R = 0, len(height) - 1

    max_vol = 0
    while L < R:
        h = min(height[L], height[R])
        w = R - L
        vol = h*w
        max_vol = vol if vol>max_vol else max_vol

        if height[L] > height[R]:
            R -= 1
        else:
            L += 1
    return max_vol
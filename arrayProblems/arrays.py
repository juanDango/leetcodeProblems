def print_menu_arrays():
    print("Ejercicios de arrays y strings seleccione uno: ")
    print("217. Contains Duplicate")
    print("242. Valid Anagram")
    print("1. Two sum")
    print("49. Group Anagrams")
    print("347. Top K Frequent")
    print("238. Product except self")

    entrada = input("Seleccione el número de problema: ")
    if entrada == "217":
        contains_duplicate_menu()
    if entrada == "242":
        is_anagram_menu()
    if entrada == "1":
        two_sum_menu()
    if entrada == "49":
        groupAnagrams_menu()
    if entrada == "347":
        tokK_menu()
    if entrada == "238":
        productExceptSelf_menu()

#Todo lo relacionado con contains duplicate
def contains_duplicate_menu():
    print("Inserte el array (por ejemplo 1, 2, 5, 7) separados por , ")
    numeros = input()
    entrada = [int(num.strip()) for num in numeros.split(",")] 
    print(contains_duplicate(entrada))
    
def contains_duplicate(nums: list) -> bool:
        """
            Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

            

            Example 1:

            Input: nums = [1,2,3,1]
            Output: true
            Example 2:

            Input: nums = [1,2,3,4]
            Output: false
            Example 3:

            Input: nums = [1,1,1,3,3,4,3,2,4,2]
            Output: true
            

            Constraints:

            1 <= nums.length <= 105
            -109 <= nums[i] <= 109
        """
        appearences = set()
        for num in nums:
            if num in appearences:
                return True
            else:
                appearences.add(num)
        return False

#Is anagram problem
def is_anagram_menu():
    s = input("Inserte el string 1: ")
    t = input("Inserte el string 2: ")
    print(is_anagram(s, t))


def is_anagram(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false
    

    Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
    """
    if len(s) != len(t):
        return False
    t_count = {}
    s_count = {}
    for l in t:
        t_count[l] = t_count.get(l, 0) + 1
        
    for l in s:
        s_count[l] = s_count.get(l, 0) + 1
        
    for k, v in t_count.items():
        if s_count.get(k, 0) != v:
            return False
        
    return True

#Two sum problem
def two_sum_menu():
    s = input("Inserte los numeros separados por coma: ")

    array = [int(i.strip()) for i in s.split(",")]
    t = int(input("Ingrese el target: "))
    print(twoSum(array, t))

def twoSum(nums, target):
    """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.

        

        Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
        Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
        Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]
        

        Constraints:

        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.
        

        Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
    """
    values = {}
    for i, num in enumerate(nums):
        subs = target-num
        if subs in values:
            return [i, values[subs]]
        else:
            values[num] = i

#Group anagrams

def groupAnagrams_menu():
    s = input("Ponga las palabras minusculas separadas por coma: ")
    array = [i.strip() for i in s.split(",")]

    print(groupAnagrams(array))
def groupAnagrams(strs):
    """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

        

        Example 1:

        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        Example 2:

        Input: strs = [""]
        Output: [[""]]
        Example 3:

        Input: strs = ["a"]
        Output: [["a"]]
        

        Constraints:

        1 <= strs.length <= 104
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.
    """
    anagrams = {}
    for stri in strs:
        d = [0] * 26
        for char in stri:
            d[ord(char) - ord("a")] += 1
            
        elems = tuple(d)
        if elems in anagrams:
            anagrams[elems].append(stri)
        else:
            anagrams[elems] = [stri]
    return list(anagrams.values())

#Top K Elements
def tokK_menu():
    s = input("Inserte los numeros separados por coma: ")

    array = [int(i.strip()) for i in s.split(",")]
    t = int(input("El top K que desea: "))
    print(topKFrequent(array, t))

def topKFrequent(nums, k):
    """
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

        

        Example 1:

        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        Example 2:

        Input: nums = [1], k = 1
        Output: [1]
        

        Constraints:

        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.
        

        Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    """
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    c = [[] for i in range(len(nums) + 1)]
    for key, value in counts.items():
        c[value].append(key)
    ret = []
    for i in reversed(c):
        if i != []:
            ret = ret + i
        if len(ret) == k:
            return ret
        
#Product except self
def productExceptSelf_menu():
    s = input("Inserte los numeros separados por coma: ")

    array = [int(i.strip()) for i in s.split(",")]
    print(productExceptSelf(array))

def productExceptSelf(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    

    Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    

    Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
    """
    ret = [1] * len(nums)
    for i in range(1, len(nums)):
        ret[i] = ret[i-1] * nums[i-1]
    post = 1
    for i in range(len(nums)-1, -1, -1):
        ret[i] *= post
        post *= nums[i]
        print(post, i)
    return ret
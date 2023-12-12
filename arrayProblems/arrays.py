def print_menu_arrays():
    print("Ejercicios de arrays y strings seleccione uno: ")
    print("217. Contains Duplicate")
    print("242. Valid Anagram")
    print("1. Two sum")
    print("49. Group Anagrams")

    entrada = input("Seleccione el número de problema: ")
    if entrada == "217":
        contains_duplicate_menu()
    if entrada == "242":
        is_anagram_menu()
    if entrada == "1":
        two_sum_menu()
    if entrada == "49":
        groupAnagrams_menu()

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
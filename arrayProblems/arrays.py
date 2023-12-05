def print_menu_arrays():
    print("Ejercicios de arrays y strings seleccione uno: ")
    print("217. Contains Duplicate")
    print("242. Valid Anagram")

    entrada = input("Seleccione el número de problema: ")
    if entrada == "217":
        contains_duplicate_menu()
    if entrada == "242":
        is_anagram_menu()

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
        if l in t_count:
            t_count[l] = t_count[l] + 1
        else:
            t_count[l] = 1
        
    for l in s:
        if l in s_count:
            s_count[l] = s_count[l] + 1
        else:
            s_count[l] = 1
        
    for k, v in t_count.items():
        if s_count.get(k, 0) != v:
            return False
        
    return True
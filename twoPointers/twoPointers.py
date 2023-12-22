def print_menu_two_pointers():
    print("Ejercicios de two pointers seleccione uno: ")
    print("125. Valid Palindrome")

    entrada = input("Seleccione el número de problema: ")
    if entrada == "125":
        isPalindrome_menu()

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
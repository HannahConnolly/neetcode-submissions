class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) < 2:
            return True

        left_ptr, right_ptr = 0, len(s) - 1
        while left_ptr < right_ptr:

            while left_ptr < right_ptr and not s[left_ptr].isalnum():
                left_ptr += 1
    
            while left_ptr < right_ptr and not s[right_ptr].isalnum():
                right_ptr -= 1
                
            if(s[left_ptr].lower() != s[right_ptr].lower()):
                print(s[left_ptr].lower(), s[right_ptr].lower())
                return False

            right_ptr -= 1
            left_ptr += 1
    
        return True        
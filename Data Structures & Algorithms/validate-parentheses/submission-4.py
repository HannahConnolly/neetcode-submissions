class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        open_paren = ('{','(','[')
        paren_pair = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        for ch in s:
            print(ch)

            if ch in open_paren:
                stack.append(ch)

            elif not stack or stack.pop() != paren_pair[ch]:
                    return False

        return len(stack) == 0
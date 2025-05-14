class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # dicts ={ '{':'}',}
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack:
                    return False
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False

        return not stack

        
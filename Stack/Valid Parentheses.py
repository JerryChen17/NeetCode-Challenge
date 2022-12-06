class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        symbolMap = {")" : "(", "]" : "[", "}": "{"}
        empStack = []

        for i in range(len(s)):
            if s[i] in symbolMap:
                if len(empStack) > 0:
                    if empStack[-1] == symbolMap[s[i]]:
                        empStack.pop()
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                empStack.append(s[i])
        
        #check if all brackes are closed
        if len(empStack) == 0:
            return True
        else:
            return False
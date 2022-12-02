class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {} #create empty hash map
        
        #record the character in s with hash map
        for i in range(len(s)):
            strKey = str(s[i])
            if strKey not in hashMap:
                hashMap[strKey] = 1
                continue
            else:
                hashMap[strKey] += 1
        #examine the character in t with the hash map
        for j in range(len(t)):
            strKey = str(t[j])
            if strKey not in hashMap: #character not exist in s
                return False
            else:
                hashMap[strKey] -= 1
                if hashMap[strKey] < 0: #the number of this character used in s is more than t
                    return False
        #make sure the length of s and t are the same
        if i == j:
            return True
        else:
            return False
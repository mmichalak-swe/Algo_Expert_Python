# O(n + m) time | O(m) space, where n is the len of s, m is the len of t
def minWindow(s, t):
        t_dict = {}
        have_dict = {}
        
        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)
            have_dict[char] = 0
        
        have, need = 0, len(t_dict)

        left, right = 0, 0
        output = [float('-inf'), float('inf')]
        
        while right < len(s) + 1:
            if have != need:
                if right == len(s):
                    break
                letter = s[right]
                if letter in have_dict:
                    have_dict[letter] += 1
                    if have_dict[letter] == t_dict[letter]:
                        have += 1
                right += 1
            else:
                letter = s[left]
                if letter in have_dict:
                    have_dict[letter] -= 1
                    if have_dict[letter] < t_dict[letter]:
                        have -= 1
                left += 1
            
            if have == need:
                if right - left < output[1] - output[0]:
                        output = [left, right]


        if output == [float('-inf'), float('inf')]:
            return ""
        else:
            return s[output[0]:output[1]]

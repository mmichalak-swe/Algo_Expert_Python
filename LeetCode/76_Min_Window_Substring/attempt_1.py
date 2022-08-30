def minWindow(s, t):
        t_dict = {}
        have_dict = {}
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1

            have_dict[char] = 0
        
        need = len(t_dict)
        have = 0

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

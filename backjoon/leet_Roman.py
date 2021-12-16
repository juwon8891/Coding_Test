class Solution:
    def romanToInt(s: str) -> int:
        symbol_map = {'M': 1000,
                      'CM': 900,
                      'D': 500,                    
                      'CD': 400,
                      'C': 100,
                      'XC': 90,
                      'L': 50,
                      'XL': 40,
                      'X': 10,
                      'IX': 9,
                      'V': 5,
                      'IV': 4,
                      'I': 1
                     }
        
        result = 0
        
        # to track the index of the character in the string 's' 
        i = 0
        
        while i < len(s)-1:
            if (s[i] + s[i+1]) in symbol_map:  # in the case of 'CM', 'CD', 'XC', 'XL', 'IX', and 'IV'
                result += symbol_map[s[i] + s[i+1]]
                i += 2
            else:
                result += symbol_map[s[i]]
                i += 1
        
		# check whether the integer value of the last character of the string 's' is reflected on the 'result'
        if i == len(s):  # that means the last two characters combined refer to a single integer i.e. IV = 4 
            return result
        else: # the last character has not been considered on the loop
            return result + symbol_map[s[len(s)-1]]
print(Solution.romanToInt("VIIXI"))
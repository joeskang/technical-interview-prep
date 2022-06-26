class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s[::-1]
        s = s.replace('-','')
        output_string = ''
        for i in range(len(s)):
            output_string += s[i].upper()
            if (i+1) % k == 0 and i < len(s) - 1:
                output_string += '-'
                
        return output_string[::-1]
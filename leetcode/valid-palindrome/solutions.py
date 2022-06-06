class Solution(object):
    def isPalindrom(self, s:str)-> bool:
        #remove non number/letter and uppercase/lowercase
        s_aux = ''.join(x for x in s if x.isalnum())
        s_aux = s_aux.lower()
        for i in range(int(len(s_aux)/2)):
            if s_aux[i] != s_aux[-(i+1)]:
                return False
        return True
            

examples = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " ",
    "Sit on a potato pan, Otis",
    "Madam, I'm Adam",
    "Able was I, ere I saw Elba"
]

sol = Solution()

for x in examples:
    print(sol.isPalindrom(x))
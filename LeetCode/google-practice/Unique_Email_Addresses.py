"""
date: 06/23/2022
time: 00:09:58

"""

class List(list):
    def __init__(self):
        super()


class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        myd = {}

        for email in emails:
            local_name, domain_name = email.split('@')

            local_name = local_name.replace('.', '')
            local_name = local_name.split('+')[0]
            name = local_name + '@' + domain_name

            if name not in myd:
                myd[name] = True


        return len(myd.keys())
            

            
if __name__ == '__main__':
    sol = Solution()
    input_ = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(sol.numUniqueEmails(input_))

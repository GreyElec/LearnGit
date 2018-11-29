class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        Count = dict()
        for obj in cpdomains:
            times, domain = obj.split()
            if domain in Count:
                Count[domain] += int(times)
            else:
                Count[domain] = int(times)
            sub_domain = '.'.join(domain.split('.')[1:])
            while sub_domain:
                if sub_domain in Count:
                    Count[sub_domain] += int(times)
                else:
                    Count[sub_domain] = int(times)
                sub_domain = '.'.join(sub_domain.split('.')[1:])
        res = []
        for obj in Count:
            res.append('{} {}'.format(str(Count[obj]), obj))
        return res


test_case_1 = ["9001 discuss.leetcode.com"]
test_case_2 = [
    "900 google.mail.com",
    "50 yahoo.com",
    "1 intel.mail.com",
    "5 wiki.org"]
S = Solution()
print(S.subdomainVisits(test_case_1))

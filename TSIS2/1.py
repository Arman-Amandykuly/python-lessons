import re
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = re.sub("\.",r"[.]",address)
        return address
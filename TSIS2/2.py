import re
class Solution:
    def interpret(self, command: str) -> str:
        command = re.sub("\(\)","o",re.sub("\(al\)","al",command))
        return command
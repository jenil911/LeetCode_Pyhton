class Solution:
    def isNumber(self, s: str) -> bool:
		#Example:               +-     1 or 1. or 1.2 or .2   e or E +- 1     
        engine = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$")
        return engine.match(s.strip(" ")) # i prefer this over putting more things (\S*) in regex
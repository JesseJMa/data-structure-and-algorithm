def isValid(self, s: str) -> bool:
    
    '''
        "()"
        "()[]{}"
        "(]"
        "([)]"
    '''
    stack = []
    dic = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    for char in s:
        if char in dic:
            topEle = stack.pop() if stack else '#'
            
            if dic[char] != topEle:
                return False
        else:
            stack.append(char)
        
     return not stack   
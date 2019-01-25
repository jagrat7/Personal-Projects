from  collections import deque

"""
Input: x
x may contain a repeating pattern.
If it does, extract the pattern.
e.g. x = abcabcabc, Output: abc
return False otherwise
"""
def has_pattern(x):
    que = deque()
    for incoming in x:
        if que and que[0] == incoming:
            que.popleft()
        que.append(incoming)
    if que:
        return ''.join(que)
    return False,"no pattern"
       



inp = 'aaaaa'
print(has_pattern(inp)) # True, a

inp = 'abcabc'
print(has_pattern(inp)) # True, abc
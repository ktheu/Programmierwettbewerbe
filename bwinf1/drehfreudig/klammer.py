def klammernToGraph(s):
    G = {x:[] for x in range(1,len(s)//2 + 1)}         
    stack = []      
    zaehl = 0      
    for c in s:
        if c == '(':
            zaehl += 1
            if stack:     # wenn nicht die Wurzel betrachtet wird
                parent = stack[-1]              
                G[parent].append(zaehl)
            stack.append(zaehl)
        elif c == ')':
            stack.pop()
    return G

s = "((())(()()))"
s = '(()())'
print(klammernToGraph(s))
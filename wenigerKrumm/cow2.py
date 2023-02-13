
 

def nextstates(state):
    if len(state) == 0:
        return []
    tmp = []
    tmp.append(state[1:])
    tmp.append(state[:-1])
    if 'M' == state[0]:
        tmp.append('O' + state[1:])
    else:
        tmp.append('M' + state[1:])
    if 'M' == state[-1]:
        tmp.append(state[:-1] + 'O')
    else:
        tmp.append(state[:-1] + 'M')
    return tmp


from collections import deque
def bfs(startstate):
    global zaehl
    frontier =  deque([(startstate,0)])
    visited = set(startstate)
     
    while frontier:
        state, ebene = frontier.popleft()
        visited.add(state)
    
        if state == 'MOO':
            return ebene
        for v in nextstates(state):
            if v not in visited:
                 
                frontier.append((v,ebene+1))

    return -1


N = int(input())
for i in range(N):
    s = input()
    print(bfs(s))

 
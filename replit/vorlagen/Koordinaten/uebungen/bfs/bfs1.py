'''
Traversieren eines Baumes mit bfs
'''


from collections import deque
def bfs(s):
    frontier =  deque([s])
    while frontier:
        state = frontier.popleft()
        print(state)
        for v in nextstates(state):
            frontier.append(v)
             
def nextstates(k):
    if k > 14: return []
    return [2*k+1, 2*k+2]


bfs(0)







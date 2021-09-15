# append() :- This function is used to insert the value in its argument to the right end of deque.
# appendleft() :- This function is used to insert the value in its argument to the left end of deque.
#  pop() :- This function is used to delete an argument from the RIGHT END of deque.
#  popleft() :- This function is used to delete an argument from the left end of deque.

import collections

def empty(q):
    return not q

q = collections.deque()
q.append(1)
print(q)
q.appendleft(2)
print(q)
q.pop()
#print(q)
q.pop()
print(q)

if len(q) == 0:
    print("pusta")
else:
    print("nie")
if empty(q):
    print("pusta")
else:
    print("nie pusta")
import random

class Node:
    def __init__(self, value):
        self.y = random.randint(0, 1 << 31)
        self.size = 1
        self.x = value
        self.l = None
        self.r = None

def new_node(value):
    res = Node(value)
    return res

def get_size(t):
    return t.size if t else 0

def update_size(t):
    if t:
        t.size = 1 + get_size(t.l) + get_size(t.r)

def merge(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    if t1.y > t2.y:
        t1.r = merge(t1.r, t2)
        update_size(t1)
        return t1
    else:
        t2.l = merge(t1, t2.l)
        update_size(t2)
        return t2

def split(t, x):
    if not t:
        return None, None
    if get_size(t.l) < x:
        t.r, t2 = split(t.r, x - get_size(t.l) - 1)
        update_size(t)
        return t, t2
    else:
        t1, t.l = split(t.l, x)
        update_size(t)
        return t1, t

def build(v):
    result = None
    for i in range(len(v)):
        result = merge(result, new_node(v[i]))
    return result

def to_start(t, l, r):
    t1, t2 = split(t, r + 1)
    t3, t4 = split(t1, l)
    return merge(merge(t4, t3), t2)

def print_tree(t):
    if not t:
        return
    print_tree(t.l)
    print(t.x, end=" ")
    print_tree(t.r)

def main():
    n, m = map(int, input().split())
    a = list(range(1, n + 1))
    t = build(a)
    for i in range(m):
        l, r = map(int, input().split())
        t = to_start(t, l - 1, r - 1)
    print_tree(t)

if __name__ == "__main__":
    main()
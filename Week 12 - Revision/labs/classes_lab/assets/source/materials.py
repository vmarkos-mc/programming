class A:
    def __init__(self, n):
        self.n = n

    def __eq__(self, __other):
        if not isinstance(__other, A):
            return False
        return self.n == __other.n

class B(A):
    def __init__(self, n):
        self.n = n

if __name__ == "__main__":
    x = A(1)
    y = A(2)
    print(f"Are x and y equal? {x == y}")
    y.n = 1
    print(f"Are x and y equal now? {x == y}")
    u = B(1)
    v = B(1)
    print(f"Are u and v equal? {u == v}")
    w = A(1)
    print(f"Are u and w equal? {u == w}")
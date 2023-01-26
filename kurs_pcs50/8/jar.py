class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("There's not so many cookies! :(")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies!")
        self._size -= n

    @property
    def capacity(self, ):
        return self._capacity

    @property
    def size(self, ):
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()
    
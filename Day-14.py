class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maxDiff = 0
        arr = self.__elements
        max = 0
        for i in range(len(arr)):
            if arr[i] > max:
                max = arr[i]
        min = max
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
        maxDiff = max-min
        self.maximumDifference = maxDiff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
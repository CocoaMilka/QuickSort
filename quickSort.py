class QuickSortAlgorithm:

    array = []

    def __init__(self, a):
        self.array = a

    def Partition(self, p, r):
        x = self.array[r]
        i = p - 1

        for j in range(p, r):
            if self.array[j] <= x:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[r] = self.array[r], self.array[i + 1]

        return i + 1

    def QuickSort(self, p, r):
        if p < r:
            q = self.Partition(p, r)
            self.QuickSort(p, q - 1)
            self.QuickSort(q + 1, r)

    def printArray(self):

        for i in self.array:
            print(i)

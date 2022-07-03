### Optimal Solution
### O(log(n)) time | O(n) space, where n is the # of inserted #s
class ContinuousMedianHandler:
    def __init__(self):
        self.lowerHalf = Heap(MAX_HEAP_FUNC, [])
        self.upperHalf = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    def insert(self, number):
        if not self.lowerHalf.length or number < self.lowerHalf.peek():
            self.lowerHalf.insert(number)
        else:
            self.upperHalf.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if self.lowerHalf.length - self.upperHalf.length == 2:
            self.upperHalf.insert(self.lowers.remove())
        elif self.upperHalf.length - self.lowerHalf.length == 2:
            self.lowerHalf.insert(self.upperHalf.remove())

    def updateMedian(self):
        if self.lowerHalf.length == self.upperHalf.length:
            self.median = (self.lowerHalf.peek() + self.upperHalf.peek()) / 2
        elif self.lowerHalf.length > self.upperHalf.length:
            self.median = self.lowerHalf.peek()
        else:
            self.median = self.upperHalf.peek()

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, comparisonFunc, array):
        self.heap = self.buildHeap(array)
        self.comparisonFunc = comparisonFunc
        self.length = len(self.heap)

    # O(n) time, start at parent nodes and call sift down | O(1) space
    def buildHeap(self, array):
        firstParent = (len(array) - 2) // 2
        for idx in range(firstParent, -1, -1):
            self.siftDown(idx, array)
        return array

    # O(log(n)) time | O(1) space, every time node is swapped, half of tree eliminated
    def siftDown(self, currIdx, heap):
        cOne = self.childOne(currIdx, heap)
        cTwo = self.childTwo(currIdx, heap)
        while cOne is not None or cTwo is not None:
            if cTwo is not None:
                if self.comparisonFunc(heap[cTwo], heap[cOne]):
                    idxToSwap = cTwo
                else:
                    idxToSwap = cOne
            else:
                idxToSwap = cOne

            if self.comparisonFunc(heap[idxToSwap], heap[currIdx]):
                self.swap(currIdx, idxToSwap, heap)
                currIdx = idxToSwap
                cOne = self.childOne(currIdx, heap)
                cTwo = self.childTwo(currIdx, heap)
            else:
                break

    # O(log(n)) time | O(1) space, every time node is swapped, half of tree eliminated
    def siftUp(self, currIdx, heap):
        parentIdx = self.getParent(currIdx)
        while currIdx > 0:
            if self.comparisonFunc(heap[currIdx], heap[parentIdx]):
                self.swap(currIdx, parentIdx, heap)
                currIdx = parentIdx
                parentIdx = self.getParent(currIdx)
            else:
                break

    # O(1) time
    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, -1, self.heap)
        output = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.heap)
        return output

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, idx1, idx2, heap):
        heap[idx1], heap[idx2] = heap[idx2], heap[idx1]

    def childOne(self, idx, heap):
        output = (2*idx + 1)
        return output if output < len(heap) else None

    def childTwo(self, idx, heap):
        output = (2*idx + 2)
        return output if output < len(heap) else None

    def getParent(self, idx):
        return ((idx-1) // 2)


def MAX_HEAP_FUNC(a, b):
    return a > b


def MIN_HEAP_FUNC(a, b):
    return a < b

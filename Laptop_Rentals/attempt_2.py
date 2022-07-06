# O(n*log(n)) time | O(n) space, n log n comes from possibly needing to insert n items
# to the min Heap, and each insertion takes log(n) time
def laptopRentals(times):
    if len(times) == 0:
        return 0

    times.sort(key=lambda x: x[0])

    heap = MinHeap([times[0]])

    for i in range(1, len(times)):
        interval = times[i]
        if heap.peek()[1] <= interval[0]:
            heap.remove()

        heap.insert(interval)
    
    return heap.getLength()


class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def getLength(self):
        return len(self.heap)

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
            try:
                idxToSwap = cOne if heap[cOne][1] < heap[cTwo][1] else cTwo
            except:
                idxToSwap = cOne if cTwo is None else cTwo

            if heap[idxToSwap][1] < heap[currIdx][1]:
                self.swap(currIdx, idxToSwap, heap)
                currIdx = idxToSwap
                cOne = self.childOne(currIdx, heap)
                cTwo = self.childTwo(currIdx, heap)
            else:
                break

    # O(log(n)) time | O(1) space, every time node is swapped, half of tree eliminated
    def siftUp(self, currIdx, heap):
        parentIdx = self.getParent(currIdx)
        while currIdx > 0 and heap[currIdx][1] < heap[parentIdx][1]:
            self.swap(currIdx, parentIdx, heap)
            currIdx = parentIdx
            parentIdx = self.getParent(currIdx)

    # O(1) time
    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, -1, self.heap)
        output = self.heap.pop()
        self.siftDown(0, self.heap)
        return output

    def insert(self, value):
        self.heap.append(value)
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

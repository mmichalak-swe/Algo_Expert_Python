# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(n) time, start at parent nodes and call sift down | O(1) space
    def buildHeap(self, array):
        firstParent = (len(array) - 2) // 2
        for idx in range(firstParent, -1, -1):
            self.siftDown(idx, array)
        return array

    # O(log(n)) time | O(1) space, every time node is swapped, half of tree eliminated
    def siftDown(self, currIdx, heap):
        cOneIdx = self.childOne(currIdx, heap)
        cTwoIdx = self.childTwo(currIdx, heap)
        while cOneIdx is not None or cTwoIdx is not None:
            try:
                idxToSwap = cOneIdx if heap[cOneIdx] < heap[cTwoIdx] else cTwoIdx
            except:
                idxToSwap = cOneIdx if cTwoIdx is None else cTwoIdx

            if heap[idxToSwap] < heap[currIdx]:
                self.swap(currIdx, idxToSwap, heap)
                currIdx = idxToSwap
                cOneIdx = self.childOne(currIdx, heap)
                cTwoIdx = self.childTwo(currIdx, heap)
            else:
                break

    # O(log(n)) time | O(1) space, every time node is swapped, half of tree eliminated
    def siftUp(self, currIdx, heap):
        parentIdx = self.getParent(currIdx)
        while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
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

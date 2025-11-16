# https://leetcode.com/problems/sort-an-array/?envType=problem-list-v2&envId=heap-priority-queue
from heapq import heapify
from typing import List


class Solution:
    # O(nlog(n)) time complexity
    # Without using any built-in functions

    def swap(self, arr:List[int], i:int, j:int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    # MaxHeap, A max-heap gives the largest element first.
    def heap_insert(self, arr: List[int], i:int):
        while i>0 and arr[(i-1)//2] < arr[i]:
            self.swap(arr, (i-1)//2, i)
            i = (i-1)//2

    def heapify(self, arr: List[int], i:int, size:int):
        l= i*2 + 1
        while l<size:
            best = l+1 if l+1 <size and arr[l]<arr[l+1] else l # MinHeap, Choose the smaller one
            if arr[best] > arr[i]:
                self.swap(arr, best, i)
                i=best
                l=i*2+1
            else: break

    # 1015 ms Beats 6.49%
    def sortArray1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            self.heap_insert(nums, i)
        for i in range(n-1, 0, -1):
            self.swap(nums, 0, i)
            self.heapify(nums, 0,i)
        return nums



s = Solution()
print(s.sortArray([5,1,1,2,0,0]))
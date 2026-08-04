class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)

        for num in nums:
            num_counts[num] += 1
        
        heap = []

        for n in num_counts.keys():
            heapq.heappush(heap, (num_counts[n], n))
            if len(heap) > k:
                heapq.heappop(heap)

        return [t[1] for t in heap]
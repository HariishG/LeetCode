class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i in range(len(times)):
            times[i].append(i)
        times.sort()

        available=[i for i in range(len(times))]
        used=[]
        for i in times:
            while used and used[0][0]<=i[0]:
                heapq.heappush(available, heapq.heappop(used)[1])

            chair=heapq.heappop(available)
            heapq.heappush(used, (i[1], chair))

            if i[2]==targetFriend:
                return chair


            
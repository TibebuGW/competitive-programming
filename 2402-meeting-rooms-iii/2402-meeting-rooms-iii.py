class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = [i for i in range(n)]
        used_rooms = [] # (expected_end_time, room_number)
        room_freq = [0 for _ in range(n)]
        meetings.sort()
        
        for start_time, end_time in meetings:
            
            # make rooms (which hosted meetings that ended before the current time starts) available
            while used_rooms and used_rooms[0][0] <= start_time:
                expected_end_time, room_number = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room_number)
            
            # delay the meeting until the earliest ending meeting if there's no available room
            delay_time = start_time
            if not available_rooms:
                expected_end_time, room_number = heapq.heappop(used_rooms)
                delay_time = max(delay_time, expected_end_time)
                heapq.heappush(available_rooms, room_number)
            
            cur_room = heapq.heappop(available_rooms)
            room_freq[cur_room] += 1
            cur_end_time = delay_time + (end_time - start_time)
            heapq.heappush(used_rooms, (cur_end_time, cur_room))
        
        print(room_freq)
        return room_freq.index(max(room_freq))
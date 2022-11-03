from collections import defaultdict

K= int(input())
room_lst=list(input().split(" "))
Room_List=[]
for i in room_lst:
    Room_List.append(int(i))
    
freq = defaultdict(int)
for k in range(len(Room_List)):
    freq[Room_List[k]] += 1
    
for k in range(len(Room_List)):
    if freq[Room_List[k]] == 1:
        print(Room_List[k])
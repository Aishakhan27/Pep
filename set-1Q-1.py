items=[1,2,3,4,5,6]
# output=[1,2],[3,4],[5,6]
k=2
for i in range(0, len(items), k):
    print(items[i:i+k])

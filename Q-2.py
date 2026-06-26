# weight[1.01,1.99,2.5,2.5,1.01],output=3
# carry one or more bags at a time,but the total weight of the bag should not exceed 3.00
bag=int(input("Enter the number of bags: "))
weight=[]
for i in range(bag):
    w=float(input("Enter the weight of bag: "))
    weight.append(w)
trip=0
weight.sort()
left=0
right=len(weight)-1
while left <= right:
    if left == right:
        trip += 1
        break
    if weight[left] + weight[right] <= 3.00:
        left += 1
        right -= 1
    else:
        right -= 1
    trip += 1

print("Number of trips required:", trip)
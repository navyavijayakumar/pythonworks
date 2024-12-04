arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]
]
n=[num for ls in arr for num in ls]
print(n)

num_gt_25=[num for ls in arr for num in ls if num>25]
print(num_gt_25)
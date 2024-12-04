users=['rahul',"rohit","kohli","rishab","sanju","pandya","siraj"]

rahuls_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

users_set=set(users)

# rahuls_followers_set=set(rahuls_followers)

# sanju_followers_set=set(sanju_followers)

#rahul_follow_suggestion=users_set.difference(rahuls_followers)

mutual=set(rahuls_followers).intersection(set(sanju_followers))
# mutual=rahuls_followers_set.intersection(sanju_followers_set)

#print(rahul_follow_suggestion)

print(mutual)
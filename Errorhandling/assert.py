# def poll(age):

#     assert age>=18,"invalid age"
#     print("voted")
# try:
#     poll(10)

# except Exception as e:
#     print(e)

# def review(rating):
#     assert rating>=0,"too low"
#     assert rating<=10,"too high"
#     print("Done")
# try:
#     review(0)
# except Exception as e:
#     print(e)

# def review(rating):
#     assert rating>=0,"too low"
#     assert rating in range(0,11),"too high"
#     print("Done")
# try:
#     review(11)
# except Exception as e:
#     print(e)




# def is_leap_yr(num):

#     if num<0:
#         return False

#     if (num%100==0 and num%400==0) or (num%100!=0 and num%4==0):
#         return True
#     else:
#         return False

# def test_leap_yr():

#     assert is_leap_yr(2024)==True,"non century yr chk failed"
#     assert is_leap_yr(2025)==False,"invalid non century yr chk failed"
#     assert is_leap_yr(2000)==True,"century yr chk failed"
#     assert is_leap_yr(1900)==False,"invalid century yr chk failed"
#     assert is_leap_yr(-2024)==False,"invalid yr chk failed"

# try:

#     test_leap_yr()
#     print("test case pass")

# except Exception as e:

#     print("failed,",e)


def factorial(num):

    n=1
    for i in range(1,num+1):
        n=i*n
    return n

def test_factorial():
    assert factorial(5)==120,"factorial chk failed"
try:
    test_factorial()
    print("passed")
except Exception as e:
    print("failed,",e)

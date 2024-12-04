f_read=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\years.txt","r")
f_leap=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\leapyr.txt","w")
f_century=open("C:\\Users\\user\\OneDrive\\Documents\\Desktop\\Pythonworks\\datasets\\centuryyr.txt","w")

def is_century_yr(year):

    return True if year%100==0 else False
def is_leap_year(year):
   if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
       return True
   else:
       return False
   
for year in f_read:
    year=int(year)
    if is_century_yr(year):
        f_century.write(str(year)+"\n")
    if is_leap_year(year):
        f_leap.write(str(year)+"\n")   


# for year in f_read:
#     year=int(year)
#     if year%100==0:
#         f_century.write(str(year)+"\n")
#     if (year%100==0 and year%400==0) or (year%4==0 and year%100!=0):
#         f_leap.write(str(year)+"\n")

    
f_read.close()
f_century.close()
f_leap.close()

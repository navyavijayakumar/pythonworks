student_data={
    "hari":[45,40,35],
    "vipin":[45,34,35],
    "vinay":[50,40,35],
    "bijoy":[45,78,35],
    "anvin":[45,42,35],
}
# index=3
# for i,element in enumerate(student_data):
#     if i+1==index:
#         print(element)
#         marks=student_data.get(element)
#         avg=sum(marks)/len(marks)
#         print(avg)


# for i,element in enumerate(student_data):
#         marks=student_data.get(element)
#         avg1=round(sum(marks)/len(marks),2)
#         avg={element:avg1}
#         print(avg)

stu_avg_marks={k:sum(v)//len(v)for k,v in student_data.items()}
print(stu_avg_marks)

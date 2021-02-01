import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (k, v) in student_dict.items():
#     print(v)

# Loop through a data frame
student_df = pandas.DataFrame(student_dict)
# for (k, v) in student_df.items():
#     print(v)

# Loop through rows of a data frame
for (index, row) in student_df.iterrows():
    print(index, row)
    if row.student == "Angela":
        print('score of Angela: ', row.score)

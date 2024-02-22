import pandas as pd

# 1. 1- Which type of data can be used 
# while creating a series object in pandas?
# Answer: Integer, float, string, bool, datetime, category, object

#2. 2- Create a series having the month's 
#number as data and assign name as their index values?

month = pd.Series([x for x in range(1,13)], index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(f"Question 2\n\n{month}\n\n")

#3-Write a program to create a series object using 
# the dictionary which store the number of students 
# in fresh batch groups ( MatMIE, Mat DAIS, COMIE, COMEC)?

Students = pd.Series([33, 32,29,28], index = ["MatMie", "MatDais", "COMIE", "COMEC"])
print(f"Question 3\n\n{Students}\n\n")


# 4-  Write a Pandas program to create and display a DataFrame from a 
# specified dictionary data which has the index labels.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, 'np.nan', 9, 20, 14.5, 'np.nan', 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

df = pd.DataFrame(exam_data, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(f"Question 4\n\n{df}\n\n")


#5- Write a Pandas program to select the rows where the number of 
# attempts in the examination is greater than 2.

greater = df[df['attempts'] > 2]
print(f"Question 5\n\n{greater}\n\n")
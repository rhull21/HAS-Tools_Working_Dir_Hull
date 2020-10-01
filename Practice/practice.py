## General Training Notes

# 09082020
# # Python practice lists, for loops, conditionals
# From Cheat Sheets


# %%
## Lists a
## Lists a
a = 'is'
b = 'nice'
my_list = ['my', 'list', a, b]

print(my_list)
# subset
print(my_list[0])
print(my_list[-2])

# slice
print(my_list[1:3])

# %% 
## Lists b

# List Methods
# index entry
my_list.index('my') 
# count number of entries
my_list.count(a)
# add to end of list
my_list.append('!')
# remove from list, by entry
my_list.remove('!')
# del from list, by index
del(my_list[0:1])
# reverse order
my_list.reverse()
# extend -> like append but iterable
my_list.extend('!')
# remove and return item at index
my_list.pop(-1)
# insert an item at the ith location
my_list.insert(0,'!')
# sort list (alpha, numberically?)
my_list.sort()


# %%
# Lists c

# append lists
print(my_list + my_list)
# Does not work, cuz list + scaler
# print(my_list + 2) 
# multiple lists 
print(my_list*2)

# %%
# Lists d
print(my_list)

# %%
# Conditionals (if/then) a

car = 'bmw'
## check equality
car == 'bmw' # returns true
car == 'audi' # returns false

## check equality (ignroe case)
car.lower() == 'audi' # returns false
car.lower() == 'bmw' # returns true

# check inequality
car != 'audi' # returns true
car != 'bmw' # returns false


# %%
# Conditionals (if/then) b

# numerical comparisons
age = 28
age == 28 # returns true
age == 18 # returns false
age != 18 # returns true
age > 18 # returns true
age < 18 # returns false


# %%
# Conditionals (if/then) c 

# multiple conditions

ages = [1, 15, 25, 30]
ages[0] <= 10 and ages[1] >=10 #returns true
ages[0] <= 10 and ages[1] <=10 #returns false 
ages[0] <= 10 or ages[1] <=10 #returns true

# %%
# Conditionals (if/then) d 

# simple if
age = 19
if age >= 18: 
    print("You're old enough to drive")

#  %%

# Conditionals (if/then) e 

# complex if-else chain
age = 1

# nb colons important

if age > 4: 
    price = 0 
elif age > 18:
    price = 5
else:
    price = 10

print("Your cost is $" + str(price))

# Alternative
# print(f"Your cost is $(price).")

# %%

# Conditionals (if/then) f
# 
# Testing if a value is in a list

players = ['al', 'bea', 'cyn', 'dale']
'al' in players # returns true
'eric' in players # returns false


# %%

# for loops #1
# From: https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/

# ex 1
list_of_values = [1, 2, 3, 4, 5]

# loops through all entries in LIST using placeholder
##  placeholder       LIST
for avalue in list_of_values:
    print(avalue)

# General Syntax 
# item_list = [item_1, item_2, item_3]

# for i in item_list:
#     execute some code here

# %%

# for loops #2

# ex 2, arithmetic operations on the placeholder

num_list = [12, 5, 136, 47]

# For each item in list, add 10 and print new value
for i in num_list:
    i += i*2 # set value = placeholder + 2 times placeholder
    print(i)


# %%

# for loops #3

# ex 3, loops with strings

files = ['file1.txt', 'file2.txt']

for fname in files: 
    print(fname)


# %%

# for loops #4 

# ex 3, loops with data structures (i.e. lists of lists)
months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
          "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

avg_monthly_precip = [0.70,  0.75, 1.85, 2.93, 3.05, 2.02,
                      1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

# List of list names
lists = [months, avg_monthly_precip]

# For each item in list, print value
for dlist in lists:
    print("The value of the variable 'dlist' is:", dlist)

# for each list in lists, print the length
for dlist in lists:
    print(len(dlist))

# for each list in list, print the last value
for dlist in lists: 
    print(dlist[-1])


# %%

# for loops #5

# Experimenting with lists of lists

months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
          "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

avg_monthly_precip = [0.70,  0.75, 1.85, 2.93, 3.05, 2.02,
                      1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

# List of list names
lists = [months, avg_monthly_precip]

# print each individual value
for dlist in lists: 
    for i in dlist:
        print(i)

# print values side by side
for i in range(0, len(months)):
    print(months[i], avg_monthly_precip[i])

# %%

# list comprehension a 
# a way to use the power of for loops within lists 
# that is super fast

# https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/list-comprehensions

# a special application where syntax is a bit reversed
    # the operation comes before the subsetting

# general syntax (assume an existing list)
# new_list = []
# for i in list: 
#     new_list.append(i*i)

# example 1 (slow)
for_list = []
for i in range(50000):
    for_list.append(i*i)

# print(for_list)

# example 2 (fast)
comp_list = [i*i for i in range(50000)]

# %%

# list comprehension b
# modifying values 

# Create list of average monthly precip (inches) in Boulder, CO
avg_monthly_precip_in = [0.70,  0.75, 1.85, 2.93, 3.05, 2.02, 
                         1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

# Convert each item in list from in to mm
[month * 25.4 for month in avg_monthly_precip_in]    


# %%

# list comprehension c
# modifying values using conditionals

# Filtering out values in a month that are less than 1.5
[month for month in avg_monthly_precip_in if month > 1.5]

# Performing if else
# Performing two different operations on the variables depending on if they are more or less than 1.5. 
# If they are more then 1.5, they are multiplied by negative 2. Otherwise, they are multiplied by positive 2. 
[month * -2 if month > 1.5 else month * 2 for month in avg_monthly_precip_in]

# %%
# numpy data frames a

# import panda  and make panda  data frame

# See: https://www.geeksforgeeks.org/different-ways-to-create-pandas-dataframe/#:~:text=%23%20initialise%20data%20of%20lists.&text=%23%20Creates%20pandas%20DataFrame.&text=Pandas%20DataFrame%20can%20be%20created%20by%20passing%20lists%20of%20dictionaries,dictionary%20keys%20taken%20as%20columns.

import pandas as pd
# one option
# intialize from lists
df_input = {'Name':['Tom', 'Jack', 'nick', 'juli'], 'marks':[99, 98, 95, 90]} 
# convert input to dataframe
df = pd.DataFrame(df_input)

# %%
# numpy data frames b

# See: week2_firstpython.py

# view df
df.shape  # See how many rows and columns the data has
df.head(1) # look at the first x rows of the data
df.tail(1) # look at the last  x rows  of the data

df.iloc[2] # grab any subset of rows to look at
# df.flow[350:380]  #Grab a subset of just the flow data dat look at

# %%
# Remove last N characters from string in Python

# See: https://thispointer.com/remove-last-n-characters-from-string-in-python/#:~:text=Remove%20final%20N%20characters%20from,characters%20from%20a%20string%20i.e.&text=To%20remove%20last%201%20character%2C%20just%20set%20n%20to%201.

org_string = "1989-01-01 00:00"

mod_string = org_string[:-6]

print(mod_string)

# Remove ends of stromg emtroes om Panda DataFrame Column

# SEe: https://stackoverflow.com/questions/37001787/remove-ends-of-string-entries-in-pandas-dataframe-column


# Below: three ways to remove .txt
f = pd.DataFrame({'A': {0: 2, 1: 1}, 
                   'C': {0: 5, 1: 1}, 
                   'B': {0: 4, 1: 2}, 
                   'filename': {0: "txt.txt", 1: "x.txt"}}, 
                columns=['filename','A','B', 'C'])

print df
#   filename  A  B  C
# 0  txt.txt  2  4  5
# 1    x.txt  1  2  1

df['filename'] = df['filename'].str.replace(r'.txt$', '')
print df
#   filename  A  B  C
# 0      txt  2  4  5
# 1        x  1  2  1

df['filename'] = df['filename'].map(lambda x: str(x)[:-4])
print df
#   filename  A  B  C
# 0      txt  2  4  5
# 1        x  1  2  1

df['filename'] = df['filename'].str[:-4]
print df
#   filename  A  B  C
# 0      txt  2  4  5
# 1        x  1  2  1

# %%


# 09152020
# # Python practice numpy
# From Cheat Sheets

# %% 
# Short hand

# import numpy
import numpy as np

# arr - a numpy array

# %%
# importing/exporting files
np.loadtxt('file.txt') # - From a text file
np.genfromtxt('file.csv',delimiter=',') # - From a CSV file
np.savetxt('file.txt',arr,delimiter=' ') # - Writes to a text file
np.savetxt('file.csv',arr,delimiter=',') # - Writes to a CSV file

# eg: 
# import from text file
arr1 = np.loadtxt('C:/Users/Juniper/OneDrive/Workspace/Work/03_UA/03_Classwork/04_HAS_Tools/02_github/github_repos/HAS-Tools_Working_Dir_Hull/Practice/practice1.txt')
arr1
# array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])

# import from csv (as string, for example)
arr1 = np.genfromtxt('C:/Users/Juniper/OneDrive/Workspace/Work/03_UA/03_Classwork/04_HAS_Tools/02_github/github_repos/HAS-Tools_Working_Dir_Hull/Practice/practice2.csv',delimiter=',')
arr1

# export to an existing csv
np.savetxt('practice2.csv',arr1,delimiter=',') 
# %%
## Creating Arrays

# 1-D array
arr1 = np.array([1,2,3])
# >>> print(arr1)
# [1 2 3]

# 2-D array (notes syntax, between ()
arr1 = np.array([(1,2,3),(4,5,6)])
# >>> print(arr1)
# [[1 2 3]
 # [4 5 6]]

# - 1D array of length 3 all values 0
np.zeros(3) 
# - 3x4 array with all values 1
np.ones((3,4)) 
# - (Identity matrix), 5x5 array of 0 with 1 on diagonal
np.eye(5)
# - Array of 6 evenly divided, from 0 to 100
# # [  0.  20.  40.  60.  80. 100.]
np.linspace(0,100,6) 
# - [0 3 6 9]
np.arange(0,10,3)
# - 2x3 array with all values 8
np.full((2,3),8) 
# - 4x5 array of random floats 0 to 1
np.random.rand(4,5)
# - - 6x7 array of randomfloats between 0-100
np.random.rand(6,7)*100 
# - 2x3 array with random ints between 0-4
np.random.randint(5,size=(2,3)) 

# %% 

# Creating arrays using dictionary
arr1 = np.array({'names':['gender', 'age'], 'formats':['S1',np.int32]})



# %%
## Inspecting Properties

arr1 = np.full((2,3),8) 


# - Returns number of elements in arr
arr1.size 
# - Returns dimensions of arr (rows, columns)
arr1.shape 
# - Returns type of elements in arr
# # dtype = default type -> https://numpy.org/doc/stable/reference/generated/numpy.dtype.html
# # Examples: int32, int64, int16, 
arr1.dtype 
# - Convert arr elements to
# type dtype
arr1.astype(dtype) # does not work
## dtype must be formatted like 'np.dtype', with dtype specfied like int32, etc..
arr1.astype(np.float32) # works
# - Convert arr to a Python list
arr1.tolist() 

# %%
# view documentation

# - View documentation for
# np.eye
np.info(np.eye)

# %%

# COPYING/SORTING/RESHAPING
# - Copies arr to new memory
np.copy(arr) 
# - Creates view of arr elements
arr.view(dtype)  # need to specific dtype like <np>.<dtype>
# - Sorts arr
arr.sort() 
# - Sorts specific axis of arr
arr.sort(axis=0) # where axis is n-1 dimension
# - Flattens 2D array
# two_d_arr to 1D
two_d_arr.flatten() 
# - Transposes arr (rows become columns and
# vice versa)
arr.T 
# - Reshapes arr to 3 rows, 4
# columns without changing data
arr.reshape(3,4) 
 # Changes arr shape to 5x6
# and fills new values with 0
arr.resize((5,6))

# %%
## Add / Remove Elements

# - Appends values to end
# of arr
np.append(arr,values) # nb always resizes to 1-D
 # - Inserts values into
# arr before index 2
np.insert(arr,2,values)
 # - Deletes row on index
# 3 of arr
np.delete(arr,3,axis=0) # where index 0 = first row
 # - Deletes column on
# index 4 of arr
np.delete(arr,4,axis=1)# where index 0 = first column
 
# %% 
# COMBINING/SPLITTING
# - Adds
# arr2 as rows to the end of arr1
np.concatenate((arr1,arr2),axis=0) # nb: the size of these arrays much match rows v columns
# - Adds
# arr2 as columns to end of arr1
np.concatenate((arr1,arr2),axis=1) # nb: the size of these arrays much match rows v column
#  Splits arr into 3 sub-arrays
np.split(arr,3) #nb: the division must be even
# - Splits arr horizontally on the
# 5th index
np.hsplit(arr,5) 

# %% 

arr1 = np.random.randint(10,size=(5,5))
# >>> arr1
# array([[2, 4, 7, 6, 2],
       # [5, 7, 6, 3, 0],
       # [3, 1, 6, 0, 3],
       # [3, 9, 0, 3, 5],
       # [3, 7, 3, 9, 0]])
	   
# - Returns the element at index 4
arr1[4]
# array([3, 7, 3, 9, 0])

# - Returns the 2D array element on index [2][4]
arr1[2,4]
# 3

# - Assigns array element on index 1 the
arr1[1]=4
arr1
# array([[2, 4, 7, 6, 2],
       # [4, 4, 4, 4, 4],
       # [3, 1, 6, 0, 3],
       # [3, 9, 0, 3, 5],
       # [3, 7, 3, 9, 0]])
	   
# >>> # - Returns the elements at indices 0,1,2
# >>> # (On a 2D array: returns rows 0,1,2)
arr1[0:3]
# array([[2, 4, 7, 6, 2],
       # [4, 4, 4, 4, 4],
       # [3, 1, 6, 0, 3]])

# >>>  # - Returns the elements on rows 0,1,2
# >>> # at column 4
arr1[0:3,4]
# array([2, 4, 3])

# >>> # - Returns the elements at indices 0,1 (On
# >>> # a 2D array: returns rows 0,1)
arr1[:2]
# array([[2, 4, 7, 6, 2],
       # [4, 4, 4, 4, 4]])
	   
# >>> # Elements at index 1 for all rows
>>> arr1[:,1]
array([4, 4, 1, 9, 7])

#>>> # - Returns an array with boolean values
 arr1<5
# #array([[ True,  True, False, False,  True],
       # [ True,  True,  True,  True,  True],
       # [ True,  True, False,  True,  True],
       # [ True, False,  True,  True, False],
       # [ True, False,  True, False,  True]])
	   
# >>> # - Returns array elements smaller than 5
arr1[arr1<5]
# array([2, 4, 2, 4, 4, 4, 4, 4, 3, 1, 0, 3, 3, 0, 3, 3, 3, 0])
	   
# INDEXING/SLICING/SUBSETTING
# - Returns the element at index 5
arr[5] 
# - Returns the 2D array element on index [2][5]
arr[2,5] 
# - Assigns array element on index 1 the
# value 4
arr[1]=4 
 # - Assigns array element on index[1][3] the value 10
arr[1,3]=10
# - Returns the elements at indices 0,1,2
# (On a 2D array: returns rows 0,1,2)
arr[0:3] 
 # - Returns the elements on rows 0,1,2
# at column 4
arr[0:3,4]
# - Returns the elements at indices 0,1 (On
# a 2D array: returns rows 0,1)
arr[:2] 
# - Returns the elements at index 1 on all
# rows
arr[:,1] 
# - Returns an array with boolean values
arr<5 
# - Returns an array with
# boolean values
(arr1<3) & (arr2>5) 
# - Inverts a boolean array
~arr 
# - Returns array elements smaller than 5
arr[arr<5] 


# %% 
# Scaler Math

## Given, arr = 
	# array([[2, 4, 7, 6, 2],
		   # [4, 4, 4, 4, 4],
		   # [3, 1, 6, 0, 3],
		   # [3, 9, 0, 3, 5],
		   # [3, 7, 3, 9, 0]])


# - Add 1 to each array element
np.add(arr,1) 
	# array([[ 3,  5,  8,  7,  3],
		   # [ 5,  5,  5,  5,  5],
		   # [ 4,  2,  7,  1,  4],
		   # [ 4, 10,  1,  4,  6],
		   # [ 4,  8,  4, 10,  1]])
#  - Subtract 2 from each array element
np.subtract(arr,2)
	# array([[ 0,  2,  5,  4,  0],
		   # [ 2,  2,  2,  2,  2],
		   # [ 1, -1,  4, -2,  1],
		   # [ 1,  7, -2,  1,  3],
		   # [ 1,  5,  1,  7, -2]])
# - Multiply each array element by three
np.multiply(arr,3) 
	# array([[ 6, 12, 21, 18,  6],
		   # [12, 12, 12, 12, 12],
		   # [ 9,  3, 18,  0,  9],
		   # [ 9, 27,  0,  9, 15],
		   # [ 9, 21,  9, 27,  0]])
# - Divide each array element by
# 3 4 (returns np.nan for division by zero)
np.divide(arr,4) 
	# array([[0.5 , 1.  , 1.75, 1.5 , 0.5 ],
		   # [1.  , 1.  , 1.  , 1.  , 1.  ],
		   # [0.75, 0.25, 1.5 , 0.  , 0.75],
		   # [0.75, 2.25, 0.  , 0.75, 1.25],
		   # [0.75, 1.75, 0.75, 2.25, 0.  ]])
# raise each element to the 5th power
np.power(arr,5) 
	# array([[   32,  1024, 16807,  7776,    32],
		   # [ 1024,  1024,  1024,  1024,  1024],
		   # [  243,     1,  7776,     0,   243],
		   # [  243, 59049,     0,   243,  3125],
		   # [  243, 16807,   243, 59049,     0]], dtype=int32)
# - Square root of each element in the
# array
np.sqrt(arr) 
# array([[1.41421356, 2.        , 2.64575131, 2.44948974, 1.41421356],
       # [2.        , 2.        , 2.        , 2.        , 2.        ],
       # [1.73205081, 1.        , 2.44948974, 0.        , 1.73205081],
       # [1.73205081, 3.        , 0.        , 1.73205081, 2.23606798],
       # [1.73205081, 2.64575131, 1.73205081, 3.        , 0.        ]])
# - Sine of each element in the array
np.sin(arr) 
# - Natural log of each element in the
# array
np.log(arr)
# - Absolute value of each element in
# the array 
np.abs(arr) 
# - Rounds up to the nearest int
np.ceil(arr)
# - Rounds down to the nearest int
np.floor(arr) 
# - Rounds to the nearest int (up and down)
np.round(arr) 


		   
# %%
## VECTOR MATH

### Given:
	# >>> arr1
	# array([[2, 4, 7, 6, 2],
		   # [4, 4, 4, 4, 4],
		   # [3, 1, 6, 0, 3],
		   # [3, 9, 0, 3, 5],
		   # [3, 7, 3, 9, 0]])
	# >>> arr2
	# array([[ 4,  8, 14, 12,  4],
		   # [ 8,  8,  8,  8,  8],
		   # [ 6,  2, 12,  0,  6],
		   # [ 6, 18,  0,  6, 10],
		   # [ 6, 14,  6, 18,  0]])

# - Elementwise add arr2 to arr1		   
np.add(arr1,arr2) 
	# array([[ 6, 12, 21, 18,  6],
		   # [12, 12, 12, 12, 12],
		   # [ 9,  3, 18,  0,  9],
		   # [ 9, 27,  0,  9, 15],
		   # [ 9, 21,  9, 27,  0]])
# - Elementwise subtract
# arr2 from arr1
np.subtract(arr1,arr2) 
	# array([[-2, -4, -7, -6, -2],
		   # [-4, -4, -4, -4, -4],
		   # [-3, -1, -6,  0, -3],
		   # [-3, -9,  0, -3, -5],
		   # [-3, -7, -3, -9,  0]])
# - Elementwise multiply
# arr1 by arr2
np.multiply(arr1,arr2) 
	# array([[  8,  32,  98,  72,   8],
		   # [ 32,  32,  32,  32,  32],
		   # [ 18,   2,  72,   0,  18],
		   # [ 18, 162,   0,  18,  50],
		   # [ 18,  98,  18, 162,   0]])
 # - Elementwise divide arr1
# by arr2
np.divide(arr1,arr2)
	# array([[0.5, 0.5, 0.5, 0.5, 0.5],
		   # [0.5, 0.5, 0.5, 0.5, 0.5],
		   # [0.5, 0.5, 0.5, nan, 0.5],
		   # [0.5, 0.5, nan, 0.5, 0.5],
		   # [0.5, 0.5, 0.5, 0.5, nan]])
# - Elementwise raise arr1
# raised to the power of arr2
np.power(arr1,arr2) 
	# array([[         16,       65536,  -381759919, -2118184960,          16],
		   # [      65536,       65536,       65536,       65536,       65536],
		   # [        729,           1, -2118184960,           1,         729],
		   # [        729, -1953380655,           1,         729,     9765625],
		   # [        729,  -381759919,         729, -1953380655,           1]],
		  # dtype=int32)
# - Returns True if the
# arrays have the same elements and shape
np.array_equal(arr1,arr2) 
# False


# %% 
## Statistics

## Given: 
	# >>> arr
	# array([[2, 4, 7, 6, 2],
		   # [4, 4, 4, 4, 4],
		   # [3, 1, 6, 0, 3],
		   # [3, 9, 0, 3, 5],
		   # [3, 7, 3, 9, 0]])


# - Returns mean along
# specific axis
np.mean(arr,axis=0) 
	# array([3. , 5. , 4. , 4.4, 2.8])
# - Returns sum of arr
arr.sum() 
	# 96
# - Returns minimum value of arr 
arr.min() 
	# 0 
# - Returns maximum value of
# specific axis

arr.max(axis=0) 
	# array([4, 9, 7, 9, 5])
# - Returns the variance of array
np.var(arr) 
	# 5.894399999999999
# - Returns the standard
# deviation of specific axis
np.std(arr,axis=1) 
	# array([2.03960781, 0.        , 2.05912603, 2.96647939, 3.2       ])
# - Returns correlation coefficient
# of array
arr.corrcoef() 
	# Doesn't work
	
# %% 

# set nan to a number
## See: https://www.geeksforgeeks.org/numpy-nan_to_num-in-python/#:~:text=nan_to_num()%20function%20is%20used,small%20(or%20negative)%20number.

# Syntax : numpy.nan_to_num(arr, copy=True)
	# Given: 
		# arr2
			# array([[ 1., nan],
				   # [nan,  1.]])
>>> np.nan_to_num(arr2)
	# array([[1., 0.],
		   # [0., 1.]])	   

#09172020: 

	#Classroom Lecture
	

# %% 
# List pros: 
	#mixed data
list0 = [10, "hello", FALSE]

# List cons:
	#not as flexible

# Dim a list	
list1 = [3,4,5.1,6]

# How do I add a value to each item in a list?

# Does not work
list2 = list1 + 2 

# Does work 
list2 = [i + 2 for i in list1]

# %%
# Numpy
# Numpy Pro:
	# Instantly vectorizes numeric data
	
# Numpy Cons:
	# Doesn't Deal with text well, though

# the same as list 1, but all values are floats
arr1 = np.array([3,4,5.1,6])

print(arr1)
# [3.  4.  5.1 6. ]
print(arr1.dtype)
# float64
print(list1)
# [3, 4, 5.1, 6]

# check dimensions, shape, and size
print(arr1.ndim)
#1
print(arr1.shape)
#(4,)
print(arr1.size)
#(4)

# Broadcasting: 
arr2 = arr1 + 7
print(arr2)
# [10.  11.  12.1 13. ]

# %%
# create a 10x10 array with zero values
arr_zero = np.zeros((10,10), dtype = int)
print(arr_zero)
	# [[0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]
	 # [0 0 0 0 0 0 0 0 0 0]]
	 
# check dimensions, shape, and size
print(arr_zero.ndim) # 2
print(arr_zero.shape) # (10,10)
print(arr_zero.size) # 100


# 3 ways to make a matrix filled with sevens

arr_7a = arr_zero + 7
arr_7b = np.ones((10,10), dtype = int )*7
arr_7c = np.full((10,10), 7)

	# [[7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]
	 # [7 7 7 7 7 7 7 7 7 7]]
	 
	 
# %%
	# Index numpy arrays:
		
# create a 10x10 array of randomints
arr_test = np.random.randint(100,size=(10,10))
print(arr_test)
	# [[81  8 70 78 16 74 20 98 60 30]
	 # [99 60 28 56 65 91 39 10 69 83]
	 # [76 32 13  1 57 54 49 99 51 40]
	 # [28 49 31 23 47 87 69 35 73 13]
	 # [87 81 11 53 37 88 68 66 52 75]
	 # [30 52 30 33 97 16 56 63 81 13]
	 # [58 32 28 98 14 65 45 15 87 79]
	 # [68 27 44 41 26 51 76 93 80 84]
	 # [98 62 76 64 70 64 68 76 41 25]
	 # [84 37 28 87 33 26 39 23 81 86]]

# Slicing
# FORMAT start:stop, step
# default to start = 0, stop = size of dimension, step = interval between

# grab first row
arr_test[0]

# grab last element of first row
arr_test[0,9]

# grab fist and second row
arr_test[0:2]

# grab last elements of first and second row
arr_test[0:2, 9]

# skipping through and collecting 0th and 5th row and 10th row and....
arr_test[::5]

# skips and gives every other on first row
arr_test[0:1, ::2]

# assigns every other value in first row to 999
arr_test[0:1, ::2] = 999


# %% Uniersal Functions
# Vectorized OPerations just means that its something you can do to the entire array

arr_test = np.random.randint(100,size=(10,10))
print(arr_test)

		# [[22 76 47 73 10 15 38 31 49 89]
		 # [24 55 38 43 53 63 98 61 31 73]
		 # [69 56 25  5 76  6 62 49 10 85]
		 # [59 30 56 67 87 68 68 40 98 13]
		 # [57 59 11 28 54 79 78 53 15 31]
		 # [48  7 87 56 49 81 36 11  5 53]
		 # [93 56 44  5 57 76 20 97 70 80]
		 # [44 25 82 88 98 21 59 33 50 37]
		 # [39 62 64 89 94 76 79 73 47 38]
		 # [55 20 25 25 28 71 84 65 62 32]]
		 
# Ex of normal math: 
arr_test = arr_test*2

# boolean returns value at every other 
arr_test>5

# Aggregates: 
np.max(arr_test) # max for whole array
np.max(arr_test, axis = 0) # max for each columne
np.max(arr_test, axis = 1) # max for each row

# %%
import numpy as np

# 1. Get the largest integer that is less than or equal to the division
# of the inputs x1 and x2 where x1 is all the integers from 1-10 and x2=1.3
# x1 = np.arange(1,11,1)
# x2 = 1.3
# print(x1, x2)
# print(np.divide(x1, x2).astype(int))

# 2. given an array x1=[0, 4, 37,17] and a second array with the values
# x2=[1.2, 3, 4.6, 7] return x1/x2 rounded to two decimal places

x1=[0, 4, 37,17] 
x2=[1.2, 3, 4.6, 7]

answer = np.round(np.divide(x1,x2), decimals=2)
print(answer)

# 3. Create a 10 by 100 matrix with 1000 random numbers and report the 
# average and standard deviation across the entire matrix and 
# for each of the 10 rows. Round your answer to  two decimal places

## hint -> np.random

# %%

### PANDAS
import numpy as np
import pandas as pd


## Advantages:
# Names of rows and columns
# Can have variable data types in e/a column
# built of numpy
# can be (more) easily queried
# note the index

## Thre ethings - Series (1-D), DataFrames, and Indices

# series w/ autonum index
sr1 = pd.Series([0.1, 50, 47, 3.37])
print(sr1)
# note the index defaults to 0,,,3
	# 0     0.10
	# 1    50.00
	# 2    47.00
	# 3     3.37
	# dtype: float64

# grab based on index
print(sr1[1:3])

# series w/ numeric index
sr2 = pd.Series([0.1, 50, 47, 3.37], index=['a', 'b', 'c', 'd'])
print(sr2)
	# a     0.10
	# b    50.00
	# c    47.00
	# d     3.37

# return values, indices respectively 
sr1.values
sr1.index
sr2.index

# index is a forever name for the rows, you can sort on 'em
print(sr1.sort_index(ascending=False))


# %%
## Pandas - Dataframes
# these are like series but 2D, so we have rows and columns
# remember - index always refers to rows)
rng = np.random.RandomState(42) # generates random range of numbers we can duplicate
# generate data frame with random numbers (from state) and give columns
df = pd.DataFrame(rng.randint(0,10,(3,3)),index=['row1', 'row2', 'row3'],columns = ['a','b','c'])
# print(df)

# grab just the 'b' column
df1 = df['b']
print(np.mean(df1))
del(df1)

# grab out parts
print("values", df.values, "indices", df.index, "columns", df.columns,sep= "\n")

# loc - find row by index 
# eg df.loc[row index, col name (opt)]
df.loc['row1']
df.loc['row1','b']

# iloc - finds row by number (location0
# df.iloc[row number, col number (opt)]
df.iloc[0]
df.iloc[0,1]

# indexing and col nmaes is used for vector math (i)
# note diff orders of indexes
df2 = pd.DataFrame(rng.randint(0,10,(3,3)),index=['row1', 'row2', 'row3'],columns = ['a','b','c'])
df3 = pd.DataFrame(rng.randint(0,10,(3,3)),index=['row2', 'row3', 'row1'],columns = ['a','b','c'])

print(df2)
print(df3)

print(df2 + df3)

# rows that exist in one but not another generate na
# note that some indices exist in one but noot another
df2 = pd.DataFrame(rng.randint(0,10,(3,3)),index=['row1', 'row2', 'row4'],columns = ['a','b','c'])
df3 = pd.DataFrame(rng.randint(0,10,(3,3)),index=['row2', 'row3', 'row1'],columns = ['a','b','c'])

print(df2)
print(df3)
df4 = df2 + df3

print(df4)


# how to handle na?
# lots of ways
# df.fillna(x) is one way to put 0 is the enpty rows
print(df4.fillna(0))


# %%

# Plotting
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# %% 
## Line Plots
### make an empty figure
fig = plt.figure()
ax = plt.axes()

# %%
### add a sin wave

fig = plt.figure()
ax = plt.axes()
#### create an array of numbers
x = np.linspace(0,10,1000)
# print(x)
ax.plot(x,np.sin(x))

# %%
### use pylab to get same result
fig = plt.figure()
ax = plt.axes()
#### pylab = plt.plot
plt.plot(x,np.sin(x))
#### can be called multiple times
plt.plot(x,np.cos(x))

# %%
### adjusting colors and style
#### colors
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported

#### styles (with linestyle)
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted

# %%
#### integrated color and style
plt.plot(x, x + 0, '-g')  # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r');  # dotted red

# %%
plt.plot(x, np.sin(x))

### Axes Limit 
#### xlim, ylim

# plt.xlim(-1, 11)
# plt.ylim(-1.5, 1.5)

#### .axis([xmin, xmax, ymin, ymax])
# plt.axis([-1, 11, -1.5, 1.5])

#### keywords tight, equal, 
plt.axis('tight')
plt.axis('equal')

# %%

### labeling (.title, .xlabel, .ylabel)
# plt.plot(x, np.sin(x))
# plt.title("A Sine Curve")
# plt.xlabel("x")
# plt.ylabel("sin(x)");

### by series, define label property, and create plt.legend()
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')

plt.legend()

# %%
### side note -> not all plt.methods translate to ax.methods
#### examples ax.set_method()
	# plt.xlabel() → ax.set_xlabel()
	# plt.ylabel() → ax.set_ylabel()
	# plt.xlim() → ax.set_xlim()
	# plt.ylim() → ax.set_ylim()
	# plt.title() → ax.set_title()

#### or just use ax.set(methods)
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot');

# %%

# Plotting
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

# %%

## Scatter Plots
### with plt.plot()
#### set 'style' to 'o', for example, or 'o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd'
# x = np.linspace(0, 10, 30)
# y = np.sin(x)

# plt.plot(x, y, 'o', color='black')

#### all style types
# rng = np.random.RandomState(0)
# for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
#     plt.plot(rng.rand(5), rng.rand(5), marker,
#              label="marker='{0}'".format(marker))
# plt.legend(numpoints=1)
# plt.xlim(0, 1.8)

#### dots plus line
# plt.plot(x, y, '-ok');

#### wide range of properties
plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2);


# %%


### plt.scatter (more powerful) 
### BECAUSE each point can be individually controlled or mapped to data
#### ex 1
# x = np.linspace(0, 10, 30)
# y = np.sin(x)
# plt.scatter(x, y, marker='o')

#### ex 2 
#### set range of values randomly, colors randomly, and sizes randomly
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()  # show color scale

# %%
### from sklearn.datasets
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);

# %%
# Plotting
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


# %%
## Visualizing Errors
### Error bars

x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

#### use .errorbar, ex 1
#plt.errorbar(x, y, yerr=dy, fmt='.k');

#### use .errorbar, ex 2
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0);

# %%
### Continuous Errors
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process import GaussianProcessClassifier

# # define the model and draw some data
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# # Compute the Gaussian process fit
gp = GaussianProcessClassifier(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1,
                     random_start=100)
gp.fit(xdata[:, np.newaxis], ydata)

# xfit = np.linspace(0, 10, 1000)
# yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
# dyfit = 2 * np.sqrt(MSE)  # 2*sigma ~ 95% confidence region

# # Visualize the result
# plt.plot(xdata, ydata, 'or')
# plt.plot(xfit, yfit, '-', color='gray')

# plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
#                  color='gray', alpha=0.2)
# plt.xlim(0, 10);


# %%
# Histograms, Binning, and Density
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')


# %%
data = np.random.randn(1000)

## First attempt using plt.hist()
# plt.hist(data);

## More detail
# set bins, normed, transparency, tyle of histogram, color, and edge color
# density = True for normalized count
plt.hist(data, bins=30, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='none');

# %%
## compare multiple distributions
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', density=True, alpha=0.3, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs);

# %%
## generates counts at edge of every bin 
### np.histogram(data,bins = n)
counts, bin_edges = np.histogram(data, bins=5)
print(counts)

# %% 
# Sub plots

## Ex:
### Make one plot w/ standard axes
ax1 = plt.axes()
### Make a second plot inset
### starting at 0.65 on x and y axes
###				or x, or y, wi, hei
ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])

# %%
## Ex2 (using object)
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                   xticklabels=[], ylim=(-1.2, 1.2))
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                   ylim=(-1.2, 1.2))

x = np.linspace(0, 10)
ax1.plot(np.sin(x))
ax2.plot(np.cos(x));

# %%
## Using plt.subplot
### create 6 subplots via loop
for i in range(1, 7):
	#plt.subplot(numrows, numcols, index)
    plt.subplot(2, 3, i)
	# print text in each
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')

# %%
### adjust the subplots using
### plt.subplots_adjust(hspace,wspace)
fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),
             fontsize=18, ha='center')

# %%
### altenrative
fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# %%


# %%
# Leadin for 10/01/2020
import pandas as pd
import numpy as np

data_frame = pd.DataFrame([[1, np.nan, 2], [2, 3, 5], [np.nan, 4, 6]])
# make nas = 999
df999 = data_frame.fillna(999)

# turn to 999
# # alternative
dfnan2 = np.where(df999==999,np.nan,df999)

# %%

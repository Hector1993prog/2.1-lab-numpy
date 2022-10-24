#1. Import the NUMPY package under the name np.



#2. Print the NUMPY version and the configuration.



#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?



#4. Print a.



#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"



#6. Print b.



#7. Do a and b have the same size? How do you prove that in Python code?




#8. Are you able to add a and b? Why or why not?



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".



#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?



#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.




#12. Multiply a and c. Assign the result to e.



#13. Does e equal to a? Why or why not?




#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"




#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.




"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""




"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""



#1. Import the NUMPY package under the name np.
import numpy as np
#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a= np.random.random((2,3,5))
#4. Print a.
print(a)
[[[0.48243756 0.60769939 0.9394359  0.02499696 0.38297883]
  [0.83168714 0.17820617 0.26113706 0.91173363 0.42544461]
  [0.51695565 0.39279906 0.16045718 0.99373835 0.94761601]]

 [[0.54569032 0.28936808 0.44554748 0.55145865 0.34810116]
  [0.23238851 0.59683068 0.86837522 0.17014709 0.07568299]
  [0.51551209 0.89084241 0.66576523 0.46479711 0.40983521]]]
#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b= np.ones((5, 2, 3))
#6. Print b.
print(b)
[[[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]]
#7. Do a and b have the same size? How do you prove that in Python code?
if a.size== b.size:
    print(True)
else:
    print(False)
True
a.size
30
b.size
30
#8. Are you able to add a and b? Why or why not?
np.add(a,b)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [23], in <cell line: 1>()
----> 1 np.add(a,b)

ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3) 

#No se puede realizar porque no tienen el mismo número de filas y columnas.
#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
​
c= np.transpose(b, (1, 2, 0))
print(c)
​
[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d= np.add(a,c)
print(d)
[[[1.48243756 1.60769939 1.9394359  1.02499696 1.38297883]
  [1.83168714 1.17820617 1.26113706 1.91173363 1.42544461]
  [1.51695565 1.39279906 1.16045718 1.99373835 1.94761601]]

 [[1.54569032 1.28936808 1.44554748 1.55145865 1.34810116]
  [1.23238851 1.59683068 1.86837522 1.17014709 1.07568299]
  [1.51551209 1.89084241 1.66576523 1.46479711 1.40983521]]]
# It works because the number of files and columns are equal to each other
#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
# The relation it is that value was added by its related vale. For example the 1 of the first line and column was added with 
# with 0.48243756 of the first line and column. 
#12. Multiply a and c. Assign the result to e.
e= np.multiply(a,c)
print(e)
[[[0.48243756 0.60769939 0.9394359  0.02499696 0.38297883]
  [0.83168714 0.17820617 0.26113706 0.91173363 0.42544461]
  [0.51695565 0.39279906 0.16045718 0.99373835 0.94761601]]

 [[0.54569032 0.28936808 0.44554748 0.55145865 0.34810116]
  [0.23238851 0.59683068 0.86837522 0.17014709 0.07568299]
  [0.51551209 0.89084241 0.66576523 0.46479711 0.40983521]]]
#13. Does e equal to a? Why or why not?
e==a
array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])
# It is equal, because every value it is been multiplied by one. Also, it is equal due to files and columns are equals. If
# they had a different shape, it would be possible the multiplication only if the numer of columns of the first equals the
#number of files of the second.
#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max= d.max()
d_min= d.min()
d_mean= d.mean()
​
#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
​
f= np.empty((2, 3, 5))
print(f)
[[[ 25.  75.  75.   0.  25.]
  [ 75.  25.  25.  75.  25.]
  [ 75.  25.  25. 100.  75.]]

 [[ 75.  25.  25.  75.  25.]
  [ 25.  75.  75.  25.  25.]
  [ 75.  75.  75.  25.  25.]]]
"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
​
"\n#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.\nIf a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.\nIf a value equals to d_mean, assign 50 to the corresponding value in f.\nAssign 0 to the corresponding value(s) in f for d_min in d.\nAssign 100 to the corresponding value(s) in f for d_max in d.\nIn the end, f should have only the following values: 0, 25, 50, 75, and 100.\nNote: you don't have to use Numpy in this question.\n"
for a in range (d.shape[0]):
    for b in range (d.shape[1]):
        for c in range (d.shape[2]):
            if d[a, b, c] > d_min and d[a, b, c] < d_mean:
                f[a, b, c]= 25
            elif d[a, b, c] > d_mean and d[a, b, c] < d_max:
                f[a, b, c]=75
            elif d[a, b, c] == d_mean:
                f[a, b, c]= 50
            elif d[a, b, c] == d_min:
                f[a, b, c]= 0
            elif d[a, b, c]== d_max:
                f[a, b, c]=100
​
print(f)
            
[[[ 25.  75.  75.   0.  25.]
  [ 75.  25.  25.  75.  25.]
  [ 75.  25.  25. 100.  75.]]

 [[ 75.  25.  25.  75.  25.]
  [ 25.  75.  75.  25.  25.]
  [ 75.  75.  75.  25.  25.]]]
print(f)
[[[ 25.  75.  75.   0.  25.]
  [ 75.  25.  25.  75.  25.]
  [ 75.  25.  25. 100.  75.]]

 [[ 75.  25.  25.  75.  25.]
  [ 25.  75.  75.  25.  25.]
  [ 75.  75.  75.  25.  25.]]]
f= 
f= f.astype(str)
for a in range (d.shape[0]):
    for b in range (d.shape[1]):
        for c in range (d.shape[2]):
            if d[a, b, c] > d_min and d[a, b, c] < d_mean:
                f[a, b, c]= "A"
            elif d[a, b, c] > d_mean and d[a, b, c] < d_max:
                f[a, b, c]="B"
            elif d[a, b, c] == d_mean:
                f[a, b, c]= "C"
            elif d[a, b, c] == d_min:
                f[a, b, c]= "D"
            elif d[a, b, c]== d_max:
                f[a, b, c]="E"
f
print(f)
[[['A' 'B' 'B' 'D' 'A']
  ['B' 'A' 'A' 'B' 'A']
  ['B' 'A' 'A' 'E' 'B']]

 [['B' 'A' 'A' 'B' 'A']
  ['A' 'B' 'B' 'A' 'A']
  ['B' 'B' 'B' 'A' 'A']]]
# 1. How to get indices of N maximum values in a NumPy array?

Let say we have the following numpy array:
```
import numpy as np

x = np.array([1, 3, 2, 5, 0, -1, 10])
print(f"x: {x}")
```

If we want the indices of N maximum values we could do:
```
N = 3
max_x = np.argsort(-x)[:N]
print(max_x)
```


# 2. Mention the use of // operator in Python?

// is the opetor for integer division (quotient without remainder)

```
10 / 3
```
Would yield to 3.3333333333

When
```
10 // 3
```
Would yield to 3

# 3. What is the difference between a list and a tuple?

Defining a list in Python:
```
mylist = [1, 2, 3, 4]
print(f"mylist: {mylist}")
print(f"type(mylist): {type(mylist)}")
```

Defining a tuple in Python:
```
mytuple = (1, 2, 3, 4)
print(f"mytuple: {mytuple}")
print(f"type(mytuple): {type(mytuple)}")
```

Mutability:
List type in mutable meaning we can change a value
```
mylist[1] = 5
print(f"mylist: {mylist}")
```
When tuple is not mutable, you can try run this line to understand
```
mytuple[1] = 5
```


You can not create a copy of a tuple, but you can create a copy of a list. This
could be a major difference for your algorithms!


# 4. What would be the output of the following?

## 1
```
a = [1,2,3]
b = a
c = [1,2,3]
```
-- 1
```
print(a == b) # True
print(a == c) # True
# a and b are equals => have the same content
```
-- 2
```
print(a is b) # True => a and b point to the same object
print(a is c) # False => a and c do not point to the same object
```
## 2 Looking at the below code, write down the final values of A0, A1, ...An.
```
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
```
If you don't know what zip is don't stress out. No sane employer will expect you to memorize the standard library. Here is the output of help(zip).
```
zip(...)
zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]
```

`A0`: dict mapping letters to integers.

`A1`: iterable from 0 to 9 included.

`A2`: empty list.

`A3`: list of integers from 1 to 5 included.

`A4`: list of integers from 1 to 5 included.

`A5`: dict mapping integers to their squares (keys are 0 to 9).

`A6`: list of lists where the first element are integers from 0 to 9 and the
second elements are the squares.

# 5. Define a class named car with 2 attributes, “color” and “speed”. Then create an instance and return speed.
```
class car():
    def __init__(self, color: str, speed: float):
        self.color = color
        self.speed = speed

ferrari = car(color='red', speed=300)
print(ferrari.speed)
```
# 6. Write a regular expression that will accept an email id. Use the re module.
```
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

def check(email):

    # pass the regular expression
    # and the string in search() method
    if(re.search(regex,email)):
        print("Valid Email")

    else:
        print("Invalid Email")
```

```
check(email="guillaume.simo@hotmail.fr")
check(email="invalidmailahotmail.fr")
check(email="invalidmail@hotmailfr")
check(email="invalidmailhotmail.fr")
```
# 7. If you have to choose between a list, set, and a dictionary to store 10 million integers, what will you use? Bear in mind that you would later like to query the frequency of a number within the dataset.

A set will not work since it keeps the unique values => we would not be able to query the frequency of a number
If it's just 10 millions integers and if there is no key, there is no reason to use a dictionary
I would use a list
```
import time
start = time.time()
mylist = list(range(10**6)) + [1]
from collections import Counter
freq_count = Counter(mylist)
print(freq_count[1])
print(freq_count[4])
print('This costs {:.4f} s.'.format(time.time() - start))
```

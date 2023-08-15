#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fibonacci_generator(n):
    if n <= 0:
        return []

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

n = int(input("Enter the number of Fibonacci numbers you want to generate: "))
fib_numbers = fibonacci_generator(n)
print("Fibonacci Sequence:", fib_numbers)


# In[ ]:





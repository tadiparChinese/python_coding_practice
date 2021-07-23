# The "with" keyword in Python allows you to simplify some code,
# as it will automatically call the __enter__ and __exit__ methods.
# When working with files, it means that the file will automatically be closed after leaving the "with" block.

with open('t.txt','w') as f:
    f.write('Hello, World!')

#it will closed automatically
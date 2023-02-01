'''
In this example, the open_file function is a context manager that opens 
a file and yields a file object. The @contextmanager decorator is used 
to create a context manager from the generator function. The context manager 
is used in a with block, which ensures that the file is automatically closed 
when the block is exited, even if an exception is raised within the block. 
This makes it easy to manage resources that need to be acquired and released, 
without having to worry about the details of resource management.

'''

# Context manager example
from contextlib import contextmanager

@contextmanager
def open_file(file_path, mode):
    f = open(file_path, mode)
    try:
        yield f
    finally:
        f.close()

# Use context manager
with open_file("file.txt", "w") as f:
    f.write("Hello, World!")

# Automatically closes file when the with block is exited

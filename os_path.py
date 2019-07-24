"""

Handling Paths for multiplatforms

Since Windows uses backslash (\) and most OS use forward slash (/), 
There is a common problem when creating code to run over multiplatforms.

A bad approach to solve this is hard code both paths.
e.g. 'folder1/folder2/file.txt' and 'folder1\\folder2\\file.txt'

But how to solve this using Python 3?

There is a famous solution using os.path.join and os.path.abs, 
but a bit verbose and not that much intuitive.

Since Python 3.4, there is a lib called 'pathlib' to help dealing with paths.
The great thing with pathlib is that it will abstract which OS is being used
and convert the representation properly.

Lets check it out for common scenarios.

"""

from pathlib import Path

""" 
    1 - Creating Paths with pathlib 
"""

"""     
1.1 - Getting some useful presets
        - Using function cwd() and home() to help handling paths
"""

curr_dir = Path.cwd()
print('Current Directory: ', curr_dir)

home_dir = Path.home()
print('Home Path: ', home_dir, '\n')

"""     
1.2 - Building inner folder path, inner file path or both 
    - Using function Path(*args) its possible to build OS independent paths
"""

# Some Examples creating generic Paths for any OS
inner_dir = Path(curr_dir, 'first_folder', 'second_folder')
print('Inner Dir Path-1:', inner_dir)

alternative_inner_dir = Path(curr_dir, 'first_folder/second_folder/')
print('Inner Dir Path-2:', alternative_inner_dir, '\n')

inner_file = Path(inner_dir, 'sample.txt')
print('Inner File Path:', inner_file)

# Straight approach with folders and fle
inner_file = Path(curr_dir, 'first_folder', 'second_folder', 'sample.txt')
print('Inner File Straight:', inner_file)

# It is possible to navigate all over path parents
print("Inner File Parent:", inner_file.parent)
print("Inner File Grandparent:", inner_file.parent.parent)

""" 
    2 - Obtaining file attributes from pathlib
    - There is lots of properties can be usefull for different problems
"""
mult_suffix_file = Path(curr_dir, 'first_folder', 'test.ext.log')

print("\nFile Name: ", inner_file.name)
print("File Exists?", inner_file.exists())
print("File Stemming: ", inner_file.stem)
print("File Suffixes: ", mult_suffix_file.suffixes)
print("File Suffix:", mult_suffix_file.suffix)

""" 
    3 - Working with paths 
    - It is possible to use Path objects within file context and similar scenarios
"""

# Read or write to files using Path object can be done with tradicional open
with open(inner_file, mode="r") as inp_file:
    print("\nTraditional:", inp_file.read())

# Pathlib also simplify write and read, 
# But beware, read works equal, but write will overwrite content 
# Since there is no option for edit type:

print("Pathlib Read:", inner_file.read_text())
inner_file.write_text("Thanks for reading!")
print("Pathlib Read After Write:", inner_file.read_text())
inner_file.write_text("Hello Pythonista!")

"""

There is also a bunch of properties that can be obtained from those path objects.
Things like last modified or creation date, content create, rename, delete or replace,
And many more can be found over the documentation page bellow:

- https://docs.python.org/3/library/pathlib.html

Also, There are some helpfull blogposts about pathlib usage:
- https://realpython.com/python-pathlib/#picking-out-components-of-a-path
- https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

Thanks for reading and feel free to contribute or leave some feedback.

"""

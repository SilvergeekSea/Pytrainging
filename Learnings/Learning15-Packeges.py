"""
How to import modules?
1. import x
2. from x import y
3. from x import y as z

Questions:
1. what happened when you import a module? main block concept

def main():
    pass

if __name__ == '__main__':
    main()

main() provides an entry for your module but it's not 100% must to have it.
It should contain some common things which would not be included in other functions.

by using __name__ if for you to separate from run module in REPL or just load in the
memory. Or you execute it with py xxx.py (that should trigger __name__ == __main__)

Everything in Pythno is a statemen, there is no such thing as declaration.
Importing a module means (after some bookkeeping) executing the statements in the module.
Likewise, executing a Python file means importing it as module.
Hence, just writing a program as module level statements works.
However, you do need to put some modules in functions.
You want to only trigger module (not functions in the module) only when you
execute the script not import it. hence, you have

if __name__ == '__main__':
    main()

2. distinguish module execution from module import ?
This is same answer I gave in the above section.


3. What is the Package?
A package is a special type of modules. The definiation of packages is it contains other modules and
other packages.
Package is a way to define hierarchy in the mdoule. To group modules in a special way.
urllib and urllib.request. In this case, urllib is a package and urllib.request is a module with in the urllib.
if you use import xxx.xxx, you can't directly access the module you just imported.

If you use from urllib import request, you are able to directly access the modules you want.
but the result is the same as system knows how to access the module from absolute path.
but how you call module is different base on how you import module.

Packages normally include an attribute __path__ to point out the directory of package.
ie: urllib.__path__ is valid. but urllib.request.__path__ is not. as package (at root level) contains directory
information while modules normaly don't.

Packages are generally directories and files(modules), while modules are generally files.


so when you import a module, Python will search default path for module file.
Python check sys.path object is list of directories. It will check first path with in this object and move on
to the next. First match provides module and stop move on to next path.
if there is no module found and running out the pathes, the importerror will be raised.

so if you install a module, it should show in the sys.path object.

sys.path[0] is a '' (no space). This indicates to instruct Python to search current directory as first directory.

You can use
import sys
sys.path.append('child_diretory') # to add new path to search path. however, it does disappear next time you load REPL
The other way to do it is to

on windows, you can use:
set PYTHONPATH=path1;path2;path3

Those pathes will be imported when sys.path object is created. so it will stay rather than disappear every time.

You can create a folder and have __init__.py in there.
you can actually import the folder as package. When you import the folder, it loads __init__.py.
You can use import folder_name
folder_name.__file__ (I think this is an attribute)

folder_name.__path__ is giving where package is. (folder base)

A package is a directory containing __init__.py.

When you have a package which includes subpackage, the __init__ of root is running first, then execute __init__ of subpackage.


sys.argv[0] contains script name. non-portabl operating system independent format.



Absolute imports

eg:
import demo_reader.compressed.bzipped
from demo_reader.compressed import bzipped

Relative imports syntax (only 1 type)

from ..module_name import name
.. Parent of current module
. Grandparent of current module

Relative imports can only be used to import modules within the current top-level package(not be able to import stuff
outside the current package)

__all__ let's specify which module-level attributes you will import when you do from module_name import * behavior
if it's not specified, then all mmodule level attributes will be imported.
__all__ must be a list of strings. each entry is a name to import.

you can use following to check all attribues.
 from pprint import pprint
 pprint(locals())

__all__ can be useful to limited which name of attributes will be exposed to public



use python -m pip freeze > requirement.txt
pythong -m pip install -r requirement.txt

python -m pip install flask==0.9
python -m pip install 'Django<2.0' (notice it has quote )

if you want to install project with setup.py with in the project
you may download project from github and run
python -m pip install -e flask (this flask is a folder, not fetch from Interenet as module)

python -m pip show flask


pip install --proxy=127.0.0.1:9000 -U virtualenvwrapper-win --trusted-host=pypi.org --trusted-host=files.pythonhosted.org

the default location of environment is
%USERPROFILE%\Envs

workon
workon projectname
deactivate

create a project and a virtualenv and bind them
myproject new_proj
myproject -p python3 new_proj

# Bind an existing project to a virtualenv
# Binds active venv to current working dir
setvirtualenvproject

export WORKON_HOME="/home/rj/envs" # Optional, no space
export PROJECT_HOME="/home/rj/dev" # Needed for mkproject, no space

Configuration
configure location of venvs and projects
by setting environment variables in .profile
WORKON_HOME="/home/rj/envs"
PROJECT_HOME="/home/rj/dev"




"""


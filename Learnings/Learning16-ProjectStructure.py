"""
project_name/
    README.rst  - quick overview
    docs/       - project documentation
    src/
        package_name/
            __init__.py
            more_source.py
            subpackage1/
                __init__.py
    tests/
        test_code.py
    setup.py

Extending Packages with Plugins
Packages define extension points
Extensions are implemented outside the package
extensions are discovered at runtime
    - Namespace packages and pkgutil
    - setuptools entry_points

core package designates subpackages as extension points
then, core package scans subpackages at runtime to discover plugins
plugins augment the nampespace packages extensible
"""
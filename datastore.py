python_interview_questions = [
    # Basics
    "What is Python?",
    "How is Python interpreted?",
    "Explain PEP 8.",
    "What are Python literals?",
    "What is the difference between a list and a tuple?",
    # Data Types
    "Explain mutable and immutable types in Python.",
    "What are the basic data types in Python?",
    "What is the difference between `==` and `is`?",
    "What is the difference between `append()` and `extend()` for lists?",
    "Explain the concept of slicing in Python.",
    # Control Structures
    "What are Python control structures?",
    "Explain the use of `if-elif-else` in Python.",
    "How do you handle exceptions in Python?",
    "What is a `try-except` block?",
    "How does the `for` loop work in Python?",
    # Functions
    "What are functions in Python?",
    "What is the difference between `return` and `yield`?",
    "Explain the concept of lambda functions.",
    "What is a decorator in Python?",
    "What is the purpose of `*args` and `**kwargs`?",
    # Object-Oriented Programming (OOP)
    "What is OOP?",
    "Explain the four pillars of OOP.",
    "What is inheritance?",
    "What is method overriding?",
    "What is the difference between `__init__` and `__new__`?",
    # Modules and Packages
    "What are modules in Python?",
    "Explain the difference between `import` and `from ... import`.",
    "What is a package in Python?",
    "How do you create a module in Python?",
    "How do you install external packages in Python?",
    # File Handling
    "How do you open and close files in Python?",
    "What are the different modes for opening a file?",
    "Explain the use of `with` statement in Python.",
    "What is pickling and unpickling in Python?",
    "How do you read and write JSON data in Python?",
    # Miscellaneous
    "Explain list comprehension.",
    "What is the Global Interpreter Lock (GIL) in Python?",
    "How do you handle multithreading in Python?",
    "What are decorators used for?",
    "What are the differences between Python 2 and Python 3?",
]

python_interview_questions = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    },
    {
        "question": "What are the key features of Python?",
        "answer": "Key features include simplicity, readability, easy syntax, extensive libraries, and high-level data types.",
    },
    {
        "question": "Explain the difference between Python 2 and Python 3.",
        "answer": "Python 2 is legacy and no longer maintained; Python 3 is the current version with several improvements like better Unicode support, syntax enhancements, and more.",
    },
    {
        "question": "What are Python decorators?",
        "answer": "Decorators are functions that modify the behavior of other functions or methods. They allow you to add functionality to an existing function dynamically.",
    },
    {
        "question": "What is the difference between a list and a tuple in Python?",
        "answer": "Lists are mutable (can be changed), while tuples are immutable (cannot be changed after creation).",
    },
    {
        "question": "What is PEP 8?",
        "answer": "PEP 8 is a style guide for Python code, providing guidelines on how to format code for better readability and consistency.",
    },
    {
        "question": "Explain the concept of a generator in Python.",
        "answer": "Generators are functions that can be paused and resumed, allowing you to generate a sequence of values lazily, which saves memory.",
    },
    {
        "question": "What is the difference between '==' and 'is' in Python?",
        "answer": "'==' checks for equality of values, while 'is' checks for identity (if the two variables point to the same object in memory).",
    },
    {
        "question": "How do you handle exceptions in Python?",
        "answer": "Exceptions are handled using try-except blocks. Code that might raise an exception is placed inside the try block, and the handling of the exception occurs in the except block.",
    },
    {
        "question": "Explain the use of `__init__` in Python classes.",
        "answer": "`__init__` is a special method (constructor) in Python classes that gets called when a new instance of the class is created, allowing you to initialize attributes.",
    },
    {
        "question": "What are the different data types in Python?",
        "answer": "Python has various data types including int, float, str, list, tuple, set, dict, bool, etc.",
    },
    {
        "question": "Explain the difference between `append()` and `extend()` methods in Python lists.",
        "answer": "`append()` adds a single element to the end of the list, while `extend()` can add multiple elements by appending each element from an iterable (e.g., another list) to the end of the list.",
    },
    {
        "question": "What are Python modules?",
        "answer": "Modules are files containing Python code. They can define functions, classes, and variables that you can use in other Python scripts.",
    },
    {
        "question": "How can you open and close a file in Python?",
        "answer": "You can open a file using the `open()` function and close it using the `close()` method or by using a context manager (`with` statement).",
    },
    {
        "question": "What is the difference between `__str__()` and `__repr__()` methods in Python?",
        "answer": "`__str__()` is used to return a human-readable string representation of an object, while `__repr__()` is used to generate the official string representation of an object.",
    },
    {
        "question": "Explain list comprehension in Python.",
        "answer": "List comprehension is a concise way to create lists in Python by applying an expression to each item in an iterable.",
    },
    {
        "question": "How can you handle regular expressions in Python?",
        "answer": "Python's `re` module provides support for regular expressions. You can use functions like `search()`, `match()`, `findall()`, etc., to work with regular expressions.",
    },
    {
        "question": "What is the use of `pass` statement in Python?",
        "answer": "`pass` is a null operation that does nothing when executed. It is used as a placeholder where syntactically a statement is required but no action is needed.",
    },
    {
        "question": "Explain the concept of a lambda function.",
        "answer": "Lambda functions, also known as anonymous functions, are small, single-expression functions that don't have a name and are defined using the `lambda` keyword.",
    },
    {
        "question": "What is a virtual environment in Python?",
        "answer": "A virtual environment is a self-contained directory that contains its own Python interpreter and allows you to install and manage packages separately from the system's Python installation.",
    },
    {
        "question": "Explain the concept of inheritance in Python.",
        "answer": "Inheritance is a mechanism in Python that allows a class (subclass/child) to inherit properties and behaviors (methods and attributes) from another class (superclass/parent).",
    },
    {
        "question": "What are the advantages of using Python?",
        "answer": "Advantages include readability, extensive libraries, platform independence, ease of learning, and strong community support.",
    },
    {
        "question": "How can you handle memory management in Python?",
        "answer": "Python uses automatic memory management via garbage collection. The `gc` module provides tools for managing memory.",
    },
    {
        "question": "Explain the use of `*args` and `**kwargs` in Python.",
        "answer": "`*args` is used to pass a variable number of non-keyworded arguments to a function, while `**kwargs` is used to pass a variable number of keyworded arguments to a function.",
    },
    {
        "question": "What is the purpose of the `__init__.py` file in Python?",
        "answer": "`__init__.py` serves as an indicator to Python that a directory should be treated as a package and it can contain initialization code for that package.",
    },
    {
        "question": "How does memory management work in Python?",
        "answer": "Python uses reference counting and a garbage collector. Objects with zero reference counts are automatically deallocated.",
    },
    {
        "question": "What is the Global Interpreter Lock (GIL) in Python?",
        "answer": "The GIL is a mutex that allows only one thread to execute Python bytecode at a time, preventing multiple threads from executing Python code in parallel.",
    },
    {
        "question": "Explain the use of `__name__` and `__main__` in Python.",
        "answer": "`__name__` is a special variable in Python that holds the name of the current module. `__main__` is the name of the top-level script that is being executed.",
    },
    {
        "question": "How can you create a virtual environment in Python?",
        "answer": "You can create a virtual environment using the `venv` module by running `python -m venv <path_to_virtual_env>`.",
    },
    {
        "question": "What is the purpose of the `__doc__` attribute in Python?",
        "answer": "`__doc__` is an attribute that holds the documentation string (docstring) of an object, providing information about the object's purpose and usage.",
    },
    {
        "question": "What is the purpose of `__slots__` in Python classes?",
        "answer": "`__slots__` is used to explicitly declare attributes and allocate space for them in instances, optimizing memory usage and preventing the creation of new attributes.",
    },
    {
        "question": "Explain the difference between a shallow copy and a deep copy in Python.",
        "answer": "A shallow copy creates a new object but inserts references to the original objects. A deep copy creates a completely new object and recursively copies the objects found in the original.",
    },
    {
        "question": "What is a decorator in Python and how do you define one?",
        "answer": "A decorator is a design pattern that allows behavior to be added to an individual object, dynamically. You can define a decorator by using the `@decorator_name` syntax above a function.",
    },
    {
        "question": "How does Python handle memory management and garbage collection?",
        "answer": "Python uses automatic memory management via reference counting and a garbage collector. Objects with zero reference counts are deallocated.",
    },
    {
        "question": "Explain the difference between a module and a package in Python.",
        "answer": "A module is a single file containing Python code, while a package is a directory of modules that contains an `__init__.py` file.",
    },
    {
        "question": "What is the purpose of `__future__` module in Python?",
        "answer": "The `__future__` module allows compatibility of Python code between different versions by providing access to features from future versions of Python.",
    },
    {
        "question": "How can you handle file I/O operations in Python?",
        "answer": "File I/O operations can be performed using built-in functions like `open()`, `read()`, `write()`, and context managers (`with` statement).",
    },
    {
        "question": "Explain the use of `map()` and `filter()` functions in Python.",
        "answer": "`map()` applies a function to every item in an iterable and returns a new iterable. `filter()` creates an iterator that filters elements based on a function returning True.",
    },
    {
        "question": "What is a set in Python and what operations can you perform on it?",
        "answer": "A set is an unordered collection of unique elements. You can perform operations like union, intersection, difference, and more on sets.",
    },
    {
        "question": "How can you handle exceptions and errors in Python?",
        "answer": "Exceptions and errors are handled using try-except blocks. Code that might raise an exception is placed in the try block, and the handling of the exception occurs in the except block.",
    },
    {
        "question": "Explain the difference between `append()` and `insert()` methods in Python lists.",
        "answer": "`append()` adds an element to the end of a list, while `insert()` adds an element at a specific index in the list.",
    },
    {
        "question": "What is the use of the `zip()` function in Python?",
        "answer": "`zip()` takes multiple iterable objects and aggregates them together into a single iterable object, creating tuples of corresponding elements.",
    },
    {
        "question": "Explain the concept of a context manager in Python.",
        "answer": "A context manager in Python allows the allocation and release of resources when used in a `with` statement. It is commonly used for file handling, database connections, etc.",
    },
    {
        "question": "How can you handle default arguments in Python functions?",
        "answer": "Default arguments are specified in the function definition, and if no value is provided during the function call, the default value is used.",
    },
    {
        "question": "What is the purpose of the `*` operator in Python?",
        "answer": "The `*` operator is used for unpacking iterable objects like lists, tuples, etc., into separate elements during function calls or assignments.",
    },
    {
        "question": "Explain the use of the `itertools` module in Python.",
        "answer": "The `itertools` module provides various functions to work with iterators and can be used to create iterators for efficient looping.",
    },
    {
        "question": "What are list comprehensions in Python? Provide an example.",
        "answer": "List comprehensions are concise ways to create lists in Python by applying an expression to each item in an iterable. Example: `[x**2 for x in range(5)]`",
    },
    {
        "question": "What is the purpose of the `super()` function in Python?",
        "answer": "`super()` is used to call methods from the parent class in inheritance and allows access to methods and properties of a superclass.",
    },
    {
        "question": "How can you perform unit testing in Python?",
        "answer": "Python's `unittest` module provides a framework for writing and running tests by creating test cases derived from the `unittest.TestCase` class.",
    },
    {
        "question": "What is the purpose of `__init__` and `__new__` methods in Python?",
        "answer": "`__init__` is the constructor method used to initialize an object after it has been created. `__new__` is a static method that creates an instance of a class before `__init__` is called.",
    },
    {
        "question": "Explain the use of the `with` statement in Python.",
        "answer": "The `with` statement is used for resource management and ensures proper acquisition and release of resources. It simplifies exception handling by automatically closing files, database connections, etc.",
    },
    {
        "question": "What are decorators in Python and why are they used?",
        "answer": "Decorators are functions that modify the behavior of other functions or methods. They are used to add functionality to an existing function dynamically without modifying its code.",
    },
    {
        "question": "How does Python manage memory?",
        "answer": "Python uses automatic memory management through reference counting and a garbage collector. Objects with zero reference counts are automatically deallocated.",
    },
    {
        "question": "What is the purpose of the `sys` module in Python?",
        "answer": "The `sys` module provides access to system-specific parameters and functions, such as interacting with the Python interpreter, command-line arguments, and environment variables.",
    },
    {
        "question": "How can you handle errors and exceptions in Python?",
        "answer": "Errors and exceptions are handled using `try`, `except`, `else`, `finally` blocks. Code that might raise an exception is placed in the `try` block, and the handling of the exception occurs in the `except` block.",
    },
    {
        "question": "Explain the use of Python's `enumerate()` function.",
        "answer": "`enumerate()` is used to loop over an iterable while keeping track of the index and value of each item in the iterable.",
    },
    {
        "question": "Explain the concept of a closure in Python.",
        "answer": "A closure is a nested function that captures and remembers the values from the enclosing (outer) function's scope even after the outer function has finished execution.",
    },
    {
        "question": "What are the differences between a list and a dictionary in Python?",
        "answer": "A list is an ordered collection of elements accessed by index, while a dictionary is an unordered collection of key-value pairs accessed by keys.",
    },
    {
        "question": "How can you handle multiple exceptions in a single except block in Python?",
        "answer": "You can handle multiple exceptions by placing them in a tuple within a single except block. For example: `except (Exception1, Exception2):`",
    },
    {
        "question": "Explain the purpose of the `__call__` method in Python classes.",
        "answer": "`__call__` allows an instance of a class to be called as a function. It is executed when the instance is called using the function call syntax.",
    },
    {
        "question": "What are the differences between Python's `range()` and `xrange()` functions?",
        "answer": "`range()` returns a list of numbers while `xrange()` returns an xrange object, which is more memory-efficient as it generates numbers on the fly.",
    },
    {
        "question": "Explain the use of `is` and `==` operators in Python.",
        "answer": "`is` checks for identity (if two variables point to the same object), while `==` checks for equality (if the values of two variables are equal).",
    },
    {
        "question": "What is the purpose of the `functools` module in Python?",
        "answer": "The `functools` module provides higher-order functions and operations on callable objects, especially functions and decorators.",
    },
    {
        "question": "How can you handle JSON data in Python?",
        "answer": "Python's `json` module provides functions to encode Python objects as JSON strings and decode JSON strings into Python objects.",
    },
    {
        "question": "What is a metaclass in Python?",
        "answer": "A metaclass is the class of a class. It defines how a class behaves and is used to create classes dynamically.",
    },
    {
        "question": "Explain the difference between `__getattr__` and `__getattribute__` in Python.",
        "answer": "`__getattr__` is called when an attribute lookup fails, while `__getattribute__` is called for every attribute access. `__getattribute__` is a built-in method that is always called, whereas `__getattr__` is called only if the attribute is not found through the normal ways.",
    },
    {
        "question": "What are decorators in Python and how do they work?",
        "answer": "Decorators are functions that modify the behavior of other functions or methods. They allow additional functionality to be added to an existing function dynamically without changing its code by wrapping it inside another function.",
    },
    {
        "question": "Explain the purpose of the `*args` and `**kwargs` in Python function definitions.",
        "answer": "`*args` and `**kwargs` allow a function to accept a variable number of positional and keyword arguments, respectively. `*args` collects extra positional arguments into a tuple, and `**kwargs` collects extra keyword arguments into a dictionary.",
    },
    {
        "question": "Explain the difference between `__str__` and `__repr__` in Python.",
        "answer": "`__str__` is used to provide a human-readable string representation of an object and is called by the `str()` function. `__repr__` is used to provide an unambiguous string representation of an object and is called by the `repr()` function.",
    },
    {
        "question": "What is the purpose of the `asyncio` module in Python?",
        "answer": "The `asyncio` module provides infrastructure for writing single-threaded concurrent code using coroutines, allowing asynchronous I/O operations in Python.",
    },
    {
        "question": "What are the differences between a list comprehension and a generator expression in Python?",
        "answer": "A list comprehension produces a list as its result, while a generator expression produces a generator object that generates values lazily.",
    },
    {
        "question": "How can you handle file I/O operations asynchronously in Python?",
        "answer": "You can use the `asyncio` module in conjunction with asynchronous file I/O functions like `asyncio.open()` to perform file operations asynchronously.",
    },
    {
        "question": "Explain the purpose of the `collections` module in Python.",
        "answer": "The `collections` module provides specialized container datatypes beyond the built-in types (list, tuple, dict, etc.), such as `namedtuple()`, `Counter`, `deque`, etc.",
    },
    {
        "question": "What is the purpose of the `*args` and `**kwargs` in Python function definitions?",
        "answer": "`*args` and `**kwargs` allow a function to accept a variable number of positional and keyword arguments, respectively.",
    },
    {
        "question": "Explain the concept of a closure in Python.",
        "answer": "A closure is a nested function that captures and remembers the values from the enclosing (outer) function's scope even after the outer function has finished execution.",
    },
    {
        "question": "What is a decorator in Python?",
        "answer": "A decorator is a design pattern that allows behavior to be added to an individual object, dynamically. You can define a decorator by using the `@decorator_name` syntax above a function.",
    },
    {
        "question": "What is the purpose of the `*args` and `**kwargs` in Python function definitions?",
        "answer": "`*args` and `**kwargs` allow a function to accept a variable number of positional and keyword arguments, respectively.",
    },
    {
        "question": "What are list comprehensions in Python?",
        "answer": "List comprehensions are concise ways to create lists in Python by applying an expression to each item in an iterable.",
    },
    {
        "question": "What is the purpose of the `itertools` module in Python?",
        "answer": "The `itertools` module provides various functions to work with iterators and can be used to create iterators for efficient looping.",
    },
    {
        "question": "What is the purpose of the `os` module in Python?",
        "answer": "The `os` module provides functions to interact with the operating system, allowing you to perform tasks like file operations, environment variables, and process management.",
    },
    {
        "question": "Explain the use of Python's `map()` function.",
        "answer": "`map()` applies a function to every item in an iterable and returns a new iterable.",
    },
    {
        "question": "What are tuples in Python?",
        "answer": "Tuples are immutable sequences of elements. They are similar to lists but cannot be changed after creation.",
    },
    {
        "question": "Explain the purpose of the `datetime` module in Python.",
        "answer": "The `datetime` module provides classes to work with dates and times in Python, allowing operations like parsing, formatting, and arithmetic.",
    },
    {
        "question": "What is the purpose of the `json` module in Python?",
        "answer": "The `json` module provides functions to encode Python objects as JSON strings and decode JSON strings into Python objects.",
    },
    {
        "question": "Explain the use of the `try`, `except`, `finally` blocks in Python.",
        "answer": "`try`, `except`, `finally` blocks are used for exception handling in Python. Code that might raise an exception is placed in the try block, and the handling of the exception occurs in the except block. The finally block is used to execute code whether an exception occurs or not.",
    },
    {
        "question": "What is the purpose of the `zip()` function in Python?",
        "answer": "`zip()` takes multiple iterable objects and aggregates them together into a single iterable object, creating tuples of corresponding elements.",
    },
    {
        "question": "What is the purpose of the `os.path` module in Python?",
        "answer": "`os.path` module provides functions for common pathname manipulation tasks, such as joining paths, checking existence, splitting paths, and more.",
    },
    {
        "question": "What is a set in Python?",
        "answer": "A set is an unordered collection of unique elements. It does not allow duplicate elements.",
    },
    {
        "question": "Explain the use of Python's `filter()` function.",
        "answer": "`filter()` creates an iterator that filters elements based on a function returning True.",
    },
    {
        "question": "What is the purpose of the `collections` module in Python?",
        "answer": "The `collections` module provides specialized container datatypes beyond the built-in types (list, tuple, dict, etc.), such as `namedtuple()`, `Counter`, `deque`, etc.",
    },
    {
        "question": "What is the purpose of the `enumerate()` function in Python?",
        "answer": "`enumerate()` is used to loop over an iterable while keeping track of the index and value of each item in the iterable.",
    },
    {
        "question": "What is the purpose of the `staticmethod` decorator in Python?",
        "answer": "`staticmethod` is used to define a static method in a class. Static methods belong to the class and not the instance, and they can be called on the class itself.",
    },
    {
        "question": "Explain the purpose of the `math` module in Python.",
        "answer": "The `math` module provides mathematical functions and constants, such as trigonometric functions, logarithmic functions, constants like pi and e, etc.",
    },
    {
        "question": "What is the purpose of the `re` module in Python?",
        "answer": "The `re` module provides support for regular expressions in Python, allowing pattern matching and search operations in strings.",
    },
    {
        "question": "Explain the use of the `super()` function in Python.",
        "answer": "`super()` is used to call methods from the parent class in inheritance and allows access to methods and properties of a superclass.",
    },
    {
        "question": "What is the purpose of the `time` module in Python?",
        "answer": "The `time` module provides functions to work with time-related functions, such as getting the current time, converting between different time formats, and more.",
    },
    {
        "question": "Explain the concept of an iterable and an iterator in Python.",
        "answer": "An iterable is an object that can be looped over (like lists, tuples). An iterator is an object that represents a stream of data and implements the `__iter__()` and `__next__()` methods.",
    },
    {
        "question": "What are list slicing and how is it performed in Python?",
        "answer": "List slicing allows you to access a portion of a list. It is performed by specifying the start, end, and step size using the syntax `list[start:end:step]`.",
    },
    {
        "question": "Explain the purpose of the `pickle` module in Python.",
        "answer": "The `pickle` module is used for serializing and deserializing Python objects, allowing objects to be saved to a file and loaded back into the program.",
    },
    {
        "question": "What is a namespace in Python?",
        "answer": "A namespace in Python is a system that ensures that all the names in a program are unique and can be used without any conflict. It helps in organizing the code and avoids naming collisions.",
    },
    {
        "question": "Explain the purpose of the `isinstance()` function in Python.",
        "answer": "`isinstance()` is used to check if an object is an instance of a specified class or any subclass thereof.",
    },
    {
        "question": "What is the purpose of the `del` statement in Python?",
        "answer": "`del` is used to remove references to objects, allowing them to be garbage collected. It can also be used to delete items from lists, dictionaries, etc.",
    },
    {
        "question": "Explain the concept of a decorator in Python.",
        "answer": "Decorators are functions that modify the behavior of other functions or methods. They allow you to add functionality to an existing function dynamically.",
    },
    {
        "question": "What is the purpose of `__init__` in Python classes?",
        "answer": "`__init__` is a special method (constructor) in Python classes that gets called when a new instance of the class is created, allowing you to initialize attributes.",
    },
    {
        "question": "What are list comprehensions in Python?",
        "answer": "List comprehensions are a concise way to create lists in Python by applying an expression to each item in an iterable.",
    },
    {
        "question": "Explain the purpose of the `global` keyword in Python.",
        "answer": "The `global` keyword is used inside functions to declare that a variable is in the global scope, allowing modification of the global variable within the function.",
    },
    {
        "question": "Explain the purpose of the `map()` function in Python.",
        "answer": "`map()` applies a function to every item in an iterable and returns a new iterable with the results.",
    },
    {
        "question": "What is the purpose of the `__str__()` method in Python?",
        "answer": "`__str__()` is a special method in Python classes that returns a string representation of an object, intended for end-users.",
    },
    {
        "question": "Explain the use of `*` operator in Python.",
        "answer": "The `*` operator is used for unpacking iterable objects like lists, tuples, etc., into separate elements during function calls or assignments.",
    },
    {
        "question": "What is the purpose of the `sorted()` function in Python?",
        "answer": "`sorted()` is used to sort an iterable and return a new sorted list, preserving the original iterable.",
    },
    {
        "question": "How do you perform string formatting in Python?",
        "answer": "String formatting in Python can be done using `%` operator, `str.format()` method, or f-strings (formatted string literals).",
    },
    {
        "question": "Explain the use of `try`, `except`, `finally` blocks in Python.",
        "answer": "`try` block is used to execute code that might raise an exception. `except` block catches and handles the exceptions. `finally` block is executed regardless of whether an exception occurred or not.",
    },
    {
        "question": "What is the purpose of the `elif` statement in Python?",
        "answer": "`elif` is short for 'else if' and is used to check multiple conditions after an initial `if` statement. If the `if` condition is false, `elif` conditions are checked one by one.",
    },
    {
        "question": "What is the purpose of the `continue` statement in Python?",
        "answer": "`continue` is used inside loops to skip the current iteration and continue with the next iteration of the loop.",
    },
    {
        "question": "How can you remove duplicates from a list in Python?",
        "answer": "You can remove duplicates from a list by converting it to a set (which doesn't allow duplicates) and then converting it back to a list.",
    },
    {
        "question": "Explain the purpose of the `random` module in Python.",
        "answer": "The `random` module in Python provides functions to generate random numbers, shuffle sequences, and choose random elements.",
    },
    {
        "question": "What is the purpose of the `pop()` method in Python lists?",
        "answer": "`pop()` method removes and returns the element at the specified index from a list. If no index is specified, it removes and returns the last element.",
    },
]

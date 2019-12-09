# Python-Cpp-wrapper

Python C++ very simple wrapper, easy to use, just clone it and use its structure.

Run bash_compile and python pytest.py to test!

    # Creates an object
    obj = Test()

    # Show greetings from C++
    obj.greetings()

    # Allocate space on memory, pass the pointer to C++ and print the array values
    array_test = np.linspace(1, 10, 10, dtype=np.uint8)
    obj.input_array(array_test)
    print(obj.output_array())

    # Changes the values of the array inside C++ and print the new array
    print("+ 10 =")
    obj.array_sum(10)
    print(obj.output_array())

    # Inputs a boolean value into C++ and gets the value back
    obj.input_bool(True)
    print(obj.output_bool())

    # Inputs a float variable into C++ and gets the value back
    obj.input_float(1.0000)
    print(obj.output_float())

    # Inputs a integer variable into C++ and gets the value back
    obj.input_int(100)
    print(obj.output_int())
    
# Output
```
Hello from C++, today is Aug  7 2018!
[ 1  2  3  4  5  6  7  8  9 10]
+ 10 =
[11 12 13 14 15 16 17 18 19 20]
True
1.0
100
```

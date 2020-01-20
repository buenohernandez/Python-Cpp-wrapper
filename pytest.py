import ctypes
lib = ctypes.cdll.LoadLibrary('./libtest.so')

class Test(object):
    def __init__(self):
        lib.test_new.restype = ctypes.c_void_p
        self.obj = ctypes.c_void_p(lib.test_new())


    def greetings(self): # Show greetings from C++
        lib.test_greetings(self.obj) # Note: these functions are declared on the bottom of test.cpp


    def input_array(self, array): # Creates a pointer and passes it to C++ object, along with its size
        self.array = array
        self.pointer = self.array.ctypes.data_as(ctypes.POINTER(ctypes.c_char)) # Casts it as char
        lib.test_input_array(self.obj, self.pointer, array.size)
        # Note: if you plan only to receive arrays from C++, passing the pointer is only necessary once


    def array_sum(self, value): # Changes the values of the array inside C++
        lib.test_array_sum(self.obj, value)


    def input_bool(self, boolean):  # Inputs a boolean value into C++ object
        lib.test_input_bool(self.obj, ctypes.c_bool(boolean)) # Data type specification


    def input_float(self, float_var):   # Inputs a float value into C++ object
        lib.test_input_float(self.obj, ctypes.c_float(float_var)) # Data type specification


    def input_int(self, integer):   # Inputs an integer value into C++ object
        lib.test_input_int(self.obj, integer)


    def output_array(self): # Outputs the array inside the C++ object
        return self.array # Since we're dealing with pointers, changing the value inside the C++ object also changes here!


    def output_bool(self):  # Outputs the boolean variable inside the C++ object
        lib.test_output_bool.restype = ctypes.c_bool # Data type specification
        return lib.test_output_bool(self.obj)


    def output_float(self): # Outputs the float variable inside the C++ object
        lib.test_output_float.restype = ctypes.c_float # Data type specification
        return lib.test_output_float(self.obj)


    def output_int(self): # Outputs the integer variable inside the C++ object
        return lib.test_output_int(self.obj)


if __name__ == "__main__":

    import numpy as np

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


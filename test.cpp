#include <iostream>
#include <stdint.h>

using namespace std;

class Test{

    private:

        uint8_t * pointer; // Variable to store the pointer
        int size; // Variable to store the size of the array
        bool boolean; // Variable to store the boolean
        float float_var; // Variable to store the float
        int integer; // Variable to store the integer

    public:

        void greetings();
        void input_array(uint8_t * python_pointer, int array_size); // Gets the pointer along with its size from Python
        void array_sum(int value); // Changes the values of the array stored
        void input_bool(bool python_bool); // Gets the boolean variable input
        void input_float(float python_float); // Gets the float variable input
        void input_int(int python_int); // Gets the integer variable input
        bool output_bool(); // Returns the boolean variable
        float output_float(); // Returns the float variable
        int output_int(); // Returns the integer variable

};

void Test::greetings(){

  cout << "Hello from C++, today is " << __DATE__ << "!" << endl;

}

// Gets the pointer along with its size from Python
void Test::input_array(uint8_t * python_pointer, int array_size){

    this->pointer = python_pointer;
    this->size = array_size;
}

// Changes the values of the array stored
void Test::array_sum(int value){

    for(unsigned int i = 0; i < this->size; i++){

        this->pointer[i] = this->pointer[i] + value;

    }

}

// Gets the boolean variable input
void Test::input_bool(bool python_bool){

    this->boolean = python_bool;

}

// Gets the float variable input
void Test::input_float(float python_float){

    this->float_var = python_float;

}

// Gets the integer variable input
void Test::input_int(int python_int){

    this->integer = python_int;

}

// Returns the boolean variable
bool Test::output_bool(){

    return boolean;

}

// Returns the float variable
float Test::output_float(){

    return float_var;

}

// Returns the integer variable
int Test::output_int(){

    return integer;

}


// Exposes the functions
extern "C" {

   	Test* test_new(){ return new Test(); }
    void test_greetings(Test * test){test->greetings();}
    void test_input_array(Test * test, uint8_t * python_pointer, int array_size){test->input_array(python_pointer, array_size);}
    void test_array_sum(Test * test, int value){test->array_sum(value);}
    void test_input_bool(Test * test, bool boolean){test->input_bool(boolean);}
    void test_input_float(Test * test, float float_var){test->input_float(float_var);}
    void test_input_int(Test * test, int integer){test->input_int(integer);}
    bool test_output_bool(Test * test){test->output_bool();}
    float test_output_float(Test * test){test->output_float();}
    int test_output_int(Test * test){test->output_int();}

}


#include <iostream> // Including the input-output stream library for using cout

using namespace std; // Using the standard namespace to avoid writing std:: before cout and cin

int main() // Main function where execution begins
{
    int a = 15, b = 2; // Declaring two integer variables 'a' and 'b', and initializing them with values

    // Performing arithmetic operations and printing the results

    cout << "Sum: " << a + b << endl;        // Printing the sum of a and b
    cout << "Difference: " << a - b << endl; // Printing the difference between a and b
    cout << "Product: " << a * b << endl;    // Printing the product of a and b
    cout << "Quotient: " << a / b << endl;   // Printing the quotient (integer division) of a and b
    cout << "Remainder: " << a % b << endl;  // Printing the remainder of the division of a by b

    return 0; // Returning 0 to indicate successful program execution
}

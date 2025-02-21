#include <iostream>  // Including the input-output stream library for using cin and cout

using namespace std;  // Using the standard namespace to avoid writing std:: before cout and cin

int main()  // Main function where execution begins
{
    string name; // String variable to store the user's name
    int age;     // Integer variable to store the user's age

    // Asking the user for their name
    cout << "Enter your name: ";
    cin >> name;  // Reading the input name from the user

    // Asking the user for their age
    cout << "Enter your age: ";
    cin >> age;   // Reading the input age from the user

    // Displaying a personalized message with the user's name and age
    cout << "Hello, " << name << "! You are " << age << " years old." << endl;

    return 0;  // Returning 0 to indicate successful program execution
}

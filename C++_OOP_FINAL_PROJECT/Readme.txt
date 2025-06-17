Attendance Analyzer - C++ Project
...................................

Purpose
........

This program helps analyze student attendance records. It allows the user to add and remove attendance entries, view records, and apply two types of analysis:

PercentAnalyzer: Calculates overall attendance percentage.
TrendAnalyzer: Detects if there's a downward trend in attendance.

This project demonstrates:
...........................

|Use of dynamic arrays
|Abstract classes and polymorphism
|Pointer arithmetic
|Memory management
|Interactive console-based interface

Features
.........

|Add new attendance records (ID, name, date, present/absent)
|Remove records by index
|Display all attendance records
|Analyze attendance using polymorphic analyzers

Code Explanation (Line by Line)
................................

1. Structs
...........

struct Date { int day, month, year; };          // Represents a calendar date
struct Attendance {
    char studentID[10];                         // Unique student ID
    char studentName[50];                       // Full student name
    Date* date;                                 // Pointer to date
    bool present;                               // True if present, false if absent
};

2. Abstract Base Class
.......................

class Analyzer {
public:
    virtual float analyze(const Attendance*, int) = 0;  // Pure virtual function
    virtual const char* name() const = 0;               // Returns analyzer name
    virtual ~Analyzer() {}                              // Virtual destructor
};

3. Derived Analyzers
......................

class PercentAnalyzer : public Analyzer {
    float analyze(...) { /* Calculates presence % */ }
};

class TrendAnalyzer : public Analyzer {
    float analyze(...) { /* Detects drops in attendance */ }
};

4. Adding Records
....................

void addAttendance(...) {
    // Input student ID and name
    // Input date and presence status
    // Resize array dynamically
}

5. Removing Records
.....................

void removeAttendance(...) {
    // Delete date pointer
    // Resize array excluding removed record
}

6. Display Records
....................

void displayRecords(...) {
    // Show index, ID, name, date, and status
}

7. Main Function
..................

int main()
This is the entry point of every C++ program.

Attendance* recs = nullptr;
Declares a dynamic array of Attendance records.

nullptr means no memory is allocated yet (empty list).

int count = 0;

Keeps track of how many attendance records exist.

Used during resizing and iteration.

Analyzer** analyzers = new Analyzer*[2];
Dynamically allocates an array of pointers to Analyzer objects.

Analyzer is an abstract base class, so we store the analyzers in polymorphic form.

analyzers[0] = new PercentAnalyzer;
analyzers[1] = new TrendAnalyzer;
These two lines create concrete analyzer objects:

PercentAnalyzer: calculates total % present.

TrendAnalyzer: detects attendance drops.

Purpose: Polymorphism
Now we can do:

analyzers[i]->analyze(recs, count);
Even though they're different types, we treat them uniformly via the base class pointer.

int choice; do { ... } while (choice != 0);
A do-while loop for the main menu.

Repeats until the user enters 0 to exit.

Menu Display and Choice Input

cout << "Attendance Analyzer Menu";
...
cin >> choice;
Prints the options and reads user choice.

switch (choice)
Handles the user’s menu input:

case 1: addAttendance(recs, count);
Adds a new attendance record.

Dynamically resizes recs and increments count.

case 2:

int index;
cout << "Enter index to remove: ";
cin >> index;
removeAttendance(recs, count, index);
Removes a record by index (if valid).

Also deletes the memory used by that record’s date.

case 3: displayRecords(recs, count);
Shows all attendance records with student ID, name, date, and presence status.

case 4:

for (int i = 0; i < 2; ++i) {
    float result = analyzers[i]->analyze(recs, count);
    cout << analyzers[i]->name() << ": " << result << "%\n";
}
Polymorphism in action:

Calls the correct analyze() method (either Percent or Trend).

Uses Analyzer* to invoke the actual overridden method.

Outputs results like:

Percentage Analyzer: 80%
Trend Analyzer: 33.33%
case 0: Exit message.

cout << "Goodbye!";
Ends the loop and program.

default:
Handles invalid menu input:

cout << "Invalid option!";
Memory Cleanup
After exiting the loop, clean up all dynamic memory to avoid leaks.

Delete Date pointers in each record:

for (int i = 0; i < count; ++i)
    delete recs[i].date;
Delete the attendance array:

delete[] recs;
Delete the analyzers:

for (int i = 0; i < 2; ++i)
    delete analyzers[i];
delete[] analyzers;
✅ return 0;
Signals successful program exit to the OS.

SAMPLE MENU OUTPUT:
...................

Attendance Analyzer Menu
1. Add Attendance
2. Remove Attendance
3. Show All Records
4. Analyze Attendance
0. Exit
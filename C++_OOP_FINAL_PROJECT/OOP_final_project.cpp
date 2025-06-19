#include <iostream>
#include <cstring>

using namespace std;

struct Date {
    int day, month, year;
};

struct Attendance {
    char studentID[10];
    char studentName[50];
    Date* date;
    bool present;
};

class Analyzer {
public:
    virtual float analyze(const Attendance* recs, int n) = 0;
    virtual const char* name() const = 0;
    virtual ~Analyzer() {}
};

class PercentAnalyzer : public Analyzer {
public:
    float analyze(const Attendance* recs, int n) override {
        int presentCount = 0;
        for (int i = 0; i < n; ++i)
            if ((recs + i)->present) presentCount++;
        return (n == 0) ? 0.0f : (float)presentCount / n * 100;
    }
    const char* name() const override { return "Percentage Analyzer"; }
};

class TrendAnalyzer : public Analyzer {
public:
    float analyze(const Attendance* recs, int n) override {
        if (n < 2) return 0.0f;
        int drops = 0;
        for (int i = 1; i < n; ++i)
            if ((recs + i - 1)->present && !(recs + i)->present)
                drops++;
        return (float)drops / (n - 1) * 100;
    }
    const char* name() const override { return "Trend Analyzer"; }
};

void addAttendance(Attendance*& recs, int& n) {
    Attendance newRec;
    cout << "Enter student ID: ";
    cin >> newRec.studentID;
    cin.ignore();
    cout << "Enter student name: ";
    cin.getline(newRec.studentName, 50);

    newRec.date = new Date;
    cout << "Enter date (DD MM YYYY): ";
    cin >> newRec.date->day >> newRec.date->month >> newRec.date->year;

    char p;
    cout << "Was student present? (y/n): ";
    cin >> p;
    newRec.present = (p == 'y' || p == 'Y');

    Attendance* newArray = new Attendance[n + 1];
    for (int i = 0; i < n; ++i)
        *(newArray + i) = *(recs + i);
    *(newArray + n) = newRec;

    delete[] recs;
    recs = newArray;
    n++;
}

void removeAttendance(Attendance*& recs, int& n, int index) {
    if (index < 0 || index >= n) {
        cout << "Invalid index!\n";
        return;
    }

    delete recs[index].date;

    Attendance* newArray = new Attendance[n - 1];
    for (int i = 0, j = 0; i < n; ++i) {
        if (i == index) continue;
        *(newArray + j) = *(recs + i);
        j++;
    }

    delete[] recs;
    recs = newArray;
    n--;
    cout << "Attendance removed!\n";
}

void displayRecords(const Attendance* recs, int n) {
    if (n == 0) {
        cout << "No records to display.\n";
        return;
    }
    for (int i = 0; i < n; ++i) {
        cout << i << ". " << (recs + i)->studentID
             << " - " << (recs + i)->studentName
             << " | " << (recs + i)->date->day << "/"
             << (recs + i)->date->month << "/"
             << (recs + i)->date->year
             << " | " << ((recs + i)->present ? "Present" : "Absent") << "\n";
    }
}

int main() {
    Attendance* recs = nullptr;
    int count = 0;

    Analyzer** analyzers = new Analyzer*[2];
    analyzers[0] = new PercentAnalyzer;
    analyzers[1] = new TrendAnalyzer;

    int choice;
    do {
        cout << "\nAttendance Analyzer Menu\n";
        cout << "1. Add Attendance\n";
        cout << "2. Remove Attendance\n";
        cout << "3. Show All Records\n";
        cout << "4. Analyze Attendance\n";
        cout << "0. Exit\n";
        cout << "Select: ";
        cin >> choice;

        switch (choice) {
        case 1:
            addAttendance(recs, count);
            break;
        case 2:
            int index;
            cout << "Enter index to remove: ";
            cin >> index;
            removeAttendance(recs, count, index);
            break;
        case 3:
            displayRecords(recs, count);
            break;
        case 4:
            for (int i = 0; i < 2; ++i) {
                float result = analyzers[i]->analyze(recs, count);
                cout << analyzers[i]->name() << ": " << result << "%\n";
            }
            break;
        case 0:
            cout << "Goodbye!\n";
            break;
        default:
            cout << "Invalid option!\n";
        }
    } while (choice != 0);

    for (int i = 0; i < count; ++i)
        delete recs[i].date;
    delete[] recs;

    for (int i = 0; i < 2; ++i)
        delete analyzers[i];
    delete[] analyzers;

    return 0;
}
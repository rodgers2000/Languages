//**************************************************
//           ProgLabStructs Assignment
//    COSC 1437 - Instructor Derakhshandeh
//              Michael Rodgers
//             Due Date: 6/19/17
//
//  Summary:
//
//  This program gathers data about the student from
//  the user and calculations the student's letter
//  grade. It uses a structure to accomplish this.
//**************************************************

    // Header files
#include <iostream> // Used for cout, cin, fixed
#include <string>   // Used for strings
#include <iomanip>  // Used for setprecision

using namespace std;

    // Define Student structure
struct Student {
        // Declare strings:
    string studFirstName;
    string studLastName;
        // Declare integers:
    int studExam1;
    int studExam2;
    int studExam3;
        // Declare doubles:
    double studAvg;             // Average can be a rational number.
        // Declare characters:
    char studGrade;
};

int main(){
        // Declare variables:
    Student michael;            // michael is a Student structure
    int studScore;              // studScore is an integer variable
    
        // Get data from user:
        // first name
    cout << "Enter student first name: ";
    getline(cin, michael.studFirstName);
        // last name
    cout << "Enter student last name: ";
    getline(cin, michael.studLastName);
        // exam 1
    cout << "Enter score for exam 1: ";
    cin  >> michael.studExam1;
        // exam 2
    cout << "Enter score for exam 2: ";
    cin  >> michael.studExam2;
        // exam 3
    cout << "Enter score for exam 3: ";
    cin  >> michael.studExam3;
    
        // Calculate michael's average:
    
    studScore = michael.studExam1 + michael.studExam2 + michael.studExam3;
    
    michael.studAvg = studScore / 3.0; // Since average can be a double, we need to
                                       // factor this in. Integer / double = double.
    
        // Calculate michael's final grade:
    
    cout << "Student's Final Grade: ";
    
        // Start logical branch
    if (michael.studAvg >= 90)
        michael.studGrade = 'A';
    else if (michael.studAvg >= 80)
        michael.studGrade = 'B';
    else if (michael.studAvg >= 70)
        michael.studGrade = 'C';
    else if (michael.studAvg >= 60)
        michael.studGrade = 'D';
    else
        michael.studGrade = 'F';
    
        // Set precision to 2 decimal places
    cout << fixed << setprecision(2);
        // Display michael's final grade
    cout << michael.studGrade << endl;

    // system pause!!!!!
    
}


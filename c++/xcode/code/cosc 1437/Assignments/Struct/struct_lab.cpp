//**************************************************
//           ProgLabStructs Assignment
//    COSC 1437 - Instructor Derakhshandeh
//              Michael Rodgers
//             Due Date: 6/19/17
//**************************************************

 #include <iostream>
 #include <iomanip>
 using namespace std;

 const int SIZE = 25; // Array size 7
 struct PayRoll{
     int empNumber; // Employee number
     char name[SIZE]; // Employee's name
     double hours; // Hours worked
     double payRate; // Hourly pay rate
     double grossPay; // Gross pay
     };

int main(){
    PayRoll employee; // employee is a PayRoll structure.
    
    // Get the employee's number.
    cout << "Enter the employee's number: ";
    cin >> employee.empNumber;
    // Get the employee's name.
    cout << "Enter the employee's name: ";
    cin.ignore(); // To skip the remaining '\n' character
    cin.getline(employee.name, SIZE);

    // Get the hours worked by the employee.
    cout << "How many hours did the employee work? ";
    cin >> employee.hours;
    
    // Get the employee's hourly pay rate.
    cout << "What is the employee's hourly pay rate? ";
    cin >> employee.payRate;

    // Calculate the employee's gross pay.
    employee.grossPay = employee.hours * employee.payRate;
    // Display the employee data.
    cout << "Here is the employee's payroll data:\n";
    cout << "Name: " << employee.name << endl;
    cout << "Number: " << employee.empNumber << endl;
    cout << "Hours worked: " << employee.hours << endl;
    cout << "Hourly pay rate: " << employee.payRate << endl;
    cout << fixed << showpoint << setprecision(2);
    cout << "Gross pay: $" << employee.grossPay << endl;
    return 0;
    }

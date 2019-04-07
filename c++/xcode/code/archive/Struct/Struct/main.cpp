//
//  main.cpp
//  Struct
//
//  Created by Michael Rodgers on 6/10/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

struct Name {
    string first;
    string middle;
    string last;
};
    

struct Employee {
    short id;
    int age;
    double wage;
    // Constructor
    Employee(short i = 0, int a = 9, double w = 50000);
    // This yields default values
    // Functions. You can define functions inside struct.
    // The functions modify the values without passing by reference
    bool verify(int);
    void payRaise(int);
};

// Writing the contructor details outside of struct
Employee::Employee(short i, int a, double w){
    id = i; age = a; wage = w;
}
// Define functions that are in the struct
bool Employee::verify(int i){
    return id == i;
}

void Employee::payRaise(int raise){
    wage += raise;
}


void printInfoEmployee(Employee employee);
void printName(Name &name);

int main(){
    
    // Three ways to define a new struct variable
    /* 1. */ Employee mike = { 12345, 21, 500000.00 };
    printInfoEmployee(mike);
    
    /* 2. */ Employee brett = mike;
    printInfoEmployee(brett);
    
    /* 3. */ Employee kevin(420, 25, 20000);
    printInfoEmployee(kevin);
    
    // These are two ways to use the contructor
    /* 1. */ Employee philphil = Employee::Employee(6969, 6, 10000);
    printInfoEmployee(philphil);
    
    // This is the default value
    /* 2. */ Employee person = Employee::Employee();
    printInfoEmployee(person);
    
    // This is the NAME struct
    Name mjr = {"mike", "james", "rodgers"};
    printName(mjr);
    
    // This is verifying id. 1 equals true. 0 equals false.
    cout << mike.verify(12345) << endl;
    
    // Let's give mike a pay raise
    mike.payRaise(69);
    
    cout <<  mike.wage << endl;
    
    // Array of structs
    
    Name array [10];
    // Loop through array of structs
    for (int index=0; index < 10; index++) {
        array[index].first = "mike";
        cout << array[index].first << " ";
    }
    
}

void printInfoEmployee(Employee employee){
    cout << employee.id << endl;
    cout << employee.age << endl;
    cout << employee.wage << endl;
}

void printName(Name &name){ // Pass struct by reference
    cout << name.first << endl;
    cout << name.middle << endl;
    cout << name.last << endl;
}

//
//  main.cpp
//  Polymorphism and Virtual Functions
//
//  Created by Michael Rodgers on 7/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//
// This demonstrates the polymorphic behavior
// of classes with virtual functions.

#include <iostream>
#include <string>

using namespace std;

enum Discipline { ARCHEOLOGY, BIOLOGY, COMPUTER_SCIENCE };
enum Classification { FRESHMAN, SOPHOMORE, JUNIOR, SENIOR };

// The Person class is modified to make getName
// a virtual function.
class Person{
protected:
    string name;
public:
    Person() { setName(""); }
    Person(string pName) { setName(pName); }
    void setName(string pName) { name = pName; }
    
    // Virtual function.
    virtual string getName() { return name; }
};

class Student:public Person
{
private:
    Discipline major;
    Person *advisor;
public:
    Student(string sname, Discipline d, Person *adv)
    : Person(sname)
    {
        major = d;
        advisor = adv;
    }
    void setMajor(Discipline d) { major = d; }
    Discipline getMajor() { return major; }
    void setAdvisor(Person *p) { advisor = p; }
    Person *getAdvisor() { return advisor; }
};

class Faculty:public Person
{
private:
    Discipline department;
public:
    Faculty(string fname, Discipline d) : Person(fname)
    {
        department = d;
    }
    void setDepartment(Discipline d) { department = d; }
    Discipline getDepartment( ) { return department; }
};

class TFaculty : public Faculty
{
private:
    string title;
public:
    TFaculty(string fname, Discipline d, string title)
    : Faculty(fname, d)
    {
        setTitle(title);
    }
    
    void setTitle(string title) { this->title = title; }
    
    // Virtual function
    virtual string getName( )
    {
        return title + " " + Person::getName();
    }
};

// HOMEWORK

//class RFaculty : public Faculty
//{
//private:
//    int day, month, year;
//public:
//    void retirementDate();
//    void setDate(int d, int m, int y);
//    
//};
//
//void RFaculty::retirementDate(){
//    cout << month << "/" << day << "/" << year;
//}
//
//void RFaculty::setDate(int d, int m, int y){
//    day = d; month = m; year = y; 
//}




int main()
{
    // Create an array of Person objects.
    const int NUM_PEOPLE = 5;
    
    Person *arr[NUM_PEOPLE] =
    {
        new TFaculty("Indiana Jones", ARCHEOLOGY, "Dr."),
        new Student("Thomas Cruise", COMPUTER_SCIENCE, NULL),
        new Faculty("James Stock", BIOLOGY),
        new TFaculty("Sharon Rock", BIOLOGY, "Professor"),
        new TFaculty("Nicole Eweman", ARCHEOLOGY, "Dr.")
    };
    
    // Print the names of the Person objects.
    for (int k = 0; k < NUM_PEOPLE; k++)
    {
        cout << arr[k]->getName() << endl;
    }  
    system ("pause");
    return 0;
}

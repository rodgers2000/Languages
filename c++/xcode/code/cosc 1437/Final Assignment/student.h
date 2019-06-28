//
//  student.h
//  ProgCode
//
//  Created by Michael Rodgers on 7/25/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#ifndef student_h
#define student_h

using namespace std; 

class Student: public Person {
private:
    string major_field_of_study;
    double gpa;
    
public:
    Student();
    Student(string, double, string, string, string, int, int, int);
    void change_data(string, double, string, string, string, int, int, int);
    void display_data();
};

Student::Student(): Person()
{
    major_field_of_study = "";
    gpa = 0.0;
}

Student::Student(string mfs, double g, string f, string l, string s, int a, int z, int p)
    : Person(f, l, s, a, z, p)
{
    major_field_of_study = mfs;
    gpa = g;
}

void Student::change_data(string mfs, double g, string f, string l, string s, int a, int z, int p)
{
    Person::change_data(f, l, s, a, z, p);
    major_field_of_study = mfs;
    gpa = g;
}

void Student::display_data()
{
    Person::display_data();
    cout << "Major field of study is " << major_field_of_study << endl;
    cout << "Grade point average is " << gpa << endl; 
}


#endif /* student_h */

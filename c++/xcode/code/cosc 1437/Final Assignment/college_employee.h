//
//  college_employee.h
//  ProgCode
//
//  Created by Michael Rodgers on 7/25/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#ifndef college_employee_h
#define college_employee_h

using namespace std;

class CollegeEmployee: public Person {
private:
    int social_security_number;
    int annual_salary;
    string department_name;
    
public:
    CollegeEmployee();
    CollegeEmployee(int, int, string, string, string, string, int, int, int);
    void change_data(int, int, string, string, string, string, int, int, int);
    void display_data();
};

CollegeEmployee::CollegeEmployee() : Person()
{
    social_security_number = 000000000;
    annual_salary          = 0;
    department_name        = "";
}

CollegeEmployee::CollegeEmployee(int sc, int as, string dn, string f, string l, string s, int a, int z, int p) : Person(f, l, s, a, z, p)
{
    social_security_number = sc;
    annual_salary          = as;
    department_name        = dn;
}

void CollegeEmployee::change_data(int sc, int as, string dn, string f, string l, string s, int a, int z, int p)
{
    Person::change_data(f, l, s, a, z, p);
    social_security_number = sc;
    annual_salary          = as;
    department_name        = dn; 
}

void CollegeEmployee::display_data()
{
    Person::display_data(); 
    cout << "Social security number is " << social_security_number << endl;
    cout << "Annual salary is " << annual_salary << endl;
    cout << "Department name is " << department_name << endl;
}


#endif /* college_employee_h */

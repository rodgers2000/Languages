#include <iostream>
#include <string> 
#include "person.h"
#include "college_employee.h"
#include "faculty.h"
#include "student.h"

using namespace std;

char prompt_user();
void enter_college_employee_data(CollegeEmployee [], int &);
void enter_faculty_data(Faculty [], int &);
void enter_student_data(Student [], int &);
void display_report(CollegeEmployee [], int &,
                    Faculty         [], int &,
                    Student         [], int &);

int main()
{
    CollegeEmployee college_employee_array [4];
    Faculty faculty_array [3];
    Student student_array [7];
    
    int college_employee_array_counter = 0;
    int faculty_array_counter = 0;
    int student_array_counter = 0;
    
    bool user_wants_to_continue = true;
    
    do {
        switch (prompt_user()) {
            case 'C':
                if (college_employee_array_counter < 4)
                    enter_college_employee_data(college_employee_array, college_employee_array_counter);
                else
                    cout << "ERROR" << endl;
                break;
            case 'F':
                if (faculty_array_counter < 3)
                    enter_faculty_data(faculty_array, faculty_array_counter);
                else
                    cout << "ERROR" << endl;
                break;
            case 'S':
                if (student_array_counter < 7)
                    enter_student_data(student_array, student_array_counter);
                else
                    cout << "ERROR" << endl;
                break;
            case 'Q':
                user_wants_to_continue = false;
                break;
            default:
                cout << "ERROR" << endl;
                break;
        }
    } while (user_wants_to_continue);
    
    
    display_report(college_employee_array, college_employee_array_counter,
                   faculty_array, faculty_array_counter,
                   student_array, student_array_counter);
    
    return 0; 
}

char prompt_user()
{
    char users_choice;
    cout << "***********************************" << endl;
    cout << "***************MENU****************" << endl;
    cout << "***********************************" << endl;
    cout << endl;
    cout << "1. Enter college employee data (C) " << endl;
    cout << "2. Enter faculty data (F)          " << endl;
    cout << "3. Enter student data (S)          " << endl;
    cout << "4. Quit program (Q)                " << endl;
    cout << endl << endl;
    cout << "Enter C, F, S, Q : " ;
    cin  >> users_choice;
    return users_choice;
}

void enter_college_employee_data(CollegeEmployee array[], int & counter)
{
    int sc; int as; string dn; string f; string l; string s; int a; int z; int p;
    
    cout << endl;
    cout << "College Employee Data: " << endl;
    cout << "Enter social security number: (int) " ;
    cin >> sc;
    cout << "Enter annual salary: (int) " ;
    cin >> as;
    cout << "Enter department name: (string) " ;
    cin >> dn;
    cout << "Enter first name: (string) " ;
    cin >> f;
    cout << "Enter last name: (string) " ;
    cin >> l;
    cout << "Enter street name: (string) " ;
    cin >> s;
    cout << "Enter address number: (int) " ;
    cin >> a;
    cout << "Enter zip code: (int) " ;
    cin >> z;
    cout << "Enter phone number: (int) " ;
    cin >> p;
    cout << endl;
    
    array[counter].change_data(sc, as, dn, f, l, s, a, z, p);
    
    counter++; 
}

void enter_faculty_data(Faculty array[], int & counter)
{
    bool t; int sc; int as; string dn; string f; string l; string s; int a; int z; int p;
    
    cout << endl;
    cout << "Faculty Data: " << endl;
    cout << "Enter tenure status: (bool) " ;
    cin >> t;
    cout << "Enter social security number: (int) " ;
    cin >> sc;
    cout << "Enter annual salary: (int) " ;
    cin >> as;
    cout << "Enter department name: (string) " ;
    cin >> dn;
    cout << "Enter first name: (string) " ;
    cin >> f;
    cout << "Enter last name: (string) " ;
    cin >> l;
    cout << "Enter street name: (string) " ;
    cin >> s;
    cout << "Enter address number: (int) " ;
    cin >> a;
    cout << "Enter zip code: (int) " ;
    cin >> z;
    cout << "Enter phone number: (int) " ;
    cin >> p;
    cout << endl;
    
    array[counter].change_data(t, sc, as, dn, f, l, s, as, z, p);
    
    counter++;
}

void enter_student_data(Student array[], int & counter)
{
    string mfs; double g; string f; string l; string s; int a; int z; int p;
    
    cout << endl;
    cout << "Student Data: " << endl;
    cout << "Enter major field of study: (string) " ;
    cin >> mfs;
    cout << "Enter grade point average: (int) " ;
    cin >> g;
    cout << "Enter first name: (string) " ;
    cin >> f;
    cout << "Enter last name: (string) " ;
    cin >> l;
    cout << "Enter street name: (string) " ;
    cin >> s;
    cout << "Enter address number: (int) " ;
    cin >> a;
    cout << "Enter zip code: (int) " ;
    cin >> z;
    cout << "Enter phone number: (int) " ;
    cin >> p;
    cout << endl;
    
    array[counter].change_data(mfs, g, f, l, s, a, z, p);
    
    counter++;
    
}

void display_report(CollegeEmployee ce_array[], int &ce_counter,
                    Faculty          f_array[], int &f_counter ,
                    Student          s_array[], int &s_counter )
{
    cout << endl;
    cout << "**********************************" << endl;
    cout << "**************REPORT**************" << endl;
    cout << "**********************************" << endl << endl;
    
    cout << "**********************************" << endl;
    cout << "******COLLEGE EMPLOYEE DATA*******" << endl;
    cout << "**********************************" << endl;
    cout << endl;
    
    if (ce_counter > 0) {
        for (int index = 0; index < ce_counter; index++)
        {
            cout << "College employee " << index + 1 << endl << endl;
            ce_array[index].display_data();
            cout << endl;
        }
        cout << "The college employee array has " << 4 - ce_counter << " empty components."
        << endl << endl;
    }
    else
        cout << "The college employee array has 4 empty components." << endl << endl;
    
    cout << "**********************************" << endl;
    cout << "**********FACULTY DATA************" << endl;
    cout << "**********************************" << endl;
    cout << endl;
    
    if (f_counter > 0) {
        for (int index = 0; index < f_counter; index++)
        {
            cout << "Faculty " << index + 1 << endl << endl;
            f_array[index].display_data();
            cout << endl;
        }
        cout << "The faculty array has " << 3 - f_counter << " empty components. "
            << endl << endl;
    }
    else
        cout << "The faculty array has 3 empty components. " << endl << endl;
    
    cout << "**********************************" << endl;
    cout << "**********STUDENT DATA************" << endl;
    cout << "**********************************" << endl;
    cout << endl;
    
    if (s_counter > 0) {
        for (int index = 0; index < s_counter; index++)
        {
            cout << "Student " << index + 1 << endl << endl;
            s_array[index].display_data();
            cout << endl;
        }
        cout << "The student array has " << 7 - s_counter << " empty components."
        << endl << endl;
    }
    else
        cout << "The student array has 7 empty components. " << endl << endl;
    
    cout << "**********************************" << endl;
    cout << "******THE REPORT HAS ENDED.*******" << endl;
    cout << "**********************************" << endl;
    cout << endl;
    
}









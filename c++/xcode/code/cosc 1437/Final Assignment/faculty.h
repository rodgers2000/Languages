//
//  faculty.h
//  ProgCode
//
//  Created by Michael Rodgers on 7/25/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#ifndef faculty_h
#define faculty_h

using namespace std;

class Faculty: public CollegeEmployee {
    bool has_tenure;
    
public:
    Faculty();
    Faculty(bool, int, int, string, string,
            string, string, int, int, int);
    void change_data(bool, int, int, string, string, string, string, int, int, int);
    void display_data(); 
};

Faculty::Faculty(): CollegeEmployee()
{
    has_tenure = false;
}

Faculty::Faculty(bool t, int sc, int as, string dn, string f,
                 string l, string s, int a, int z, int p)
        : CollegeEmployee(sc, as, dn, f, l, s, a, z, p)
{
    has_tenure = t; 
}

void Faculty::change_data(bool t, int sc, int as, string dn, string f, string l, string s, int a, int z, int p)
{
    CollegeEmployee::change_data(sc, as, dn, f, l, s, a, z, p);
    has_tenure = t;
}

void Faculty::display_data()
{
    CollegeEmployee::display_data();
    if (has_tenure)
        cout << "Professor has tenure " << endl;
    else
        cout << "Professor does not have tenure " << endl;
}





#endif /* faculty_h */

//
//  main.cpp
//  Manipulators: cout
//
//  Created by Michael Rodgers on 6/23/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream> // includes unparameterized manipulators
#include <iomanip> // includes parameterized manipulators
#include <string>
using namespace std;

int main(){
    
//    double x = 3.145600;
//    double y = 4.0;
    string mike = "Go LSU!";
    //FIXED
    
//    cout << "Default x: " << x << endl;
//    cout << "Fixed x (no set): " << fixed << x << endl;
//    cout << "Fixed x (set): " << setprecision(2) << x << endl;
    
// Comments:
    //      Showpoint is used for showing the decimal place when the decimal place has
    //      trailing zeros.
    //
    //      If you set the precision without fixed, then you are adjusting the total number
    //      of digits shown. With fixed, you are setting the decimal places shown.
    
    //SHOWPOINT
    
//    cout << "Default y: " << y << endl;
//    cout << "Showpoint y: " << showpoint << y << endl;
//    cout << "Showpoint x: " << x << endl;
    
    //SETW
    
    cout << "12345678901234567890" << endl;
    cout << setw(10) << mike << " Hi" << endl;
    cout << setw(10) << left << mike << endl;
    
    cout << "12345678901234567890" << endl;
    cout << right << setw(20) << setfill('$') << mike << endl;
    
    cout << "_*_*_*_*_*_*_*_*_*_*_*_*_*_*" << endl;
    cout << left << setw(20) << setfill('.') << "Team: " << " " << mike << endl;
    
    
    return 0;
}

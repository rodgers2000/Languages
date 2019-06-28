//
//  main.cpp
//  Operator Overloading
//
//  Created by Michael Rodgers on 7/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

//**********************************************************
// Author: D.S. Malik
//
// This program shows how to use the class clockType.
//**********************************************************

#include <iostream>
#include "newClock.h"
#include "newRectangle.h"

using namespace std;

int main()
{
    clockType myClock(5, 6, 23);                     //Line 1
    clockType yourClock;                             //Line 2
    
    cout << "Line 3: myClock = " << myClock
    << endl;                                    //Line 3
    cout << "Line 4: yourClock = " << yourClock
    << endl;                                    //Line 4
    
    cout << "Line 5: Enter the time in the form "
    << "hr:min:sec ";                           //Line 5
    cin >> myClock;                                  //Line 6
    cout << endl;                                    //Line 7
    
    cout << "Line 8: The new time of myClock = "
    << myClock << endl;                         //Line 8
    
    ++myClock;                                       //Line 9
    
    cout << "Line 10: After incrementing the time, "
    << "myClock = " << myClock << endl;         //Line 10
    
    yourClock.setTime(13, 35, 38);                   //Line 11
    cout << "Line 12: After setting the time, "
    << "yourClock = " << yourClock << endl;     //Line 12
    
    if (myClock == yourClock)                        //Line 13
        cout << "Line 14: The times of myClock and "
        << "yourClock are equal." << endl;      //Line 14
    else                                             //Line 15
        cout << "Line 16: The times of myClock and "
        << "yourClock are not equal." << endl;  //Line 16
    
    if (myClock <= yourClock)                        //Line 17
        cout << "Line 18: The time of myClock is "
        << "less than or equal to " << endl
        << "the time of yourClock." << endl;    //Line 18
    else                                             //Line 19
        cout << "Line 20: The time of myClock is "
        << "greater than the time of "
        << "yourClock." << endl;                //Line 20
    
    
// HOMEWORK
    
    //Rectangle box1(10, 20), box2(10, 20), box3(2, 2);
    //
    //if (box1 == box2)
    //    cout << "Box 1 equals Box 2" << endl; 
    //
    //cout << "box1(10, 20) + box3(2, 2) = box(width = 12, length = 22) " << endl;
    //
    //(box1 + box3).printMe();
    
    return 0;
}



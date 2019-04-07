//
//  main.cpp
//  Classes
//
//  Created by Michael Rodgers on 6/18/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;

class Date{
private:
    int m_year;
    int m_month;
    int m_day;
    static int count;
public:
//    Date();     // Default Constructor
    Date(int year=1995, int month=9, int day=6);     // Constructor with default parameters
    ~Date();    // Terminator
    void SetDate(int year, int month, int day);
    void getDate();
    void incrementCount();
    void print();
};

// FUNCTIONS

//Date::Date(){
//    m_year = 1969;
//    m_month = 9;
//    m_day = 6;
//}

int Date::count = 0; // STATIC VARIABLE

Date::Date(int year, int month, int day){
    SetDate(year, month, day);
}

Date::~Date(){
    cout << "The class object has gone out of scope. Deleting history!" << endl;
    
}

void Date::SetDate(int year, int month, int day){
    m_year = year;
    m_month = month;
    m_day = day;
}

void Date::getDate(){
    cout << m_month << "/" << m_day << "/" << m_year << endl;
    cout << "The cout is " << count << endl;
}

void Date::incrementCount(){
    count++;
}

int main(){
    
    Date usa(2017, 6, 18);
    usa.getDate();
    
    usa.incrementCount(); // Static variables updates for all objects!! pretty cool 
    
    Date mjr; // constructor is called automatically
    mjr.getDate();
    
    usa.getDate();

    
    
    return 0;
}


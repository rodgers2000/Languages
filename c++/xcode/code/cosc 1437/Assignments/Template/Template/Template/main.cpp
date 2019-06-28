//
//  main.cpp
//  Template
//
//  Created by Michael Rodgers on 7/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;


template <typename T>
T const& Max (T const& a, T const& b)
{
    return a < b ? b:a;
}
int main ()
{
    
    int i = 39;
    int j = 20;
    cout << "Max(i, j): " << Max(i, j) << endl;
    
    double f1 = 13.5;
    double f2 = 20.7;
    cout << "Max(f1, f2): " << Max(f1, f2) << endl;
    
	string s1 = "Hello";
    string s2 = "World";
    cout << "Max(s1, s2): " << Max(s1, s2) << endl;
    
    return 0;
}

//HOMEWORK

template <typename T>
void const Swap (T & a, T & b)
{
    cout << "a = " << a << endl
    << "b = " << b << endl;
    T temp;
    temp = a;
    a = b;
    b = temp;
    cout << "SWAP" << endl;
    cout << "a = " << a << endl
    << "b = " << b << endl;
}

int main () {
    
    cout << "INT" << endl;
    
    int i1 = 39;
    int i2 = 20;
    
    Swap(i1, i2);
    
    cout << "DOUBLE" << endl;

    double d1 = 13.5;
    double d2 = 20.7;
    
    Swap(d1, d2);

    cout << "FLOAT" << endl;

    float f1 = 12.12f;
    float f2 = 14.32f;
    
    Swap(f1, f2);
    
    return 0;
}


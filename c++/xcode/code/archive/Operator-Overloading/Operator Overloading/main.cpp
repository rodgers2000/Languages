//
//  main.cpp
//  Operator Overloading
//
//  Created by Michael Rodgers on 7/15/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

class myNumber {
    
private:
    int mjr;
    
public:
    myNumber(int);
//    myNumber operator+(myNumber &);
    friend myNumber operator+(myNumber &, myNumber &);
    void print();
};

// =========================================================

myNumber::myNumber(const int num)
{
    mjr = num;
}

//myNumber myNumber::operator+(myNumber &obj2)
//{
//    return myNumber(mjr + obj2.mjr);
//}

myNumber operator+(myNumber &obj1, myNumber &obj2)
{
    return myNumber(obj1.mjr + obj2.mjr);
}


void myNumber::print()
{
    cout << "Number = " << mjr << endl;
}

// ==========================================================

int main()
{
    myNumber one(1), two(2);
    
    myNumber three = two + one;
    
    three.print();
    
    return 0;
}

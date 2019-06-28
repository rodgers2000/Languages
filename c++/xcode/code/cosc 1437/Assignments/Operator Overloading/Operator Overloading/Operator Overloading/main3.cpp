//
//  main3.cpp
//  Operator Overloading
//
//  Created by Michael Rodgers on 7/19/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include "newClock.h"
#include "newRectangle.h"

using namespace std;

Rectangle Rectangle::operator+(Rectangle &obj1)
{
    return Rectangle(width + obj1.width, length + obj1.length);
}
bool Rectangle::operator==(Rectangle &obj1)
{
    return ((width == obj1.width) && (length == obj1.length)); 
}

void Rectangle::printMe()
{
    cout <<  "width = " << width << " " << "length = " << length << endl;
}



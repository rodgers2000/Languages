//
//  newRectangle.h
//  Operator Overloading
//
//  Created by Michael Rodgers on 7/19/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#ifndef newRectangle_h
#define newRectangle_h

#include <iostream> 

using namespace std;

class Rectangle {
private:
    int width, length;
    
public:
    Rectangle(int a, int b){width = a; length = b;};
    void printMe(); 
    Rectangle operator+(Rectangle &obj1);
    bool operator==(Rectangle &obj1);
};


#endif /* newRectangle_h */

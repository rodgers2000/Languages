//
//  function1.cpp
//  practice2000
//
//  Created by Michael Rodgers on 6/6/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream> 
#include "maxmin.hpp"

using namespace std;

int criticalPoints(int number1, int number2)
{
    
    int maximum = max(number1, number2);
    
    cout << "The max is " << maximum << endl;
    
    if (maximum == number1)
    cout << "The min is " << number2 << endl;
    else
    cout << "The min is " << number1 << endl;
    
    return 0; 
    
}

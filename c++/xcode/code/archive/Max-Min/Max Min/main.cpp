//
//  main.cpp
//  practice2000
//
//  Created by Michael Rodgers on 6/6/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include "maxmin.hpp"

using namespace std;

int number_1, number_2;

int main()
{
    cin >> number_1;
    cin >> number_2;
    
    criticalPoints(number_1, number_2);
    
    return 0; 
    
}

//
//  main.cpp
//  ifElseGoTo
//
//  Created by Michael Rodgers on 6/6/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include "loops.hpp"

using namespace std;

int main()
{
    int loopsize;
    cout << "Choose a loop: short (1), medium (2), long (3) or dual (any number)" << endl;
    
    cin >> loopsize;
    
    switch (loopsize) {
        case 1:
            Short();
            break;
        case 2:
            Medium();
            break;
        case 3:
            Long();
            break;
        default:
            Dual(); 
            break;
    }
    
    cout << endl; 
    return 0;
    
    
}

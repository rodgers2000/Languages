//
//  main.cpp
//  Pointers2
//
//  Created by Michael Rodgers on 7/9/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    
    int x = 25;
    int *p;
    p = &x;
    *p = 46;
    
    cout << x << endl;
    
    return 0;
}

//
//  main.cpp
//  Pointers
//
//  Created by Michael Rodgers on 6/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

int main(){
    
    int x=1, y=2;
    int * p1, * p2;
    
    p1 = &x; p2 = &y;
    *p1 = 10;
    *p2 = *p1;
    cout << x << " " << y << endl;
    p1 = p2;
    cout << x << " " << y << endl;
    *p1 = 20;
    cout << x << " " << y << endl;
    
    cout << *p2 << " " << *p1 << endl;
    cout << x << " " << y << endl;
}


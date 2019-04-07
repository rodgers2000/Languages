//
//  main.cpp
//  Pass by Reference
//
//  Created by Michael Rodgers on 6/11/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;


void modifyValue(int &x);

int main(){
    
    int y = 10;
    modifyValue(y); // adds ten to value 
    cout << y << endl;
    
    
}

void modifyValue(int &x){
    x = x + 10;
}

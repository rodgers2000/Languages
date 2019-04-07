//
//  main.cpp
//  For Loop
//
//  Created by Michael Rodgers on 6/11/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

int main(){
    
    double list[25];
    // standard for loop 
    for(int index = 0; index < 25; index++){
            list[index] = 1;
    }
    // range-based for loop
    for(double num : list){
        cout << num << endl;
    }

}

//
//  main.cpp
//  Static Variables
//
//  Created by Michael Rodgers on 6/18/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

void counter();

int main(){
    
//    static int count = 0;
    
    for (int i=0; i < 5; i++) {
        counter();
    }
    
    cout << endl;
    
    return 0;
}

void counter(){
    static int count = 0;
    cout << count++ << " ";
}

//void counter(){
//    int count = 0;
//    cout << count++ << " ";
//}

//void counter(){
//    cout << count++ << " ";
//}

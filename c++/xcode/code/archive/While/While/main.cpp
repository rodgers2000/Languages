//
//  main.cpp
//  While
//
//  Created by Michael Rodgers on 6/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

int main(){
    
    int x = 1;
    int y = 0;
    while (x) {
        cout << 1 << " ";
        y++;
        if (y == 10) {
            x = 0;
            cout << endl;
        }
    }
}

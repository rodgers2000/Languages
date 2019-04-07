//
//  main.cpp
//  Arithmetic
//
//  Created by Michael Rodgers on 6/10/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

void AddTen(int &);

int main(){
    
    int x=1, y=2;
    AddTen(x);
    y -= 2;
    cout << x << " " << y << endl;
    
    return 0;
}

void AddTen(int & num){
    num = num + 10;
}

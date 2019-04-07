//
//  main.cpp
//  Recursion
//
//  Created by Michael Rodgers on 6/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

int factorial(int num);

int factorial(int num){
    // This will lead to the factorial we want.
    if (num > 1) {
        return num * factorial(num - 1);
    } // We want the last number to be one.
    else
        return 1;
}

int main(){
    int number = 9;
    cout << number << "! = " << factorial(number) << "\n";
    return 1;
}

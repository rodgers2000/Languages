//
//  main.cpp
//  Namespaces
//
//  Created by Michael Rodgers on 6/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

namespace namespace1 {
    int x = 0;
    double y = 2.5;
}

namespace namespace2 {
    int z = 5;
}

using namespace namespace1;
using namespace std;

void changeNumber(int& num); // Initiate global scoping
void runLoop();

int main(){
    cout << x << " " << y << " " << namespace2::z << endl;
    int omg = namespace2::z;
    cout << "omg before: " << omg << endl;
    changeNumber(omg); // Nice for changing value of a var initiated outside of local scope.
    cout << "omg after: " << omg << endl;
    runLoop(); // Print each index in the loop 
    cout << endl;
    return 0;
}

void changeNumber(int& num){ // This overwrites local scoping.
    num = num + 1;
}

void runLoop(){
    for (int bookmark = 0; bookmark < 10; bookmark++) {
        cout << bookmark << " ";
    }
}

//
//  main.cpp
//  array
//
//  Created by Michael Rodgers on 4/4/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <array>

using namespace std;

int main(int argc, const char * argv[]) {
    
    array <int, 3> a1{ {1, 3, 2} };
    
    for (int i = 0; i < a1.size(); i++) {
        a1[i] = 0;
    }
    for (int i = 0; i < a1.size(); i++) {
        cout << a1[i] << endl;
    }
    
    return 0;
}

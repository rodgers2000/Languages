//
//  main.cpp
//  test
//
//  Created by Michael Rodgers on 4/4/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
// the cpp file calls the header file, which declares the functions or objects
#include "/Users/mrodgers/Documents/other/languages/c++/xcode/code/templates/organize-folders/organize-folders/objects/Mike.cpp"
#include "/Users/mrodgers/Documents/other/languages/c++/xcode/code/templates/organize-folders/organize-folders/functions/arithmetic.cpp"

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    Mike mjr;
    cout << mjr.y << endl;
    cout << mjr.add(10, 1) << endl;
    cout << mjr.add2() << endl;
    cout << add(2, 2) << endl;
    cout << Mike::add(10, 1) << endl; 
    return 0;
}

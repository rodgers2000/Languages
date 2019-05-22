//
//  main.cpp
//  Iterate Map
//
//  Created by Michael Rodgers on 5/11/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(int argc, const char * argv[]) {
    // create object
    map<string, int> mjr;
    // insert values
    mjr.insert(pair<string, int>("first", 1));
    mjr.insert(pair<string, int>("second", 2));
    mjr.insert(pair<string, int>("third", 3));
    // iterate through them
    for (pair<string, int> element : mjr) {
        if (element.second == 2) {
            cout << element.first << "::" << element.second << endl;
        }
    }
    return 0;
}

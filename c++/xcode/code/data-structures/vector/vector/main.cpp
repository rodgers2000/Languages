//
//  main.cpp
//  vector
//
//  Created by Michael Rodgers on 4/4/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

void print(vector<int> v) {
    for (int i : v) {
        cout << i << endl;
    }
}

void insert(vector<int> &v, int index, int value){
    if (index >= v.size() || index < 0) {
        cout << "error" << endl;
    }
    else {
        v[index] = value;
    }
}



int main(int argc, const char * argv[]) {
    
//    vector <int> v = {7, 5, 16, 8};
//    insert(v, 3, 69);
//    print(v);
    
//    vector<int> v;
//    v.push_back(10);

    vector<int> v(3, 10);
    print(v);
    
    
    return 0;
}

//
//  main.cpp
//  output to file
//
//  Created by Michael Rodgers on 4/5/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    int A[3] = {1, 2, 3};
    
    ofstream myfile;
    myfile.open("/Users/mrodgers/Documents/other/languages/c++/xcode/code/algorithms/output to file/output to file/example.csv");
    int a = 0;
    for (int i : A) {
        if (a != 2) {
            myfile << i << ",";
        } else {
            myfile << i;
        }
        a++;
    }
    myfile << endl;
    myfile.close();
    
    return 0;
}

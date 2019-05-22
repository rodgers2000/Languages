//
//  main.cpp
//  Output CSV
//
//  Created by Michael Rodgers on 5/10/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    // file object
    fstream fout;
    fout.open("/Users/mrodgers/Documents/other/languages/c++/xcode/code/algorithms/Output CSV/Output CSV/mjr.csv", ios::out);

    int a=1, b=2, c=3, d=4;
    fout << "col1" << "," << "col2" << "," << "col3" << "," << "col4"   << "\n";
    for (int i = 1; i < 5; i++) {
        fout << a << ","
        << b << ","
        << c << ","
        << d << "\n";
    }
    fout.close();
    return 0;
}


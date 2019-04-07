//
//  main.cpp
//  Read CSV
//
//  Created by Michael Rodgers on 4/6/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {

    ifstream myfile;
    myfile.open("/Users/mrodgers/Documents/other/languages/c++/xcode/code/algorithms/Read CSV/Read CSV/data.csv");
    
    string line;
    string temp = "";

    while (getline(myfile, line)) { //while there is a line
            // column index
        for (int i = 0; i < line.size(); i++) { // for each character in rowstring
            if (!isblank(line[i]) and line[i] != ',') { // if it is not blank, do this
                string d(1, line[i]); // convert character to string
                temp.append(d); // append the two strings
            } else {
                cout << temp << endl;
                temp = ""; // reset the capture
                
            }
            if (i == line.size() - 1) {
                cout << temp << endl;
            }
        }
    
    }
return 0;
}

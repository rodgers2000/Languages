//
//  main.cpp
//  data entry
//
//  Created by Michael Rodgers on 3/15/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

class DataEntry
{
public:
    int X[2][5];
    
    void printData(){
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 5; j++) {
                cout << X[i][j] << endl;
                //            cout << i << j << endl;
            }
        }
    }
    
    void getData(){
        ifstream myfile;
        myfile.open("/Users/mrodgers/Documents/other/languages/c++/xcode/code/algorithms/data entry/data entry/data.txt");
        
        string line;
        string temp = "";
        int a = 0;
        
        while (getline(myfile, line)) {
            int b = 0;
            for (int i = 0; i < line.size(); i++) {
                if (!isblank(line[i])) {
                    string d(1, line[i]); // convert character to string
                    temp.append(d); // append the two strings
                } else {
                    //                cout << stod(temp);
                    X[a][b] = stod(temp);  // convert string to double
                    temp = ""; // reset the capture
                    b++; // increment b cause we have a new number
                }
            }
            //        cout << stod(temp);
            X[a][b] = stod(temp);
            temp = "";
            a++;
        }
    }
};

int main() {
    
    DataEntry mjr;
    
    mjr.getData();
    mjr.printData();
    
    //    cout << "enter n: ";
    //    cin >> n;
    //    cout << "enter p: ";
    //    cin >> p;
    
    //    if (myfile.fail()) {
    //        cout << "FAIL" << endl;
    //    }

    
//    int n = 2, p = 5;
//
//    int X[n][p];
//
//    ifstream myfile;
//    myfile.open("/Users/mrodgers/Documents/other/languages/c++/xcode/code/algorithms/data entry/data entry/data.txt");
//
//    string line;
//    string temp = "";
//    int a = 0;
//
//    while (getline(myfile, line)) {
//        int b = 0;
//        for (int i = 0; i < line.size(); i++) {
//            if (!isblank(line[i])) {
//                string d(1, line[i]); // convert character to string
//                temp.append(d); // append the two strings
//            } else {
////                cout << stod(temp);
//                X[a][b] = stod(temp);  // convert string to double
//                temp = ""; // reset the capture
//                b++; // increment b cause we have a new number
//            }
//        }
////        cout << stod(temp);
//        X[a][b] = stod(temp);
//        temp = "";
//        a++;
//        }
    
//    int content;
//    int a = 0;
//    int b = 0;
//
//    while(myfile >> content) {
////        cout << content << endl;
////        cout << a << b << endl;
//        X[a][b] = content;
////        cout << X[a][b] << endl;
//        if (b == p-1) {
//            b = -1; // start at 0
//            a++; // start on 2nd row
//        }
//        b++;
//    }
//
//    for (int i = 0; i < n; i++) {
//        for (int j = 0; j < p; j++) {
//            cout << X[i][j] << endl;
////            cout << i << j << endl;
//        }
//    }
//
    return 0;
}

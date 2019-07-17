//
//  main.cpp
//  Read CSV 2
//
//  Created by Michael Rodgers on 7/9/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ifstream ip;
    ip.open("data.csv");
    
    int COLS = 4, ROWS = 3;
    int mjr[COLS][ROWS];
    
    if (ip.is_open()) {
        cout << "good" << "\n";
    }
    
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            string temp;
            if (j < COLS - 1) {
                getline(ip, temp, ',');
            } else {
                getline(ip, temp, '\n');
            }
//            cout << temp << "\n";
            mjr[i][j] = stoi(temp);
            cout << mjr[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}

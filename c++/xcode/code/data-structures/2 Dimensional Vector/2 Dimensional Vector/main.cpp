//
//  main.cpp
//  2 Dimensional Vector
//
//  Created by Michael Rodgers on 5/11/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    
    vector<vector<int>> mjr;
    mjr.push_back(vector<int>());
    mjr[0].push_back(5);
    cout << mjr[0][0] << endl; 
    
    return 0;
}

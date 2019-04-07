//
//  main.cpp
//  matrix
//
//  Created by Michael Rodgers on 4/5/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

void print(int a[][3], int x, int y){
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++) {
            cout << a[i][j] << endl;
        }
    }
}

int main(int argc, const char * argv[]) {
    
    int A[3][3] = {{1, 2, 3}, {4, 5, 6}, {7 ,8, 9}};
    
    print(A, 3, 3);
    
    
    return 0;
}

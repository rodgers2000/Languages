//
//  main.cpp
//  C-string arrays
//
//  Created by Michael Rodgers on 7/24/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

int main()
{
    int a = 5, b = 10; 
    
    char list[10][20];
    
    for (int index = 0; index < 10; index++)
        cin >> list[index];
    
    for (int index = 0; index < 10; index++) {
        cout << strlen(list[index]);
    }
    
    cout << endl;
    
    return 0;
}

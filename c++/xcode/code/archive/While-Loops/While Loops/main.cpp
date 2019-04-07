//
//  main.cpp
//  While Loops
//
//  Created by Michael Rodgers on 6/7/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

int main()
{
    int outer = 5;
    int inner = 0;

    while(outer > 0)
    {
        cout << outer << " ";
        outer--;
    }
        
    do
    {
        cout << inner << "\n";
        inner++;
    } while (inner <= 5);
    
    int middle = 3;
    
    while (middle > 0) {
        cout << middle << " ";
        //Let's create a new line
        if (middle == 1)
        {
            cout << endl;
        }
        //Decrement the value
        middle--;
    }
    //While and for loops are equivalent
    for (int omg = 0; omg < 3; omg++) {
        cout << omg ;
        //if condition
        if (omg == 2) {
            cout << " The omg loop!!!" << endl;
        }
        else cout << " ";
    }
    
        
    return 0;
}



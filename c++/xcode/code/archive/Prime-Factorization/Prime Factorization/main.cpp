//
//  main.cpp
//  Prime Factorization
//
//  Created by Michael Rodgers on 7/2/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <math.h>

using namespace std;

void primeFactorization(int number) {
    
    cout << number << ": ";

    // WHILE number is even
    while (number % 2 == 0) {
       // SET number = number / 2
        number = number / 2;
       // PRINT number
        cout << 2 << " " ;
        // END WHILE
    }
    //  GO TO DESTINATON
    reloop:
    // FOR factor in 3 to the sqrt(number), by 2
    for (int factor = 3; factor <= sqrt(number); factor = factor + 2) {
        // IF number modular factor equals 0 THEN
        if (number % factor == 0) {
        // PRINT factor
            cout << factor << " " ;
        // SET number = number / factor
            number = number / factor;
        // GO TO
            goto reloop;
        // END IF
        }
        //  END FOR
    }
    //IF number > 2 THEN
    if (number > 2) {
        //PRINT number
        cout << number;
        //END IF
    }
    cout << endl;
}

int main() {
    int usersNumber;
    bool userWants2Play = true;
    
    while (userWants2Play) {
        
    cout << "Please enter a number to be factored: " ;
    cin >> usersNumber;
    
    primeFactorization(usersNumber);
     
        cout << "Do you want to play again? 1 or 0: " ;
        cin >> userWants2Play;
    }
    
    
    return 0;
    
}

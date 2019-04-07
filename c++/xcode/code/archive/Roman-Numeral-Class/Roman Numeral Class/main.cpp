//
//  main.cpp
//  Roman Numeral Class
//
//  Created by Michael Rodgers on 7/1/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

class romanType {
    
private:
    int number;
    string romanNumeral;
    
public:
    void convertRoman();
    void printDigit();
    void setRomanNumeral(string unit);
};

void romanType::setRomanNumeral(string unit){
    romanNumeral = unit;
}

void romanType::convertRoman(){
    
    int sum = 0;
    
    for (int index = 0; index < romanNumeral.length(); index++) {
    
    switch (romanNumeral[index]) {
        case 'M':
            sum += 1000;
            break;
        case 'D':
            sum += 500;
            break;
        case 'C':
            sum += 100;
            break;
        case 'L':
            sum += 50;
            break;
        case 'X':
            sum += 10;
            break;
        case 'V':
            sum += 5;
            break;
        case 'I':
            sum += 1;
            break;
            
        default:
            cout << "Invalid numeral \n";
            break;
    }
    }
    // Once the loop has run, set sum to converted number
    
    number = sum;
}


void romanType::printDigit(){
    cout << "Roman numeral: " << romanNumeral << " equals number: " << number << endl;
}

int main(){
    
    bool theyWant2Play = true;
    string usersRomanNum;
    romanType MYROME;
    
    while (theyWant2Play) {
        
        cout << "Enter a Roman Numeral. "
             << "Your options are: M, D, C, L, X, V, I"
        << endl;
        cin >> usersRomanNum;
        
        MYROME.setRomanNumeral(usersRomanNum);
        MYROME.convertRoman();
        MYROME.printDigit();
        
        cout << "Do you want to play again? 1 or 0" << endl;
        cin >> theyWant2Play;
        
    }
    
    return 0;
}
















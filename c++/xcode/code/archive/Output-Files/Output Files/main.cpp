//
//  main.cpp
//  output files
//
//  Created by Michael Rodgers on 6/7/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int sum = 0;
    int val = 0;
    int count = 0;
    int average;
    
    ifstream inData;
    ofstream outData;
    
    inData.open("infile.txt");
    
    if (!inData) {
        cout << "Can't open in file. ";
        return 1;
    }
    
    outData.open("theOutputFile.txt");
    
    if (!outData) {
        cout << "Can't open out file. ";
        return 2;
    }
    
    //Read value from the input file
    //Loop terminates when EOF is encountered
    
    inData >> val; //read value in
    
    while (inData) { //while previous input succeeded
        sum = sum + val;
        count++;
        
        inData >> val; //read in the next value
    }
    
    if (count != 0) {
        average = sum / count;
    }
    else
        average = 0;
    
    outData << "Data items: " << count << endl << "Sum: " << sum << endl<<
                                    "Average: " << average <<endl;
    
    return 0;
}

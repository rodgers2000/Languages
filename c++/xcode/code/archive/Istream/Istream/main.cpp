//
//  main.cpp
//  Istream
//
//  Created by Michael Rodgers on 7/6/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

ostream& output(string myString, ostream& outPut) {
    
    outPut << myString << endl;
    
    return outPut;
    
}

istream& input(string& myString, istream& inPut) {
    
    inPut >> myString;
    
    return inPut;
}


int main() {
    
    output("Hello Michael", cout);
    
    string helloString;
    
    input(helloString, cin);
    
    cout << helloString << endl;
    
    return 0;
}

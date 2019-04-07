//
//  main.cpp
//  Arrays Initialization
//
//  Created by Michael Rodgers on 6/15/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
using namespace std;

void initialization(int array[], int array_size); // declare functions
void printArray(int array[], int array_size);     // declare functions

int main(){
    
    int my_array[10];
    int my_array_size = 10;
    
    // This is proof that arrays are passed by reference and changes to their
    // values are kept, even within different scopes.
    
    initialization(my_array, my_array_size);
    
    printArray(my_array, my_array_size);
    
    cout << endl;
    
}

void initialization(int array[], int array_size){
    
    for (int index=0; index < array_size; index++) {
        array[index] = 0;
    }
    
}

void printArray(int array[], int array_size){
    
    for (int index=0; index < array_size; index++) {
        cout << array[index] << ", ";
    }
    
}

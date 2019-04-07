//
//  main.cpp
//  Arrays
//
//  Created by Michael Rodgers on 6/7/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

int main(){
    int array [5] = {1, 5, 10, 15, 20};
    //Let's loop through the array
    for (int index = 0; index < 5; index++) {
        std::cout << array[index] << std::endl;
    }
    //initialize
    int index = 0;
    do {
        std::cout << array[index] << " ";
        if (index == 4) {
            std::cout << std::endl;
        }
        index++;
    } while (index < 5);
    //One more time!!
    std::cout << "One more time!!!\n";
    index = 0;
    while (index < 5) {
        std::cout << array[index] << " ";
        if (index == 4) {
            std::cout << std::endl;
        }
        index++;
    }
    
    //Bidimensional Arrays
    
    int mjr [10][10];
    for (int row = 0; row < 10; row++) {
        for (int col = 0; col < 10; col++) {
             mjr[row][col] = row * col;
            std::cout << mjr[row][col] << " ";
        }
        std::cout << std::endl;
    }
    
    
    
}

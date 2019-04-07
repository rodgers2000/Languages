//
//  main.cpp
//  Dynamic Memory
//
//  Created by Michael Rodgers on 7/4/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    
//    int *ptr1 = new int;
//    
//    int *ptr2 = new int;
//    
//    *ptr1 = 15;
//    *ptr2 = 10;
//    
//    cout << "ptr1 = " << *ptr1 << endl;
//    cout << "ptr2 = " << *ptr2 << endl;
//    
//    ptr1 = ptr2;
//    
//    
//    cout << "ptr1 = ptr2 " << ptr1 << " " << *(&ptr1) << endl;
    
    int *list = new int[10];
    
    
    for (int index = 0; index < 10; index++) {
        list[index] = index;
    }
    
    for (int index = 0; index < 10; index++) {
        cout << *(&list[0] + index) << " " ;
        cout << *(list + index) << " " ;
    }
    
    cout << endl;
    
    for (int index = 0; index < 10; index++) {
        cout << list[index] << " " ;
    }
    
    cout << endl;
    cout << list << " ";
    cout << &list[1] << " ";
    
    delete [] list;
    
    cout << endl;
    
    
    
    
    return 0;
}

//
//  main.cpp
//  Pointers Lab
//
//  Created by Michael Rodgers on 7/8/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    
 // THIS IS BE SUBMITTED
    
    int a=12,b=20,c=30;
    int sum;
    int *ptrA = &a, *ptrB = &b, *ptrC = &c;
    sum = a + b + c;
    cout << "Sum of a,b,c is " << sum<< endl;
    sum = *ptrA + *ptrB + *ptrC;
    cout << "Using pointers Sum of a,b,c is " << sum<< endl; *ptrA = 1;
    sum = a + b + c;
    cout << "Sum of a,b,c is " << sum<< endl;
    *ptrB = 11;
    sum = *ptrA + *ptrB + *ptrC;
    cout << "Using pointers Sum of a,b,c is " << sum<< endl;
    system ("pause");
    
// THIS IS FOR HOMEWORK
    
//    string name;
//    
//    string address;
//    
//    int item = 100;
//    
//    int quantity = 10;
//    
//    int price = 50;
//    
//    int SIZE = 6;
//    
//    int VALID_ITEM [6] = {106, 108, 307, 405, 457, 688};
//    
//    double VALID_ITEM_PRICE [6] = {0.59, 0.99, 4.50, 15.99, 17.50, 39.00};
//    
//    int sub;
//    
//    string foundIt = "N";
//    
//    string MSG_YES = "Item available";
//    
//    string MSG_NO = "Item not found";
//    
//    cout << "Enter name, address, item, quantity. ";
//    
//    cin >> name, address, item, quantity;
//    
//    sub = 1;
//    
//    while (sub <= SIZE)
//    {
//        if (item == VALID_ITEM [sub])
//        {
//            
//            foundIt = "Y";
//            
//            price = VALID_ITEM_PRICE [sub];
//            
//        }
//            
//        sub = sub + 1;
//    }
//            
//            if (foundIt == "Y")
//            {
//                cout << "MSG_YES";
//                
//                cout << quantity << " at " << price << " each ";
//                
//                cout << "Total " << quantity * price;
//                
//            } else
//            {
//                    cout << "MSG_NO";
//            }
    
    return 0;
}

//    Output Sample:
//    Sum of a,b,c is 62
//    Using pointers Sum of a,b,c is 62
//    Sum of a,b,c is 51
//    Using pointers Sum of a,b,c is 42

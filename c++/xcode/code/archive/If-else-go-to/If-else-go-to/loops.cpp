//
//  loops.cpp
//  ifElseGoTo
//
//  Created by Michael Rodgers on 6/6/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

void Short()
{
    for (int i=0; i < 10; i++)
        {
            std::cout << i;
        }
   
}

void Medium()
{
    for (int j=0; j < 20; j++)
    {
        std::cout << j << std::endl;
    }
    

}

void Long()
{
    for (int j=0; j < 50; j++)
    {
        std::cout << j << std::endl;
    }
    
    
}

void Dual()
{
    for (int i=0, j=10; i < 10; i++, j--)
    {
        std::cout << i << " " << j << std::endl;
    }
}

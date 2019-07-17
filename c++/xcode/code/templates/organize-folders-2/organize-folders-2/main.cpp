//
//  main.cpp
//  organize-folders-2
//
//  Created by Michael Rodgers on 7/16/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>

#include "functions/arithmetic.cpp"

int main(int argc, const char * argv[]) {
    arithmetic mjr;
    std::cout << mjr.add(5, 5) << std::endl;
    return 0;
}

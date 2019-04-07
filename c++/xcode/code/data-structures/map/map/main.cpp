//
//  main.cpp
//  map
//
//  Created by Michael Rodgers on 4/4/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    
    map <string, int> m;
    m.insert(make_pair("hello",9));
    m.insert(make_pair("hi",11));
    
    map<string,int>::iterator itr = m.find("hi");
    
    cout << itr->second << endl; 
    
    
    return 0;
}

//
//  main.cpp
//  Vector Class
//
//  Created by Michael Rodgers on 5/11/19.
//  Copyright © 2019 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

class Node {
public:
    int a = 1;
    int b = 2;
    int c = 3;
};

int main(int argc, const char * argv[]) {
    Node abc;
    abc.a = 69;
    vector<Node> graph;
    graph.push_back(abc);
    cout << graph[0].a << endl;
    
    return 0;
}

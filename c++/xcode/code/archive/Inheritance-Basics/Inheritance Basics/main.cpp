//
//  main.cpp
//  Inheritance Basics
//
//  Created by Michael Rodgers on 6/25/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

class Base
{
private:
    int m_id;
public:
    Base(int id=0)
    : m_id(id)
    {
    }
public:
    int getId() const { return m_id; }
};

class Derived: public Base
{
public:
    double m_cost;
    
    Derived(double cost=0.0, int id=0)
    : m_cost(cost), Base(id)
    {
    }
    
    double getCost() const;
    
    string getId() { return "ERROR"; }
    
};

double Derived::getCost() const{
    return m_cost;
}

int main(){
    
    Derived mjr;
    
    cout << mjr.Base::getId() << endl;
    
    
}

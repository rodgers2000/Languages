//
//  main.cpp
//  Final Code
//
//  Created by Michael Rodgers on 7/22/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>
#include <string>

using namespace std;

/////////////////////////////////////////////////////////////
////////////////// DOG AND COLLIE CLASS /////////////////////
/////////////////////////////////////////////////////////////

class Dog {
private:
    char gender;
    int age;
    string name;
    
public:
    Dog();
    Dog(string n, int a, char g);
    void dispDog();
};

class Collie: public Dog {
private:
    string look;
    int size;
    int LifeSpan;
    
public:
    Collie();
    Collie(string n, int a, char g, string l, int s, int ls);
    void disp();
};

/////////////////////////////////////////////////////////////
////////////////// DOG FUNCTIONS ////////////////////////////
/////////////////////////////////////////////////////////////

Dog::Dog(){
    gender = ' ';
    age = 0;
    name = "";
}

Dog::Dog(string n, int a, char g){
    name = n;
    age = a;
    gender = g;
}

void Dog::dispDog(){
    cout << "Dog's gender: " << gender << endl;
    cout << "Dog's age: " << age << endl;
    cout << "Dog's name: " << name << endl;
}

/////////////////////////////////////////////////////////////
////////////////// COLLIE FUNCTIONS /////////////////////////
/////////////////////////////////////////////////////////////

Collie::Collie(){
    look = "";
    size = 0;
    LifeSpan = 0;
}

Collie::Collie(string n, int a, char g, string l, int s, int ls)
    : Dog(n, a, g)
{
    look = l;
    size = s;
    LifeSpan = ls;
}

void Collie::disp(){
    dispDog();
    cout << "Collie's look: " << look << endl;
    cout << "Collie's size: " << size << endl;
    cout << "Collie's LifeSpan: " << LifeSpan << endl;
}

/////////////////////////////////////////////////////////////
////////////////// MAIN FUNCTION ////////////////////////////
/////////////////////////////////////////////////////////////

int main(){
    
    Collie myCollie = Collie("Max", 3, 'M', "Short Coat", 55, 12);
    
    myCollie.disp();
    
    return 0;
}












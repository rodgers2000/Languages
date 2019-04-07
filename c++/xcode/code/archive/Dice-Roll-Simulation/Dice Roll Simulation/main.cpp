//
//  main.cpp
//  Dice Roll Simulation
//
//  Created by Michael Rodgers on 7/1/17.
//  Copyright © 2017 Michael Rodgers. All rights reserved.
//

#include <iostream>

using namespace std;

class die{
    
private:
    int roll[10];
    int chosenSum;
    int numberOfSims;
    int hitsOfChosenSum = 0;
public:
    void setChosenSum(int expectation = 3.5 * 10){chosenSum = expectation; }
    void setNumberOfSims(int trials = 10000){ numberOfSims = trials; }
    void diceRollSimulation();

};

void die::diceRollSimulation(){
    
    int trial = 0;
    hitsOfChosenSum = 0;
    
    do {
        int youRolled;
        
        for (int dice = 0; dice < 10; dice++) {
            
            youRolled = rand() % 6 + 1;
            
            roll[dice] = youRolled;
    
        }
        
         int runningSum = 0;
        
        for (int dice = 0; dice < 10; dice++) {
            runningSum += roll[dice];
        }
        
        if (runningSum == chosenSum) {
            hitsOfChosenSum += 1;
        }
        
        trial += 1;
        
    } while (trial < numberOfSims);
    
    double probability;
    probability = static_cast<double>(hitsOfChosenSum) / trial;
    
    
    cout << "Your chosen sum is " << chosenSum << endl
    << "You had " << hitsOfChosenSum << " hits" << endl
    << "The probability of a hit is " << probability << endl
    << "You had " << numberOfSims << " simulations" << endl;
    
}


int main(){
    
    die myCraps;
    int simulations;
    int usersSum;
    bool playAgain = true;
    
    cout << "Enter simulations: " ;
    cin >> simulations;
    
    cout << "Enter desired sum for 10 roles: " ;
    cin >> usersSum;
    
    while (playAgain == true) {
    
    myCraps.setChosenSum(usersSum);
    myCraps.setNumberOfSims(simulations);
    myCraps.diceRollSimulation();
        
        cout << "Do you want to simulation again? 1 or 0: " ;
        cin >> playAgain;
    
        
    }
    
    return 0;
    
}














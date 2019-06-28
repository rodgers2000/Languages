//**************************************************
//           ProgLabStructs Assignment
//    COSC 1437 - Instructor Derakhshandeh
//              Michael Rodgers
//             Due Date: 6/19/17
//**************************************************

#include <iostream>
#include <string>
using namespace std;

class Patient  //ADT
{
private:
    string name;
    int age;
    int smoker, HBP, HFD;
    int points;
public:
    Patient();
    Patient(string, int, int, int, int);
    void calPoints();
    void setPatient(string, int, int, int, int);
    void dispPatient();
};
Patient::Patient(string n, int a, int s, int hbp, int hfd)
{
    name = n;
    age = a;
    smoker = s;
    HBP = hbp;
    HFD = hfd;
}
Patient::Patient()
{
    name = "";
    age = smoker = HBP = HFD = 0;
    
}

void Patient::setPatient(string n, int a, int s, int hbp, int hfd)
{
    name = n;
    age = a;
    smoker = s;
    HBP = hbp;
    HFD = hfd;
}
void Patient::calPoints()
{
    if (age < 20)
        points = 1;
    else if (age < 30)
        points = 2;
    else
        points = 3;
    
    if (smoker == 1) points += 4;
    if (HBP == 1)    points += 2;
    if (HFD == 1)    points += 1;
}

void Patient::dispPatient()
{
    cout << "Name: " << name << endl;
    cout << "Points: " << points << endl;
}
int main()
{
    //Add your c++ code
    Patient woman1("Woman1", 33, 0, 0, 1);
    woman1.calPoints();
    woman1.dispPatient();
    
    Patient man1("Man1", 19, 0, 1, 1);
    man1.calPoints();
    man1.dispPatient();
    
    Patient woman2("Woman2", 50, 0, 1, 1);
    woman2.calPoints();
    woman2.dispPatient();
    
    Patient man2("Man2", 27, 1, 1, 0);
    man2.calPoints();
    man2.dispPatient();
    
    Patient woman3("Woman3", 43, 1, 1, 1);
    woman3.calPoints();
    woman3.dispPatient();
    
    Patient woman4("Woman4", 17, 0, 0, 1);
    woman4.calPoints();
    woman4.dispPatient();
    
    
//     system("pause");
    return 0;
}







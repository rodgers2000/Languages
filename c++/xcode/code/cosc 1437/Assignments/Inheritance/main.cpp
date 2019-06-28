// This demonstrates the polymorphic behavior
// of classes with virtual functions.

#include <iostream>
#include <string>
using namespace std;

enum Discipline { ARCHEOLOGY, BIOLOGY, COMPUTER_SCIENCE };
enum Classification { FRESHMAN, SOPHOMORE, JUNIOR, SENIOR };

// PERSON CLASS

class Person
{
protected:
    string name;
    
public:
    Person() { setName(""); }
    
    Person(string pName) { setName(pName); }
    
    void setName(string pName) { name = pName; }
    
    string getName() { return name; }
};

// STUDENT CLASS

class Student: public Person
{
protected:
    Discipline major;
    Person *advisor;
    
public:
    Student(string sname, Discipline d, Person *adv)
    : Person(sname)
    {
        major = d;
        advisor = adv;
    }
    void setMajor(Discipline d) { major = d; }
    Discipline getMajor() { return major; }
    void setAdvisor(Person *p) { advisor = p; }
    Person *getAdvisor() { return advisor; }
    
    bool isStudent(){return true; }
};

// FACULTY CLASS

class Faculty: public Person
{
private:
    Discipline department;
    
public:
    Faculty(string fname, Discipline d) : Person(fname)
    {
        department = d;
    }
    void setDepartment(Discipline d) { department = d; }
    Discipline getDepartment( ) { return department; }
};

// TEACHING FACULTY CLASS

class TFaculty: public Faculty
{
private:
    string title;
    
public:
    TFaculty(string fname, Discipline d, string title)
    : Faculty(fname, d)
    {
        setTitle(title);
    }
    
    void setTitle(string title) { this->title = title; }
    
    // Virtual function
    string getName( )
    {
        return title + " " + Person::getName();
    }
};

// GRADUATE STUDENT CLASS

class GradStudent: public Student
{
private:
    string bsDegreeName; // degree name
    float bsGPA;  // gpa
    string ProgName;  // master's program name
    
public:
    
    // default constructor
    GradStudent(Person advisor = Person()):
    Student("", ARCHEOLOGY, &advisor)
    {
        bsDegreeName = "";
        bsGPA = 0;
        ProgName = "";
    }
    
    // parameterized constructor with default values
    GradStudent(string bsdn = "", float gpa = 0, string inst = "", string pname = "", Discipline d = ARCHEOLOGY, Person advisor = Person()):
    Student(pname, d, &advisor)
    {
        bsDegreeName = bsdn;
        bsGPA = gpa;
        ProgName = inst;
    }
    
    string getDegree() {return bsDegreeName; }
    
};





int main()
{
    // Create objects.
    
    
    TFaculty Tf1("Indiana Jones", ARCHEOLOGY, "Dr.");
    Student  Stud("Thomas Cruise", COMPUTER_SCIENCE, NULL);
    Faculty  Fac("James Stock", BIOLOGY);
    TFaculty Tf2("Sharon Rock", BIOLOGY, "Professor");
    TFaculty Tf3("Nicole Eweman", ARCHEOLOGY, "Dr.");
    
    
    // Print the names of the Person objects.
//    
//    cout << Tf1.getName() << endl;
//    cout << Stud.getName() << endl;
//    cout << Fac.getName() << endl;
//    cout << Tf2.getName() << endl;
//    cout << Tf3.getName() << endl;
    
    // HOMEWORK SECTION
    
    GradStudent mjr("Stats", 4.33, "Rice", "Michael Rodgers", COMPUTER_SCIENCE, Person("Michael's Advisor"));
    
    mjr.setMajor(COMPUTER_SCIENCE);
    
    cout << "Student's getMajor() function: " << mjr.isStudent() << endl;

    
//    system ("pause");
    return 0;
}

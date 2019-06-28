#ifndef person_h
#define person_h

using namespace std;

class Person {
private:
    string first_name;
    string last_name;
    string street_name;
    int address;
    int zip_code;
    int phone_number;
public:
    Person();
    Person(string, string, string, int, int, int);
    void change_data(string, string, string, int, int, int);
    void display_data();
};

Person::Person()
{
    first_name   = "";
    last_name    = "";
    street_name  = "";
    address      = 0;
    zip_code     = 0;
    phone_number = 0;
}

Person::Person(string f, string l, string s, int a, int z, int p)
{
    first_name   = f;
    last_name    = l;
    street_name  = s;
    address      = a;
    zip_code     = z;
    phone_number = p;
}

void Person::change_data(string f, string l, string s, int a, int z, int p)
{
    first_name   = f;
    last_name    = l;
    street_name  = s;
    address      = a;
    zip_code     = z;
    phone_number = p;
}

void Person::display_data()
{
    cout << "Name is " << first_name << " " << last_name << endl;
    cout << "Address is " << address << " " << street_name << " " << zip_code
    << endl;
    cout << "Phone number is " << phone_number << endl;
}


#endif /* person_h */

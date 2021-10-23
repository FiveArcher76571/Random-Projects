//Saicharan Vemuri (FiveArcher76571)
//Rock Paper Scissors
//Start: June 28th, 2021

#include <iostream>
#include <string>
using namespace std;

int main() {
    
    cout << "Welcome to RPS!" << endl;
    string p1name;
    cout << "What's your name?" << endl;
    bool ok = false;
    while (!ok) {
        cin >> p1name;
        if (!cin) {
            cout << "Error. Please enter a valid name" << endl;
        }
        else {
            ok = true;
        }
    }




    cin.get();

    return 0;
}
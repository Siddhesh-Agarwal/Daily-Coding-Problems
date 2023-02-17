// This problem was asked by Two Sigma.

// Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
// implement a function rand7() that returns an integer from 1 to 7 (inclusive).

#include <iostream>
using namespace std;


int rand5() {
    int num = rand();
    cout << num << endl;
    return num % 5 + 1;
}

int rand7() {
    int num = rand();
    cout << num << endl;
    return num % 7 + 1;
}

int main() {
    cout << "Random number between 1 and 5 is: " << rand5() << endl;
    cout << "Random number between 1 and 7 is: " << rand7() << endl;
}
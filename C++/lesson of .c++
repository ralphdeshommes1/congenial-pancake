#include <iostream>
using namespace std;

int main(){
    // with const the varible cannot be changed
    // with "char" varibles, the quotactions count as part of the space in the index
    const char the_word[17] = "this";
    std:: cout << "this is working" << endl;
    std:: cout << the_word;


    return 0;
}
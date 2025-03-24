#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
using namespace std;


int main(void){
    char str1[12] = "yomama";
    char str2[12] = "mayoma";
    char str3[12] = "yomama";


    if(strcmp(str1,str2) == 0){
        std:: cout << "these strings are the same";
    }
    else{
        std:: cout << "these strings are not the same";
    }

    return 0;
}
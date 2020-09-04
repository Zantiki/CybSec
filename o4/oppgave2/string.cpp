//
// Created by sebastian on 28.08.2020.
//
#include <iostream>
using namespace std;

string string_modifier(string in_string){

    char to_find[3] = {'&', '<', '>'};
    string replacement[3] = {"&amp", "&lt", "&gt"};
    /*string in_string;
    //string *in_string = malloc(1000);
    cout << "Input a string: ";
    cin >> in_string;*/

    cout << "String before modification: " << in_string << endl;

    for(int i = 0; i < 3; i++){
        int found_index = in_string.find(to_find[i]);
        while(found_index > -1 and found_index < in_string.length()){
            in_string.replace(found_index, 1, replacement[i]);
            if(found_index+1 < in_string.length()-1){
                found_index = in_string.find(to_find[i], found_index+1);
            }
        }
    }
    cout << "String after modification: " << in_string << endl;
    return in_string;

}

int main(){
    string res = string_modifier("yoyo && <<<><>>> maccaflow");
    return 0;
}


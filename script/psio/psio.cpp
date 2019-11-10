#include <iostream>
#include <stdio.h>
#include <dos.h>
using namespace std;

int main(){
    //integer the psio
    int psio;
    bool check = (psio == 0);
    if (psio == 0){
        cout << psio << "   ->   " << psio + 0 << endl;
    }else if (psio == 1){
              cout << psio << "    ->    " << psio + 1 << endl;
          }else{
                return 0;
                }
}

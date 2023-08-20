#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    if(0<=num1<=10000 && 0<= num2 <= 10000){
       if (num1==num2) return 1;
        return -1;
    }
}
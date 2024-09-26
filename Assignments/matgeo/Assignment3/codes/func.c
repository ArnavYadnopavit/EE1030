#include <math.h>
int sub(int num1, int num2)
   {
    return num1-num2;
   }
int vector_norm(int* vector, int size) {
   
    int norm=0;
    for (int i=0;i<size;i++){
    norm+=(int)(vector[i]*vector[i]);
    }
    norm=((int)(sqrt((double)norm)));
    return norm ;
}

#include <stdio.h>
#include "mathfun.h"
int main(){
	int A[3]={-2,3,5},B[3]={1,2,3},C[3]={7,0,-1};
	FILE *ptr;
	ptr=fopen("data.txt","w");
	for (int i=0;i<=2;i++){

	fprintf(ptr, "%d ",A[i]);
	}
	fprintf(ptr,"\n");
	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",B[i]);
        }
	fprintf(ptr,"\n");
	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",C[i]);
        }
	return 0;
}


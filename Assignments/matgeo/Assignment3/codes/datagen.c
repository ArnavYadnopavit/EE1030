#include <stdio.h>
int main(){
	int A[2]={-3,-14},B[2]={-3,-5};
	FILE *ptr;
	ptr=fopen("data.txt","w");
	for (int i=0;i<=1;i++){

	fprintf(ptr, "%d ",A[i]);
	}
	fprintf(ptr,"\n");
	for (int i=0;i<=1;i++){
                
        fprintf(ptr, "%d ",B[i]);
        }
	
	return 0;
}


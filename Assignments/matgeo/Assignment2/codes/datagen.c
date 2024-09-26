#include <stdio.h>
int main(){
	int P[3]={4,2,-6},Q[3]={10,-16,6},R[3]={0,0,0},S[3]={0,0,0};
	FILE *ptr;
	ptr=fopen("data.txt","w");
	for (int i=0;i<=2;i++){

	fprintf(ptr, "%d ",P[i]);
	}
	fprintf(ptr,"\n");
	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",Q[i]);
        }
	for (int i=0;i<=2;i++){
	R[i]=(((0.5*P[i]+Q[i])*2)/3);
	}
	for (int i=0;i<=2;i++){
        S[i]=(2*P[i]+Q[i])/3;
        }
	fprintf(ptr,"\n");
	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",R[i]);
        }
	fprintf(ptr,"\n");

	for (int i=0;i<=2;i++){
                
        fprintf(ptr, "%d ",S[i]);
        }
	return 0;
}


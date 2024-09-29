#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

void point_gen(FILE *fptr, double **A, double **B, int num_points) {
    for (double i = 0; i <= num_points; i++) {
        double **output = Matsec(A, B, 2, (double) i / num_points);
        fprintf(fptr, "%lf,%lf\n", output[0][0], output[1][0]);
        freeMat(output,2);
    }
}

int main()
{
    double a, b, c, x1, y1, x2, y2, x3, y3, angleb;
    a = 4.285714286;
    c =  3.571428571;
    angleb = 60;
    b = sqrt(pow(a,2)+pow(c,2)- (2*a*c*cos(angleb)));
    
    int m = 2, n = 1;
    double **A = createMat(m, n);
    double **B = createMat(m, n);
    double **C = createMat(m, n);
    double radianb = angleb*M_PI/180;

    A[0][0] = c*cos(radianb);
    A[1][0] = c*sin(radianb);
    B[0][0] = 0;
    B[1][0] = 0;
    C[0][0] = a;
    C[1][0] = 0;

    FILE *fptr;
    fptr = fopen("triangle_points.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    point_gen(fptr, A, B, 10);
    point_gen(fptr, B, C, 10);
    point_gen(fptr, C, A, 10);

    freeMat(A, m);
    freeMat(B, m) ;
    freeMat(C, m) ;

    fclose(fptr) ;
    //original triangle
    double ao, bo, co, x1o, y1o, x2o, y2o, x3o, y3o, anglebo;
    ao = 6;
    co =  5;
    anglebo = 60;
    bo = sqrt(pow(ao,2)+pow(co,2)- (2*ao*co*cos(anglebo)));
    
    int mo = 2, no = 1;
    double **Ao = createMat(mo, no);
    double **Bo = createMat(mo, no);
    double **Co = createMat(mo, no);
    double radianbo = anglebo*M_PI/180;

    Ao[0][0] = co*cos(radianbo);
    Ao[1][0] = co*sin(radianbo);
    Bo[0][0] = 0;
    Bo[1][0] = 0;
    Co[0][0] = ao;
    Co[1][0] = 0;

    FILE *fptro;
    fptro = fopen("triangleo_points.txt", "w");
    if (fptro == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    point_gen(fptro, Ao, Bo, 10);
    point_gen(fptro, Bo, Co, 10);
    point_gen(fptro, Co, Ao, 10);

    freeMat(Ao, mo);
    freeMat(Bo, mo) ;
    freeMat(Co, mo) ;

    fclose(fptro) ;
}

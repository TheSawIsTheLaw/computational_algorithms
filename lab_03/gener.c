#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double func(double x){
    return sin(4 * x);
}

int main(){
    FILE *file = fopen("table.txt", "w");

    double start, stop, step;
    scanf("%lf%lf%lf", &start, &stop, &step);

    fprintf(file, "number of dots: %d\n\n", (int)((stop - start) / step) + 1);

    for (double cur = start; cur <= stop; cur += step){
        fprintf(file, "%lf %lf\n", cur, func(cur));
    }
    fclose(file);
}

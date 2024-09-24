#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void roots(int a, int b, int c)
{
    if (a == 0) return;
    int discrim = b*b - 4*a*c;
    float sqrt_discrim = sqrt(discrim);  
    //x1 and x2 are roots of our quadratic                           
    if (discrim >= 0)
    printf("x1= %f \n x2= %f ", (-b + sqrt_discrim)/(2*a) , (-b - sqrt_discrim)/(2*a));    
}

void main()
{
    int a,b,c; //ax^2 +bx +c is the quadratic 
    scanf("%d%d%d",&a,&b,&c);
    roots(a,b,c);
}
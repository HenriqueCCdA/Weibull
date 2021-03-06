#include<stdio.h>
#include<omp.h>
#include<math.h>
#include"Weibull.h"

/*********************************************************************/
int main(int argc, char *argv[]){

  double mu, sig, mui, sigi, b, c;
  double time;
/*...*/
  mu  = 386.95e0;
  sig = 265.84e0;
/*...................................................................*/

/*...*/
  time = omp_get_wtime();
  weibull(mu ,sig
         ,&b ,&c
         ,1.e-11,15000000
         ,0.5e0);
  time = omp_get_wtime() - time;
/*...................................................................*/

/*...*/
  printf("*********************************************************\n");
  printf("Time (s) = %.6lf\n", time);
  printf("*********************************************************\n");
/*...................................................................*/

/*...*/
  printf("*********************************************************\n");
  printf("c = %.6lf\n", c);
  printf("b = %.6lf\n", b);
  printf("*********************************************************\n");
/*...................................................................*/

/*...*/
  mui  = media( b, c);
  sigi = std( b, c);
/*...................................................................*/

/*...*/
  printf("*********************************************************\n");
  printf("mu    = %.6lf\nmui   = %.6lf\n|res| = %e\n"
        , mu, mui, fabs( mu - mui ));
  printf("\n");
  printf("sig   = %.6lf\nsigi  = %.6lf\n|res| = %e\n"
        , sig, sigi, fabs( sig - sigi ));
  printf("*********************************************************\n");
/*...................................................................*/

  return 0;
}
/*********************************************************************/
#ifndef _ADJCENCY_H_
  #define _ADJCENCY_H_

  #include<math.h>
  #include<stdio.h>

  int weibull(double const mu , double const sig
              ,double *b       , double *c
              ,double const tol, int const maxIt
              ,double const alf);

  double media(double b, double c);
  double var(double b, double c);
  double std(double b, double c);
  
#endif



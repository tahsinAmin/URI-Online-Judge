#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main()
{
  double a, square, a2, a3, AEHD, CG, A, F, FIHG, BEDC;
  while (cin >> a && a != EOF)
  {
    square = pow(a, 2.0);
    a2 = 60 / 360.0 * M_PI * pow(a, 2.0);
    a3 = a2 - (sqrt(3) / 4 * pow(a, 2.0));
    AEHD = a2 + a3;
    CG = M_PI * pow(a, 2.0) / 4 - AEHD;
    A = square - 4 * CG;
    F = square - M_PI * pow(a, 2.0) / 4 - CG;
    FIHG = 4 * F;
    BEDC = square - FIHG - A;

    printf("%.3lf %.3lf %.3lf\n", A, BEDC, FIHG);
  }
  return 0;
}

// https://www.youtube.com/watch?v=AavgJ_w2De4
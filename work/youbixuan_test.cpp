#include <iostream>
#include <cmath>

using namespace std;

void GetGaussianKernel(double **gaus, const int size, const double sigma);

int main(){
    int size;
    double sigma;
    cin >> size >> sigma;
    double **gaus = new double *[size];
    for(int i = 0; i < size; i++)
    {
        gaus[i] = new double[size];
    }
    GetGaussianKernel(gaus, size, sigma);
    return 0;
}

void GetGaussianKernel(double **gaus, const int size, const double sigma)
{
    const double PI = 4.0 * atan(1.0);
    int center = size/2;
    double sum = 0;
    for(int i = 0; i < size; i++)
    {
        for(int j = 0; j < size; j++)
        {
            gaus[i][j] = (1/(2*PI*sigma*sigma))*exp(-((i-center)*(i-center) + (j-center)*(j-center))/(2*sigma*sigma));
            sum += gaus[i][j];
        }
    }
    for(int i = 0; i < size; i++)
    {
        for(int j = 0; j < size; j++)
        {
            gaus[i][j] /= sum;
            cout << gaus[i][j] << " ";
        }
        cout << endl;
    }
    return;
}
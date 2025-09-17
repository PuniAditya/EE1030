#include <math.h>
void eigenvalues(const double A[], double* eigenvalues_out) {
    double trace = A[0] + A[3]; // a + d
    double det = A[0] * A[3] - A[1] * A[2]; // ad - bc
    double discriminant = trace * trace - 4 * det;
    if (discriminant < 0) {
        discriminant = 0;
    }
    eigenvalues_out[0] = (trace + sqrt(discriminant)) / 2.0;
    eigenvalues_out[1] = (trace - sqrt(discriminant)) / 2.0;
}

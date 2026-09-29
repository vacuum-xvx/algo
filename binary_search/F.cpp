#include <iostream>

using namespace std;

int main() {
    long long n, x, y;
    cin >> n >> x >> y;

    long long fastest = min(x, y);

    long long l = -1;
    long long r = fastest * (n - 1);

    for (int i = 0; i < 100; i++) {
        long long m = (l + r) / 2;

        long long copies = m / x + m / y;

        if (copies >= n - 1) {
            r = m;
        } else {
            l = m;
        }
    }

    cout << fastest + r;

    return 0;
}
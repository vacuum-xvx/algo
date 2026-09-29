#include <iostream>
#include <algorithm>

using namespace std;

bool check(long long w, long long h, long long n, long long s) {
    return (s / w) * (s / h) >= n;
}

int main() {
    long long w, h, n;
    cin >> w >> h >> n;

    long long l = 0;
    long long r = max(w, h) * n;

    for (int i = 0; i < 100; i++) {
        long long m = l + (r - l) / 2;

        if (m == 0) {
            break;
        }

        if (!check(w, h, n, m)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << r;

    return 0;
}
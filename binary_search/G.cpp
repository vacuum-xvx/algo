#include <iostream>
#include <vector>

using namespace std;

bool good(const vector<int>& a, int k, int x) {
    int cnt = 0;

    for (int length : a) {
        cnt += length / x;
    }

    return cnt >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int l = 0;
    int r = 10000000 + 1;

    for (int i = 0; i < 100; i++) {
        int m = (l + r) / 2;

        if (m == 0) {
            break;
        }

        if (good(a, k, m)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << l;

    return 0;
}
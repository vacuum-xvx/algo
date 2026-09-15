#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int>& A) {
    int cnt[101] = {0};

    for (int x : A) {
        cnt[x]++;
    }

    int pos = 0;
    for (int num = 0; num <= 100; num++) {
        for (int i = 0; i < cnt[num]; i++) {
            A[pos++] = num;
        }
    }
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }

    CountSort(A);

    for (int i = 0; i < (int)A.size(); i++) {
        cout << A[i];
        if (i + 1 < (int)A.size()) cout << ' ';
    }
    cout << endl;

    return 0;
}

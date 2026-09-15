#include <iostream>
#include <vector>

using namespace std;

void BubbleSort(vector<int>& A) {
    int n = A.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (A[j] < A[j + 1]) {
                swap(A[j], A[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }

    BubbleSort(A);

    for (int i = 0; i < (int)A.size(); i++) {
        cout << A[i];
        if (i + 1 < (int)A.size()) cout << " ";
    }
    cout << endl;

    return 0;
}

#include <iostream>
#include <vector>

using namespace std;

void SelectionSort(vector<int>& A) {
    int n = A.size();

    for (int i = 0; i < n - 1; i++) {
        int maxIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[maxIndex]) {
                maxIndex = j;
            }
        }
        swap(A[i], A[maxIndex]);
    }
}

int main() {
    vector<int> A;
    int x;

    while (cin >> x) {
        A.push_back(x);
    }

    SelectionSort(A);

    for (int i = 0; i < (int)A.size(); i++) {
        cout << A[i];
        if (i + 1 < (int)A.size()) cout << " ";
    }
    cout << endl;

    return 0;
}

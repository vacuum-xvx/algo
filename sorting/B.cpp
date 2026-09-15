#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& A) {
    int n = A.size();
    for (int i = 1; i < n; i++) {
        int buffer = A[i];
        int j = i;
        while (j > 0 && A[j - 1] > buffer) {
            A[j] = A[j - 1];
            j--;
        }
        A[j] = buffer;
    }
}

int main() {
    vector<int> A;
    int x;
    while (cin >> x) {
        A.push_back(x);
    }

    InsertionSort(A);

    for (int i = 0; i < (int)A.size(); i++) {
        cout << A[i];
        if (i + 1 < (int)A.size()) cout << " ";
    }
    cout << endl;

    return 0;
}

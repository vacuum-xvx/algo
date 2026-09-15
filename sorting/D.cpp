#include <iostream>
#include <vector>

using namespace std;

int BubbleSort(vector<int>& A) {
    int n = A.size();
    int count = 0;

    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (A[j] > A[j + 1]) {
                swap(A[j], A[j + 1]);
                swapped = true;
                count++;
            }
        }
        if (!swapped) {
            break;
        }
    }

    return count;
}

int main() {
    int n;
    if (!(cin >> n)) {
        return 0;
    }

    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    int swaps = BubbleSort(A);
    cout << swaps << endl;

    return 0;
}

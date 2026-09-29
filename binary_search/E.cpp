#include <iostream>
#include <vector>

using namespace std;

bool canPlace(vector<int>& boxes, int k, int dist) {
    int cows = 1;
    int lastBox = boxes[0];

    for (int i = 1; i < boxes.size(); i++) {
        if (boxes[i] - lastBox >= dist) {
            cows++;
            lastBox = boxes[i];
        }
    }

    return cows >= k;
}

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> boxes(n);

    for (int i = 0; i < n; i++) {
        cin >> boxes[i];
    }

    int l = 0;
    int r = boxes[n - 1] - boxes[0] + 1;

    while (r - l > 1) {
        int mid = (l + r) / 2;

        if (canPlace(boxes, k, mid)) {
            l = mid;
        } else {
            r = mid;
        }
    }

    cout << l;

    return 0;
}
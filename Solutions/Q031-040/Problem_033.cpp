// Compute the running median of a sequence of numbers. That is, given a stream of 
// numbers, print out the median of the list so far on each new element.

// Recall that the median of an even-numbered list is the average of the two middle numbers.
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int>> minHeap;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        if (maxHeap.empty() || x <= maxHeap.top())
            maxHeap.push(x);
        else
            minHeap.push(x);
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
        if (maxHeap.size() == minHeap.size())
            cout << (maxHeap.top() + minHeap.top()) / 2.0 << endl;
        else
            cout << maxHeap.top() << endl;
    }
}
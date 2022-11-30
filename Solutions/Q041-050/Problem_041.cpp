// Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
// and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If
// there are multiple possible itineraries, return the lexicographically smallest one. All flights must
// be used in the itinerary.

// For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
// and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

// Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM',
// you should return null.

// Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
// you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a
// valid itinerary. However, the first one is lexicographically smaller.

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cout << "number of pairs: " << endl;
    cin >> n;
    cout << "\n";
    vector<pair<string, string>> list;
    string temp1, temp2;
    for (int i = 0; i < n; i++)
    {
        cout << "\nstart #" << i << ": " << endl;
        cin >> temp1;
        cout << "\nend #" << i << ": " << endl;
        cin >> temp2;
        list.emplace_back(temp1, temp2);
    }
    string start;
    cout << "\nStart place: " << endl;
    cin >> start;

    vector<string> nodes;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (list[j].first.compare(start) == 0)
            {
                start = list[j].second;
                nodes.push_back(list[j].first);
                list.erase(list.begin() + j);
                break;
            }
        }
    }
    nodes.push_back(start);
    for (int i = 0; i < nodes.size(); i++)
        cout << nodes[i] << " ";
}
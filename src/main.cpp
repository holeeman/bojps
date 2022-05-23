#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);

    for (int i = 0; i < n; i++)
    {
        int x, y;
        cin >> x >> y;
        a[i] = {y, x};
    }
    sort(a.begin(), a.end());
    for (auto &p : a)
    {
        cout << p.second << ' ' << p.first << '\n';
    }
}
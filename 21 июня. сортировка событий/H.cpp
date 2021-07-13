/*
 * author : frija
 * c++ 17.12
*/

#include <bits/stdc++.h>

using namespace std;

#define int long long
#define fi first
#define se second
#define mp make_pair
#define pb push_back

bool comp(pair <int, int> a, pair <int, int> b)
{
    return a.fi < b.fi || a.fi == b.fi && a.se > b.se;
}

void solve()
{
    int n;
    cin >> n;
    vector <pair <int, int> > a( n);
    for (int i = 0; i < 2 * n; i ++)
    {
        cin >> a[i].fi >> a[i].se;
    }
    sort(a.begin(), a.end(), comp);
    vector <pair <int, int> > t(2 * n);
    for (int i = 0; i < n; i ++)
    {
        t[i * 2].fi = a[i].fi;
        t[i * 2].se = 1;
        t[i * 2 + 1].fi = a[i].se;
        t[i * 2 + 1].se = -1;
    }
    sort(t.begin(), t.end());

    int cnt = 100000;
    int cur = 1;
    for (int i = 1; i < n; i ++)
    {
        if (t[i].se == 1)
        {
            cur ++;
            cnt = min()
        }
    }
    if (a[0].fi != 1)
        ans = false;
    if (a[2 * n - 1].fi != 10000)
        ans = false;

    cout << (ans ? "Accepted": "Wrong Answer");
}

int32_t main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t = 1;
    cin >> t;
    while (t--)
    {
        solve();
        cout << "\n";
    }
}


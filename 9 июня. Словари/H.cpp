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

int32_t main()
{
    int g, q;
    cin >> g >> q;
    vector <int> a(52, 0);
    vector <int> cur(52, 0);
    for (int i = 0; i < g; i ++)
    {
        char c;
        cin >> c;
        if (c >= 'a' && c <= 'z')
            a[c - 'a'] += 1;
        else
            a[26 + c - 'A'] += 1;
    }

    int ans = 0;
    string s;
    cin >> s;
    for (int i = 0; i < q; i ++)
    {
        char c = s[i];
        if (c >= 'a' && c <= 'z')
            cur[c - 'a'] += 1;
        else
            cur[26 + c - 'A'] += 1;
        if (i - g >= 0)
        {
            c = s[i - g];
            if (c >= 'a' && c <= 'z')
                cur[c - 'a'] -= 1;
            else
                cur[26 + c - 'A'] -= 1;
        }
        bool was = true;
        for (int j = 0; j < 52; j ++)
        {
            if (a[j] != cur[j])
                was = false;
        }
        if (was)
            ans += 1;
    }
    cout << ans;
}

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

int manh(pair <int, int> a, int x, int y)
{
    return abs(a.fi - x) + abs(a.se - y);
}

int32_t main()
{
    int t, d, n;
    set <pair <int, int> > s;
    s.insert(mp(0, 0));
    cin >> t >> d >> n;
    for (int _ = 0; _ < n; _ ++)
    {
        for (int j = 0; j < t; j ++)
        {
            set <pair <int, int> > s_new;
            set <pair <int, int> >  ::iterator it = s.begin();
            while (it != s.end())
            {
                pair <int, int> a = *it;
                s_new.insert(mp(a.fi + 1, a.se));
                s_new.insert(mp(a.fi - 1, a.se));
                s_new.insert(mp(a.fi, a.se + 1));
                s_new.insert(mp(a.fi, a.se - 1));
                s_new.insert(mp(a.fi , a.se));
                it ++;
            }
            s = s_new;
        }
        set <pair <int, int> >  ::iterator it = s.begin();
        int x, y;
        cin >> x >> y;
        it = s.begin();
        set <pair <int, int> > ss;
        while (it != s.end())
        {
            if (manh(*it, x, y) <= d)
            {
                ss.insert(*it);
            }
            it ++;
        }
        s = ss;
    }
    cout << s.size() << "\n";
    set <pair <int, int> >  :: iterator it = s.begin();
    while (it != s.end())
    {
        pair <int, int> a = *it;
        cout << a.fi << " " << a.se << "\n";
        it++;
    }
    return 0;
}

#include <iostream>
using namespace std;

int main() {
    int q, a, b, c, p = 0;
    
    cin >> q >> a >> b >> c;

    while (q > 0) {
        //First machine
        a++;
        q--;
        p++;
        if (a == 35) {
            q += 30;
            a = 0;
        }
        if (q == 0) {
            break;
        }

        //Second machine
        b++;
        q--;
        p++;
        if (b == 100) {
            q += 60;
            b = 0;
        }
        if (q == 0) {
            break;
        }

        //Third machine
        c++;
        q--;
        p++;
        if (c == 10) {
            q += 9;
            c = 0;
        }
        if (q == 0) {
            break;
        }
    }
    cout << "Martha plays " << p << " times before going broke.";
}

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1000000; // A value larger than any possible number of strokes

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int total_distance;
    cin >> total_distance;

    int num_clubs;
    cin >> num_clubs;

    vector<int> clubs(num_clubs);
    for (int i = 0; i < num_clubs; ++i) {
        cin >> clubs[i];
    }

    // dp[i] will store the minimum strokes to reach distance 'i'
    // Size is total_distance + 1 to accommodate index 0 to total_distance
    vector<int> dp(total_distance + 1, INF);

    // Base case: It takes 0 strokes to travel distance 0
    dp[0] = 0;

    // Iterate through every distance from 0 up to the target
    for (int i = 0; i <= total_distance; ++i) {
        // If the current distance 'i' is unreachable, we can't hit from here
        if (dp[i] == INF) continue;

        // Try hitting with every club from the current position
        for (int club_dist : clubs) {
            int next_pos = i + club_dist;

            // Ensure we don't overshoot the hole
            if (next_pos <= total_distance) {
                // Update the next position if we found a faster way to get there
                // (Current strokes + 1)
                if (dp[i] + 1 < dp[next_pos]) {
                    dp[next_pos] = dp[i] + 1;
                }
            }
        }
    }

    // Check the value at the target distance
    if (dp[total_distance] == INF) {
        cout << "Roberta acknowledges defeat." << endl;
    } else {
        cout << "Roberta wins in " << dp[total_distance] << " strokes." << endl;
    }

    return 0;
}
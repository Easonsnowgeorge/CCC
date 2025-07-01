

def max_consecutive_sunshine_sliding_window(n,weather):
    left = 0
    right = 0
    p_count = 0
    max_len = 0

    while right < n:
        if weather[right] == 'P':
            p_count += 1

        while p_count > 1:
            if weather[left] == 'P':
                p_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)
        right += 1

    return max_len

n = int(input())

weather = []
for i in range(n):
    weather.append(input())
result = max_consecutive_sunshine_sliding_window(n,weather)
print(result)
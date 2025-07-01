# Read the width of the sign
width = int(input())
# Split the input string into words
s = "WELCOME TO CCC GOOD LUCK TODAY".split()

# Create a list of lengths for each word
l = [len(word) for word in s]
# Create a list of required spaces (including the word length and a space)
req = [len(s[0])]
for i in range(1, len(s)):
    req.append(len(s[i]) + 1)  # +1 for the space between words

# Variables to keep track of total length and the segments of words
total = 0
segments = [[]]
i = 0

# Loop to divide words into lines based on the width of the sign
while i < len(req):
    if total + req[i] > width:  # Start a new line if the current word doesn't fit
        total = 0
        segments.append([])
        req[i] -= 1  # The space before the word is not needed on a new line
        continue
    total += req[i]
    segments[-1].append(s[i])
    i += 1

# Process each line to add dots as separators
for words in segments:
    if len(words) == 1:  # Special case for a line with only one word
        print(words[0] + "." * (width - len(words[0])))
        continue

    separator = '.'
    total_length = sum(len(word) for word in words)
    gaps = len(words) - 1
    separator_count = width - total_length
    separators_per_gap, extras = divmod(separator_count, gaps)
    res = ''

    # Distribute the separators (dots) among the gaps
    for i, word in enumerate(words):
        res += word
        if i < gaps:
            res += separator * separators_per_gap
            if i < extras:  # Additional dot for the gaps on the left
                res += separator
    print(res)
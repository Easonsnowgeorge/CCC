sentence = input()

num_happy = sentence.count(':-)')
num_sad = sentence.count(':-(')

if num_happy == 0 and num_sad == 0:
    print('none')
elif num_happy == num_sad:
    print('unsure')
elif num_happy > num_sad:
    print('happy')
else:
    print('sad')

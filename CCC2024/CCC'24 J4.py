# def find_troublesome_keys(typed, displayed):
#     # If lengths differ, we know there's a quiet key
#     has_quiet_key = len(typed) != len(displayed)
#
#     # Try each possible letter as the silly key
#     for silly_key in set(typed):
#         # Try each possible letter as the wrong display
#         for wrong_display in set(displayed):
#             # Skip if the wrong display letter appears in typed (per constraint 3)
#             if wrong_display in typed:
#                 continue
#
#             # Create a mapping for how the string should display
#             current_display = ""
#             quiet_key_candidate = None
#             valid = True
#             prev_was_quiet = False
#             prev_was_silly = False
#
#             # Try to match the displayed string
#             i = 0  # Index for displayed string
#             for j, char in enumerate(typed):
#                 if char == silly_key:
#                     # Check constraint: no silly key after quiet key
#                     if prev_was_quiet:
#                         valid = False
#                         break
#                     current_display += wrong_display
#                     prev_was_silly = True
#                     prev_was_quiet = False
#                     i += 1
#                 else:
#                     # If character doesn't show up in output at the expected position
#                     if i >= len(displayed) or (char != displayed[i]):
#                         # If we haven't found a quiet key yet
#                         if quiet_key_candidate is None:
#                             quiet_key_candidate = char
#                             # Check constraint: no quiet key after silly key
#                             if prev_was_silly:
#                                 valid = False
#                                 break
#                             prev_was_quiet = True
#                             prev_was_silly = False
#                         # If this is a different character than our quiet key candidate
#                         elif char != quiet_key_candidate:
#                             valid = False
#                             break
#                         # If this is our quiet key
#                         else:
#                             # Check constraint: no quiet key after silly key
#                             if prev_was_silly:
#                                 valid = False
#                                 break
#                             prev_was_quiet = True
#                             prev_was_silly = False
#                     else:
#                         current_display += char
#                         prev_was_quiet = False
#                         prev_was_silly = False
#                         i += 1
#
#             # Check if this combination works
#             if valid and current_display == displayed:
#                 return silly_key, wrong_display, quiet_key_candidate if has_quiet_key else None
#
#     return None  # No solution found
#
#
# def solve_keyboard_problem(typed, displayed):
#     result = find_troublesome_keys(typed, displayed)
#     if result:
#         silly_key, wrong_display, quiet_key = result
#         # Print first line: silly key and wrong display
#         print(f"{silly_key} {wrong_display}")
#         # Print second line: quiet key or dash
#         print(f"{quiet_key if quiet_key else '-'}")
#
#
# typed= input()
# displayed = input()
# solve_keyboard_problem(typed, displayed)

typed = input()
displayed = input()
dlen = len(typed)-len(displayed)
twokey = set()
check = set()
temp = ""
temp2 = ""
wrongkey = str(set(displayed) - set(typed))
if len(typed) == len(displayed):
    quietkey ="-"
    for i in range(len(typed)):
        if typed[i] != displayed[i]:
            print(typed[i],displayed[i])
            print(quietkey)
            exit()
else:
    twokey = set(typed) - set(displayed)
    key1 = twokey.pop()
    key2 = twokey.pop()
    temp = ""
    key1count = typed.count(key1)
    key2count = typed.count(key2)
    if key1count != key2count:
        if key1count == dlen:
            quietkey = key1
        else:
            quietkey = key2
        for i in range(len(typed)):
            if typed[i] == quietkey:
                continue
            else:
                temp += typed[i]
        for j in range(len(displayed)):
            if temp[j] != displayed[j]:
                print(temp[j],displayed[j])
                print(quietkey)
                exit()
    else:
        quietkey = key1
        for i in range(len(typed)):
            if typed[i] == quietkey:
                continue
            else:
                temp += typed[i]
        for j in range(len(displayed)):
            if temp[j] != displayed[j]:
                check.add((temp[j],displayed[j]))
        if len(check) == 1:
            print(temp[j],displayed[j])
            print(quietkey)
            exit()
        else:
            quietkey = key2
            for i in range(len(typed)):
                if typed[i] == quietkey:
                    continue
                else:
                    temp2 += typed[i]
            for j in range(len(displayed)):
                if temp2[j] != displayed[j]:
                    print(temp2[j],displayed[j])
                    print(quietkey)
                    exit()






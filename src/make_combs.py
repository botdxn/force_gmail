from itertools import combinations


def make_combs(path):
    print("FUNC make_combs STARTED")
    with open(path, 'r') as f:
        pw_list = f.readlines()
    print("Password file read.")

    comb_list = list()
    for n in range(len(pw_list) + 1):
        comb_list += list(combinations(pw_list, n))

        joind_comb_list = list()
    for elem in comb_list:
        joind_comb_list.append(''.join(elem).replace("\n", ""))

    no_long_list = [x for x in joind_comb_list if len(x) <= 40]
    print(f"Total password combinations: {len(no_long_list)}")
    print("Combination list completed.")

    return no_long_list

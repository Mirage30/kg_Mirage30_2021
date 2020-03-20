import sys


def check_map(src, tar):
    if len(src) != len(tar):
        return False
    map = {}
    for i in range(len(src)):
        if src[i] not in map:
            map[src[i]] = tar[i]
        elif map[src[i]] != tar[i]:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Missing arguments')
    elif len(sys.argv) > 3:
        print('Too many arguments')
    else:
        print(check_map(sys.argv[1], sys.argv[2]))

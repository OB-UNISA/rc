import argparse

SEP = ':'

def sep_strip(data, space=False):
    res = data.split(SEP)[1].strip()
    if space:
        res = res.split(' ')[0]
    return res


def abToDict(input):
    ab_dict = {}
    ab_dict['server'] = sep_strip(input[0])
    ab_dict['doc_len'] = sep_strip(input[5], True)
    ab_dict['conc'] = sep_strip(input[7])
    ab_dict['time'] = sep_strip(input[8], True)
    ab_dict['r_comp'] = sep_strip(input[9])
    ab_dict['r_fail'] = sep_strip(input[10])
    ab_dict['rps'] = sep_strip(input[13], True)
    ab_dict['tpr'] = sep_strip(input[14], True)

    return ab_dict



if __name__ == '__main__':
    parser = argparse.ArgumentParser('ab to CSV')
    in_grp = parser.add_mutually_exclusive_group(required=True)
    in_grp.add_argument('--inp', help='Input file')
    parser.add_argument('--out', required=True, help='Output file')
    parser.add_argument('-a', action='store_true', help='Append to input file')
    in_grp.add_argument('--stdin', action='store_true', help='Input from stdin')

    args = parser.parse_args()

    if args.stdin:
        data = []
        while True:
            try:
                line = input()
                data.append(line)
            except EOFError:
                break
    else:
        with open(args.inp, 'r') as f:
            data = f.readlines()

    mode = 'a' if args.a else 'w'
    with open(args.out, mode) as f:
        ab_dict = abToDict(data[7:])
        print(ab_dict)

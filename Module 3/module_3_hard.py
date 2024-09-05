data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    count = 0
    args = args[0]
    print(type(args), args)

    if isinstance(args, int):
        print(f'this is int: {args}\n')
        count += args
    elif isinstance(args, str):
        count += len(args)
    elif isinstance(args, dict):
        print(list(args.items()))
        return calculate_structure_sum(list(args.items()))
    elif isinstance(args, set):
        if len(args) == 0:
            return 0
        else:
            for iter_ in args:
                return calculate_structure_sum(iter_)
    elif isinstance(args, list | tuple):
        if len(args) == 0:
            return 0
        first = calculate_structure_sum(args[0])
        if len(args) > 1:
            print(args[0], '|', args[1:])
            print(f'count: {count} \n')
            return first + calculate_structure_sum(args[1:])
        else:
            return first

    return count



result = calculate_structure_sum(data_structure)
print(f'result: {result}')

def str_to_set(str_value):
    input1 = str_value.split(',')
    return set([int(i) for i in input1])


def main(inputs):
    set1 = str_to_set(inputs['input_name_0'])
    set2 = str_to_set(inputs['input_name_1'])

    set_union = set1.union(set2)

    set_intersection = set1.intersection(set2)

    set_difference = set1.difference(set2)

    set_symmetric_difference = set1.symmetric_difference(set2)

    if set1 == set2:
        set_equality = "A = B"
    else:
        set_equality = "A ≠ B"

    if set2.issubset(set1):
        set_subset = "A ⊆ B"
    else:
        set_subset = "A ⊄ B"

    if set1.issuperset(set2):
        set_superset = "A ⊃ B"
    else:
        set_superset = "A ⊅ B"

    return {
        "set1": set1,
        "set2": set2,
        "union": set_union,
        "intersection": set_intersection,
        "difference": set_difference,
        "symmetric_difference": set_symmetric_difference,
        "equality": set_equality,
        "subset": set_subset,
        "superset": set_superset}

from . import compare as _compare
from . import quick, insert, merge

_ALGORITHMS = {
    "quick": quick.sort,
    "insert": insert.sort,
    "merge": merge.sort,
}


def sort(arr, by="id", reverse=False, algo="quick"):
    if algo not in _ALGORITHMS:
        raise ValueError(f"Неизвестный алгоритм: {algo!r}")
    
    rules = _compare.build_rules(by, reverse)
    comparator = _compare.make_comparator(rules)
    return _ALGORITHMS[algo](arr, comparator)
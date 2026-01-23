import time

def progressBar(sub_title, part, total, length=50):
    frac = part/total
    completed = int(frac * length)
    missing = length - completed
    bar = f"{sub_title}\n[{'#'* completed}{'-'*missing}]{frac:.2%}"
    return bar
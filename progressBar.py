import time

def progressBar(part, total, length=50):
    frac = part/total
    completed = int(frac * length)
    missing = length - completed
    bar = f"[{'#'* completed}{'-'*missing}]{frac:.2%}"
    return bar



def fib(n, evaluated):
    """Return the value of fibonacci sequence at position n"""
    #0, 1, 1, 2, 3, 5
    if n == 0 or n == 1:
        return n
    elif n in evaluated:
        return evaluated[n]
    else:
        twoPositionsBefore = n-2
        onePositionBefore = n-1
        twoBefore = fib(n-2, evaluated)
        oneBefore = fib(n-1, evaluated)
        evaluated[twoPositionsBefore] = twoBefore
        evaluated[onePositionBefore] = oneBefore
        return twoBefore + oneBefore


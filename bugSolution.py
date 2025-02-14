def function_with_uncommon_error(a, b):
    try:
        if a == 0:
            return b / a 
        return a + b
    except ZeroDivisionError:
        return float('inf') # Or handle it appropriately for your application
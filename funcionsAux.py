from functools import reduce
import numpy as np

def realizar_operacion(op, op1, op2):
    # Comprobar length error
    if len(op1) != len(op2) and len(op1) != 1 and len(op2) != 1 and op != ',' and op != '{':
        raise Exception("Error de longitud.")
    
    arr1 = np.array(op1)
    arr2 = np.array(op2)

    if op == '+':
        res = arr1 + arr2
    elif op == '-':
        res = arr1 - arr2
    elif op == '*':
        res = arr1 * arr2
    elif op == '%':
        res = arr1 // arr2
    elif op == '^':
        res = arr1 ** arr2
    elif op == '|':
        res = arr2 % arr1
    elif op == '=':
        res = (arr1 == arr2).astype(int)
    elif op == '<>':
        res = (arr1 != arr2).astype(int)
    elif op == '<':
        res = (arr1 < arr2).astype(int)
    elif op == '<=':
        res = (arr1 <= arr2).astype(int)
    elif op == '>':
        res = (arr1 > arr2).astype(int)
    elif op == '>=':
        res = (arr1 >= arr2).astype(int)
    elif op == ',':
        res = np.concatenate((arr1, arr2))
    elif op == '#':
        mask = arr1.astype(bool)
        res = arr2[mask]
    elif op == '{':
        res = np.array([int(arr2[i]) for i in arr1])
    else:
        raise Exception(f"Operador no soportado: {op}")

    return res.tolist()

def compon(ops, x):
    for op in reversed(ops):
        if callable(op):
            x = op(x)
        else:
            raise Exception(f"Operador no soportado en la composicion: {op}")
    return x

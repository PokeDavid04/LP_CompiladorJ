from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from gVisitor import gVisitor
from functools import reduce
import numpy as np
import sys


class EvalVisitor(gVisitor):
    def __init__(self):
        self.variables = {}
        self.funciones = {}

    def visitArrel(self, ctx):
        # (statement? comment? '\n')* EOF
        children = list(ctx.getChildren())

        for child in children:
            if child.getText() != '<EOF>':
                res = self.visit(child)

                if isinstance(res, str):
                    if res in self.variables:
                        print(res, '=:', end=' ')
                        for r in self.variables[res]:
                            if isinstance(r, int) and r < 0:
                                print("_" + str(abs(r)), end=' ')
                            else: 
                                print(r, end=' ')
                    elif res in self.funciones:
                        print(res, '=:', end=' ')
                        func = self.funciones[res]
                        print("<funcion>", end=' ')

                elif isinstance(res, list):
                    for element in res:
                        if isinstance(element, int) and element < 0:
                            print("_" + str(abs(element)), end=' ')
                        else:
                            print(element, end=' ')

                elif child.getText() == '\n':
                    print()

    def visitAsignacion(self, ctx):
        # ID '=:' expr
        [variable, _, expresion] = list(ctx.getChildren())
        var_name = variable.getText()
        value = self.visit(expresion)
        
        self.variables[var_name] = value
        return var_name
    
    def visitExpresion(self, ctx):
        # expr
        [expresion] = list(ctx.getChildren())
        return self.visit(expresion)

    def visitAsignacion_funcion(self, ctx):
        # ID '=:' funcion
        [name, _, funcion] = list(ctx.getChildren())
        fun_name = name.getText()
        func = self.visit(funcion)
        self.funciones[fun_name] = func
        return fun_name


    def visitParentesis(self, ctx):
        # '(' expr ')'
        [_, expressio, _] = list(ctx.getChildren())
        return self.visit(expressio)
    
    def visitOperacion_binaria(self, ctx):
        # expr operador_bin expr
        [expr1, operacion, expr2] = list(ctx.getChildren())
        res1 = self.visit(expr1)
        res2 = self.visit(expr2)
        op = self.visit(operacion)

        return realizar_operacion(op, res1, res2)

    def visitOperacion_unaria(self, ctx):
        # operador_un expr
        [operador, expresion] = list(ctx.getChildren())
        exp = self.visit(expresion)
        op = self.visit(operador)

        if op == ']':
            return exp
        elif op == '#':
            return [len(exp)]
        elif op == 'i.':
            return [i for i in range(exp[0])]
        
    def visitOperacion_binaria_combinada(self, ctx):
        # expr operador_bin operador_bin_comb expr
        [expr1, operacion, mod, expr2] = list(ctx.getChildren())
        res1 = self.visit(expr1)
        res2 = self.visit(expr2)
        op = self.visit(operacion)
        mod_op = self.visit(mod)

        if mod_op == '~':
            return realizar_operacion(op, res2, res1)

    def visitOperacion_unaria_combinada(self, ctx):
        # operador_bin operador_un_comb expr
        [operacion, mod, expresion] = list(ctx.getChildren())
        exp = self.visit(expresion)
        op = self.visit(operacion)
        mod_op = self.visit(mod)

        if mod_op == ':':
            return realizar_operacion(op, exp, exp)
        elif mod_op == '/':
            if op == '+':
                return [reduce(lambda acc, y: acc + y, exp)]
            if op == '-':
                return [reduce(lambda acc, y: y - acc, exp)]
            elif op == '*':
                return [reduce(lambda acc, y: acc * y, exp)]
            elif op == '%':
                return [reduce(lambda acc, y: y // acc, exp)]
            elif op == '^':
                return [reduce(lambda acc, y: y ** acc, exp)]
            elif op == '|':
                return [reduce(lambda acc, y: y % acc, exp)]
            else:
                raise Exception(f"Operador no soportado para fold: {op}")

    def visitLlamada_funcion(self, ctx):
        # ID expr
        [name, expresion] = list(ctx.getChildren())
        fun_name = name.getText()
        expr = self.visit(expresion)
        func = self.funciones.get(fun_name)
        if func is None:
            raise Exception(f"Funcion '{fun_name}' no definida.")
        return func(expr)

    def visitOperando(self, ctx):
        # operand+
        children = list(ctx.getChildren())
        return [self.visit(child) for child in children]
    
    def visitVariable(self, ctx):
        # ID
        [variable] = list(ctx.getChildren())
        var_name = variable.getText()
        
        if var_name not in self.variables:
            raise Exception(f"Variable '{var_name}' no definida.")
        
        return self.variables[var_name]
    
    def visitOperador_binario(self, ctx):
        # ('+'|'-'|'*'|'%'|'^'|'|'|'='|'<>'|'<'|'>'|'<='|'>=')
        [op] = list(ctx.getChildren())
        return op.getText()
    
    def visitOperador_unario(self, ctx):
        # (']'|'#'|'i.')
        [op] = list(ctx.getChildren())
        return op.getText()
    
    def visitOperador_binario_combinacion(self, ctx):
        # ('~')
        [op] = list(ctx.getChildren())
        return op.getText()
    
    def visitOperador_unario_combinacion(self, ctx):
        # (':'|'/')
        [op] = list(ctx.getChildren())
        return op.getText()
    
    def visitOperador_composicion(self, ctx):
        # ('@:')
        [op] = list(ctx.getChildren())
        return op.getText()

    def visitF_comp(self, ctx):
        # funcion_atom ('@:' funcion_atom)*
        children = list(ctx.getChildren())
        ops = []
        for i in range(len(children)):
            name = children[i].getText()
            if name == '@:':
                continue
            elif name in self.funciones:
                op = self.funciones[name]
            else:
                op = self.visit(children[i])
            ops.append(op)
        return lambda x: compon(ops, x)

    def visitF_un(self, ctx):
        # operador_un
        [operador] = list(ctx.getChildren())
        op = self.visit(operador)
        if op == ']':
            return lambda x: x
        elif op == '#':
            return lambda x: [len(x)]
        elif op == 'i.':
            return lambda x: [i for i in range(x[0])]

    def visitF_bin(self, ctx):
        # expr operador_bin ']'
        [expr, op, _] = list(ctx.getChildren())
        exp = self.visit(expr)
        op = self.visit(op)
        return lambda x: realizar_operacion(op, exp, x)

    
    def visitF_comb_un(self, ctx):
        # operador_bin operador_un_comb
        [op, mod] = list(ctx.getChildren())
        op = self.visit(op)
        mod_op = self.visit(mod)
        if mod_op == ':':
            return lambda x: realizar_operacion(op, x, x)
        elif mod_op == '/':
            if op == '+':
                return lambda x: [reduce(lambda acc, y: acc + y, x)]
            if op == '-':
                return lambda x: [reduce(lambda acc, y: y - acc, x)]
            elif op == '*':
                return lambda x: [reduce(lambda acc, y: acc * y, x)]
            elif op == '%':
                return lambda x: [reduce(lambda acc, y: y // acc, x)]
            elif op == '^':
                return lambda x: [reduce(lambda acc, y: y ** acc, x)]
            elif op == '|':
                return lambda x: [reduce(lambda acc, y: y % acc, x)]
            else:
                raise Exception(f"Operador no soportado para fold: {op}")


    def visitF_id(self, ctx):
        # ID
        [id] = list(ctx.getChildren())
        fun_name = id.getText()
        if not fun_name in self.funciones:
            raise Exception(f"Funcion '{fun_name}' no definida.")
        return self.funciones[fun_name]
    
    def visitNumero(self, ctx):
        # NUM = [0-9]+
        [numero] = list(ctx.getChildren())
        return int(numero.getText())
    
    def visitNumero_negativo(self, ctx):
        # NUM_NEG = '_' [0-9]+
        [negnum] = list(ctx.getChildren())
        text = negnum.getText()
        numero = text[1:]
        return -int(numero)

    def visitComentario(self, ctx):
        # 'NB.' (ID | NUM | NUM_NEG)* 
        return None


def realizar_operacion(op, op1, op2):
    # Comprobar length error
    if len(op1) != len(op2) and len(op1) != 1 and len(op2) != 1 and op != ',' and op != '{':
        raise Exception("Las listas deben tener la misma longitud o una de ellas debe tener un solo elemento.")
    
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
        raise Exception(f"Operador no soportado: {op} (Aqui no deberia entrar nunca)")

    return res.tolist()

def compon(ops, x):
    for op in reversed(ops):
        if callable(op):
            x = op(x)
        else:
            raise Exception(f"Operador no soportado en la composicion: {op}")
    return x



def main():
    if len(sys.argv) > 1: # Ejecutar desde archivo
        with open(sys.argv[1], 'r') as file:
            input_stream = InputStream(file.read())
    else: # Entrada interactiva
        input_stream = InputStream(input('? '))

    lexer = gLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = gParser(token_stream)
    tree = parser.root()

    # Uncomment to see the parse tree structure
    # print(tree.toStringTree(recog=parser))
    
    # Para evaluar el programa
    visitor = EvalVisitor()
    visitor.visit(tree)


if __name__ == "__main__":
    main()

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

    def visitArrel(self, ctx):
        # (statement? comment? '\n')* EOF
        children = list(ctx.getChildren())

        for child in children:
            if child.getText() != '<EOF>':
                res = self.visit(child)

                if isinstance(res, str):
                    print(res, '=:', end=' ')
                    for r in self.variables[res]:
                        if isinstance(r, int) and r < 0:
                            print("_" + str(abs(r)), end=' ')
                        else: 
                            print(r, end=' ')

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

        # Comprobar length error
        if len(res1) != len(res2) and len(res1) != 1 and len(res2) != 1 and op != ',' and op != '{':
            raise Exception("Las listas deben tener la misma longitud o una de ellas debe tener un solo elemento.")

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

        if len(res1) != len(res2) and len(res1) != 1 and len(res2) != 1 and op != ',' and op != '{':
            raise Exception("Las listas deben tener la misma longitud o una de ellas debe tener un solo elemento.")
    
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
            return [reduce(lambda acc,y: realizar_operacion(op, acc, y), exp)]

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

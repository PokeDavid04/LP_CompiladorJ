from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from gVisitor import gVisitor
import numpy as np
import sys


class EvalVisitor(gVisitor):
    def __init__(self):
        self.variables = {}

    def visitArrel(self, ctx):
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
        [variable, _, expresion] = list(ctx.getChildren())
        var_name = variable.getText()
        value = self.visit(expresion)
        
        self.variables[var_name] = value
        return var_name
    
    def visitExpresion(self, ctx):
        [expresion] = list(ctx.getChildren())
        return self.visit(expresion)

    def visitParentesis(self, ctx):
        [_, expressio, _] = list(ctx.getChildren())
        return self.visit(expressio)
    
    def visitOperacion(self, ctx):
        [op1, operacion, op2] = list(ctx.getChildren())
        res1 = self.visit(op1)
        res2 = self.visit(op2)
        op = operacion.getText()

        # Comprobar length error
        if len(res1) != len(res2) and len(res1) != 1 and len(res2) != 1:
            raise Exception("Las listas deben tener la misma longitud o una de ellas debe tener un solo elemento.")

        arr1 = np.array(res1)
        arr2 = np.array(res2)

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
        else:
            raise Exception(f"Operador no soportado: {op} (Aqui no deberia entrar nunca)")

        return res.tolist()

    def visitOperando(self, ctx):
        children = list(ctx.getChildren())
        return [self.visit(child) for child in children]
    
    def visitVariable(self, ctx):
        [variable] = list(ctx.getChildren())
        var_name = variable.getText()
        
        if var_name not in self.variables:
            raise Exception(f"Variable '{var_name}' no definida.")
        
        return self.variables[var_name]

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())
    
    def visitNumero_negativo(self, ctx):
        [negnum] = list(ctx.getChildren())
        text = negnum.getText()
        numero = text[1:]
        return -int(numero)

    def visitComentario(self, ctx):
        return None


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

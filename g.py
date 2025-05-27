from antlr4 import *
from gLexer import gLexer
from gParser import gParser
from gVisitor import gVisitor
from functools import reduce
import numpy as np
import sys
from funcionsAux import realizar_operacion

class EvalVisitor(gVisitor):
    def __init__(self):
        self.variables = {}

    def visitArrel(self, ctx):
        # (statement? comment? '\n')* EOF
        children = list(ctx.getChildren())

        for child in children:
            if child.getText() != '<EOF>':
                # print('Vissiting:', child.getText())
                try:
                    res = self.visit(child)
                except Exception as e:
                    print(f"Error: {e}")
                    break

                if isinstance(res, str):
                    if res in self.variables:
                        print(res, '=: <asignada>', end=' ')

                elif isinstance(res, list):
                    for element in res:
                        if isinstance(element, int) and element < 0:
                            print("_" + str(abs(element)), end=' ')
                        else:
                            print(element, end=' ')
                
                elif callable(res):
                    print(f"Una funcion no puede ser una expresion independiente.")

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
        op = self.visit(operacion)
        
        res1 = self.visit(expr1)
        if not isinstance(res1, list): 
            raise Exception(f'El primer operando debe ser una lista, pero se obtuvo: {type(res1)}')

        if expr2.getText()  == ']':
            return lambda x: realizar_operacion(op, res1, x)
        
        res2 = self.visit(expr2)
        if not isinstance(res2, list):
            raise Exception(f'El segundo operando debe ser una lista, pero se obtuvo: {type(res2)}')
        
        return realizar_operacion(op, res1, res2)

    def visitOperacion_unaria(self, ctx):
        # operador_un expr
        [operador, expresion] = list(ctx.getChildren())
        exp = self.visit(expresion)
        if not isinstance(exp, list):
            raise Exception("El operando debe ser una lista.")
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
        if not isinstance(res1, list) or not isinstance(res2, list):
            raise Exception("Ambos operandos deben ser listas.")
        op = self.visit(operacion)
        mod_op = self.visit(mod)

        if mod_op == '~':
            return realizar_operacion(op, res2, res1)

    def visitOperacion_unaria_combinada(self, ctx):
        # operador_bin operador_un_comb expr
        [operacion, mod, expresion] = list(ctx.getChildren())
        exp = self.visit(expresion)
        if not isinstance(exp, list):
            raise Exception("El operando debe ser una lista.")
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
            
    def visitOperacion_binaria_filtro(self, ctx):
        # expr '#' expr
        [expr1, _, expr2] = list(ctx.getChildren())
        res1 = self.visit(expr1)
        res2 = self.visit(expr2)
        if not isinstance(res1, list): 
            raise Exception(f'El primer operando debe ser una lista, pero se obtuvo: {type(res1)}')
        if not isinstance(res2, list):
            raise Exception(f'El segundo operando debe ser una lista, pero se obtuvo: {type(res2)}')
        
        return realizar_operacion('#', res1, res2)

    def visitLlamada_funcion(self, ctx):
        # ID expr
        [name, expresion] = list(ctx.getChildren())
        fun_name = name.getText()
        if fun_name not in self.variables:
            raise Exception(f"Funcion '{fun_name}' no definida.")
        
        func = self.variables[fun_name]
        if not callable(func):
            raise Exception(f"'{fun_name}' no es una funcion.")
        
        expr = self.visit(expresion)
        if not isinstance(expr, list):
            raise Exception("El argumento de la funcion debe ser una numero o lista.")
        
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
            raise Exception(f"Variable o funcion '{var_name}' no definida.")
        
        return self.variables[var_name]
    
    def visitOperador_binario(self, ctx):
        # ('+'|'-'|'*'|'%'|'^'|'|'|'='|'<>'|'<'|'>'|'<='|'>='|','|'#'|'{')
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
        # funcion '@:' funcion
        [func1, _, func2] = list(ctx.getChildren())
        func1 = self.visit(func1)
        func2 = self.visit(func2)
        if not callable(func1) or not callable(func2):
            raise Exception("Ambas funciones deben ser llamadas.")
        return lambda x: func1(func2(x))

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

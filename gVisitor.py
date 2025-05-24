# Generated from g.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gParser import gParser
else:
    from gParser import gParser

# This class defines a complete generic visitor for a parse tree produced by gParser.

class gVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gParser#arrel.
    def visitArrel(self, ctx:gParser.ArrelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#asignacion.
    def visitAsignacion(self, ctx:gParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#expresion.
    def visitExpresion(self, ctx:gParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#parentesis.
    def visitParentesis(self, ctx:gParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#variable.
    def visitVariable(self, ctx:gParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operacion.
    def visitOperacion(self, ctx:gParser.OperacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operando.
    def visitOperando(self, ctx:gParser.OperandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#numero.
    def visitNumero(self, ctx:gParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#numero_negativo.
    def visitNumero_negativo(self, ctx:gParser.Numero_negativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#comentario.
    def visitComentario(self, ctx:gParser.ComentarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operador_binario.
    def visitOperador_binario(self, ctx:gParser.Operador_binarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operador_unario.
    def visitOperador_unario(self, ctx:gParser.Operador_unarioContext):
        return self.visitChildren(ctx)



del gParser
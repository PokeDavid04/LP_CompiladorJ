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


    # Visit a parse tree produced by gParser#asignacion_funcion.
    def visitAsignacion_funcion(self, ctx:gParser.Asignacion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#parentesis.
    def visitParentesis(self, ctx:gParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operacion_binaria.
    def visitOperacion_binaria(self, ctx:gParser.Operacion_binariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:gParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#variable.
    def visitVariable(self, ctx:gParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operando.
    def visitOperando(self, ctx:gParser.OperandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operacion_binaria_combinada.
    def visitOperacion_binaria_combinada(self, ctx:gParser.Operacion_binaria_combinadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operacion_unaria.
    def visitOperacion_unaria(self, ctx:gParser.Operacion_unariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operacion_unaria_combinada.
    def visitOperacion_unaria_combinada(self, ctx:gParser.Operacion_unaria_combinadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#f_comp.
    def visitF_comp(self, ctx:gParser.F_compContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#f_un.
    def visitF_un(self, ctx:gParser.F_unContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#f_bin.
    def visitF_bin(self, ctx:gParser.F_binContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#f_comb_un.
    def visitF_comb_un(self, ctx:gParser.F_comb_unContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operador_binario.
    def visitOperador_binario(self, ctx:gParser.Operador_binarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operador_unario.
    def visitOperador_unario(self, ctx:gParser.Operador_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operador_binario_combinacion.
    def visitOperador_binario_combinacion(self, ctx:gParser.Operador_binario_combinacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operador_unario_combinacion.
    def visitOperador_unario_combinacion(self, ctx:gParser.Operador_unario_combinacionContext):
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



del gParser
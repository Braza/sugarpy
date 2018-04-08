# Generated from SugarCubeParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SugarCubeParser import SugarCubeParser
else:
    from SugarCubeParser import SugarCubeParser

# This class defines a complete generic visitor for a parse tree produced by SugarCubeParser.

class SugarCubeParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SugarCubeParser#parse.
    def visitParse(self, ctx:SugarCubeParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#block.
    def visitBlock(self, ctx:SugarCubeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#statement.
    def visitStatement(self, ctx:SugarCubeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#assignment.
    def visitAssignment(self, ctx:SugarCubeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#if_stat.
    def visitIf_stat(self, ctx:SugarCubeParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#stat_block.
    def visitStat_block(self, ctx:SugarCubeParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#notExpr.
    def visitNotExpr(self, ctx:SugarCubeParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#funcExpr.
    def visitFuncExpr(self, ctx:SugarCubeParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:SugarCubeParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx:SugarCubeParser.MultiplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#atomExpr.
    def visitAtomExpr(self, ctx:SugarCubeParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#orExpr.
    def visitOrExpr(self, ctx:SugarCubeParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:SugarCubeParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#relationalExpr.
    def visitRelationalExpr(self, ctx:SugarCubeParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#equalityExpr.
    def visitEqualityExpr(self, ctx:SugarCubeParser.EqualityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#andExpr.
    def visitAndExpr(self, ctx:SugarCubeParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#parExpr.
    def visitParExpr(self, ctx:SugarCubeParser.ParExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#numberAtom.
    def visitNumberAtom(self, ctx:SugarCubeParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#booleanAtom.
    def visitBooleanAtom(self, ctx:SugarCubeParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#varAtom.
    def visitVarAtom(self, ctx:SugarCubeParser.VarAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#varNakedAtom.
    def visitVarNakedAtom(self, ctx:SugarCubeParser.VarNakedAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#stringAtom.
    def visitStringAtom(self, ctx:SugarCubeParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#nilAtom.
    def visitNilAtom(self, ctx:SugarCubeParser.NilAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#randomFunc.
    def visitRandomFunc(self, ctx:SugarCubeParser.RandomFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#arguments.
    def visitArguments(self, ctx:SugarCubeParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#text.
    def visitText(self, ctx:SugarCubeParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SugarCubeParser#log.
    def visitLog(self, ctx:SugarCubeParser.LogContext):
        return self.visitChildren(ctx)



del SugarCubeParser
# Generated from SugarCubeParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SugarCubeParser import SugarCubeParser
else:
    from SugarCubeParser import SugarCubeParser

# This class defines a complete listener for a parse tree produced by SugarCubeParser.
class SugarCubeParserListener(ParseTreeListener):

    # Enter a parse tree produced by SugarCubeParser#parse.
    def enterParse(self, ctx:SugarCubeParser.ParseContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#parse.
    def exitParse(self, ctx:SugarCubeParser.ParseContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#block.
    def enterBlock(self, ctx:SugarCubeParser.BlockContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#block.
    def exitBlock(self, ctx:SugarCubeParser.BlockContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#statement.
    def enterStatement(self, ctx:SugarCubeParser.StatementContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#statement.
    def exitStatement(self, ctx:SugarCubeParser.StatementContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#assignment.
    def enterAssignment(self, ctx:SugarCubeParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#assignment.
    def exitAssignment(self, ctx:SugarCubeParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#if_stat.
    def enterIf_stat(self, ctx:SugarCubeParser.If_statContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#if_stat.
    def exitIf_stat(self, ctx:SugarCubeParser.If_statContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#stat_block.
    def enterStat_block(self, ctx:SugarCubeParser.Stat_blockContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#stat_block.
    def exitStat_block(self, ctx:SugarCubeParser.Stat_blockContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#notExpr.
    def enterNotExpr(self, ctx:SugarCubeParser.NotExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#notExpr.
    def exitNotExpr(self, ctx:SugarCubeParser.NotExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#funcExpr.
    def enterFuncExpr(self, ctx:SugarCubeParser.FuncExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#funcExpr.
    def exitFuncExpr(self, ctx:SugarCubeParser.FuncExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:SugarCubeParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:SugarCubeParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:SugarCubeParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:SugarCubeParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#atomExpr.
    def enterAtomExpr(self, ctx:SugarCubeParser.AtomExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#atomExpr.
    def exitAtomExpr(self, ctx:SugarCubeParser.AtomExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#orExpr.
    def enterOrExpr(self, ctx:SugarCubeParser.OrExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#orExpr.
    def exitOrExpr(self, ctx:SugarCubeParser.OrExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:SugarCubeParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:SugarCubeParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#relationalExpr.
    def enterRelationalExpr(self, ctx:SugarCubeParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#relationalExpr.
    def exitRelationalExpr(self, ctx:SugarCubeParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#equalityExpr.
    def enterEqualityExpr(self, ctx:SugarCubeParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#equalityExpr.
    def exitEqualityExpr(self, ctx:SugarCubeParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#andExpr.
    def enterAndExpr(self, ctx:SugarCubeParser.AndExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#andExpr.
    def exitAndExpr(self, ctx:SugarCubeParser.AndExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#parExpr.
    def enterParExpr(self, ctx:SugarCubeParser.ParExprContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#parExpr.
    def exitParExpr(self, ctx:SugarCubeParser.ParExprContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#numberAtom.
    def enterNumberAtom(self, ctx:SugarCubeParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#numberAtom.
    def exitNumberAtom(self, ctx:SugarCubeParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#booleanAtom.
    def enterBooleanAtom(self, ctx:SugarCubeParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#booleanAtom.
    def exitBooleanAtom(self, ctx:SugarCubeParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#varAtom.
    def enterVarAtom(self, ctx:SugarCubeParser.VarAtomContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#varAtom.
    def exitVarAtom(self, ctx:SugarCubeParser.VarAtomContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#stringAtom.
    def enterStringAtom(self, ctx:SugarCubeParser.StringAtomContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#stringAtom.
    def exitStringAtom(self, ctx:SugarCubeParser.StringAtomContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#nilAtom.
    def enterNilAtom(self, ctx:SugarCubeParser.NilAtomContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#nilAtom.
    def exitNilAtom(self, ctx:SugarCubeParser.NilAtomContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#randomFunc.
    def enterRandomFunc(self, ctx:SugarCubeParser.RandomFuncContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#randomFunc.
    def exitRandomFunc(self, ctx:SugarCubeParser.RandomFuncContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#arguments.
    def enterArguments(self, ctx:SugarCubeParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#arguments.
    def exitArguments(self, ctx:SugarCubeParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#text.
    def enterText(self, ctx:SugarCubeParser.TextContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#text.
    def exitText(self, ctx:SugarCubeParser.TextContext):
        pass


    # Enter a parse tree produced by SugarCubeParser#log.
    def enterLog(self, ctx:SugarCubeParser.LogContext):
        pass

    # Exit a parse tree produced by SugarCubeParser#log.
    def exitLog(self, ctx:SugarCubeParser.LogContext):
        pass



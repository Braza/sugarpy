from sugarpy.SugarCubeParser import SugarCubeParser
from sugarpy.SugarCubeParserVisitor import SugarCubeParserVisitor
from random import randint


class SugarCubeVisitor(SugarCubeParserVisitor):

    def __init__(self, story_vars):
        super().__init__()
        self.story_vars = story_vars
        # self.result = []

    # Visit a parse tree produced by SugarCubeParser#parse.
    def visitParse(self, ctx: SugarCubeParser.ParseContext):
        result = ''
        n = ctx.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(ctx, result):
                return result

            c = ctx.getChild(i)
            child_result = c.accept(self)
            if child_result:
                result += child_result

        return result

    # Visit a parse tree produced by SugarCubeParser#block.
    def visitBlock(self, ctx: SugarCubeParser.BlockContext):
        result = ''
        n = ctx.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(ctx, result):
                return result

            c = ctx.getChild(i)
            child_result = c.accept(self)
            if child_result is not None:
                result += str(child_result)

        return result

    # Visit a parse tree produced by SugarCubeParser#assignment.
    def visitAssignment(self, ctx: SugarCubeParser.AssignmentContext):
        right = ctx.expr().accept(self)
        # print('Setting var: {} , value: {}; available vars: {}'.format(
        #    ctx.VAR().__str__(),
        #    right,
        #    self.story_vars))
        self.story_vars[ctx.VAR().__str__()] = right
        return None

    # Visit a parse tree produced by SugarCubeParser#if_stat.
    def visitIf_stat(self, ctx: SugarCubeParser.If_statContext):
        i = 0
        for condition, block in zip(ctx.condition(), ctx.block()):  # hoping that it will end at shortest list
            i += 1
            if self.visitChildren(condition):
                return self.visitChildren(block)
        if len(ctx.condition()) < len(ctx.block()):           # else block is present
            return self.visitChildren(ctx.block(i))
        return None

    # Visit a parse tree produced by SugarCubeParser#stat_block.
    def visitStat_block(self, ctx: SugarCubeParser.Stat_blockContext):
        return bool(self.visitChildren(ctx))

    # Visit a parse tree produced by SugarCubeParser#notExpr.
    def visitNotExpr(self, ctx: SugarCubeParser.NotExprContext):
        return ~self.visitChildren(ctx)

    # Visit a parse tree produced by SugarCubeParser#unaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx: SugarCubeParser.UnaryMinusExprContext):
        return -self.visitChildren(ctx)

    # Visit a parse tree produced by SugarCubeParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx: SugarCubeParser.MultiplicationExprContext):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        print('Mult-Div op: {} {} {}'.format(left, ctx.op.type, right))
        if ctx.op.type == SugarCubeParser.MULT:
            return left * right
        elif ctx.op.type == SugarCubeParser.DIV:
            return left / right
        elif ctx.op.type == SugarCubeParser.MOD:
            return left % right
        raise ValueError()

    # Visit a parse tree produced by SugarCubeParser#orExpr.
    def visitOrExpr(self, ctx: SugarCubeParser.OrExprContext):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        return left or right

    def visitRandomFunc(self, ctx: SugarCubeParser.RandomFuncContext):
        print(ctx.children)
        c = ctx.getChild(1)
        args = c.accept(self)
        return randint(*args)

    def visitArguments(self, ctx: SugarCubeParser.ArgumentsContext):
        print("visitng arguments")
        result = []
        n = ctx.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(ctx, result):
                return result

            c = ctx.getChild(i)
            child_result = c.accept(self)
            if child_result:
                result.append(child_result)

        return result

    def visitAdditiveExpr(self, ctx: SugarCubeParser.AdditiveExprContext):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        if ctx.op.type == SugarCubeParser.PLUS:
            return left + right
        elif ctx.op.type == SugarCubeParser.MINUS:
            return left - right
        raise ValueError()

    # Visit a parse tree produced by SugarCubeParser#relationalExpr.
    def visitRelationalExpr(self, ctx: SugarCubeParser.RelationalExprContext):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        if ctx.op.type == SugarCubeParser.GT:
            return left > right
        elif ctx.op.type == SugarCubeParser.LT:
            return left < right
        elif ctx.op.type == SugarCubeParser.GTEQ:
            return left >= right
        elif ctx.op.type == SugarCubeParser.LTEQ:
            return left <= right
        raise ValueError()

    # Visit a parse tree produced by SugarCubeParser#equalityExpr.
    def visitEqualityExpr(self, ctx: SugarCubeParser.EqualityExprContext):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        return (left == right) if ctx.op.type == SugarCubeParser.EQ else (left != right)

    # Visit a parse tree produced by SugarCubeParser#andExpr.
    def visitAndExpr(self, ctx: SugarCubeParser.AndExprContext):
        left = ctx.expr(0).accept(self)
        right = ctx.expr(1).accept(self)
        return left and right

    # Visit a parse tree produced by SugarCubeParser#numberAtom.
    def visitNumberAtom(self, ctx: SugarCubeParser.NumberAtomContext):
        x = ctx.getText()
        return float(x) if '.' in x else int(x)

    # Visit a parse tree produced by SugarCubeParser#booleanAtom.
    def visitBooleanAtom(self, ctx: SugarCubeParser.BooleanAtomContext):
        return ctx.getText() in ctx.TRUE()

    # Visit a parse tree produced by SugarCubeParser#varAtom.
    def visitVarAtom(self, ctx: SugarCubeParser.VarAtomContext):
        if ctx.getText() in self.story_vars.keys():
            print('Getting var: {} , value: {}; available vars: {}'.format(
                ctx.getText(),
                self.story_vars[ctx.getText()],
                self.story_vars))
            return self.story_vars[ctx.getText()]
        else:
            self.story_vars[ctx.getText()] = None
            print('Getting var: {}, but not found; available vars: {}'.format(
                ctx.getText(),
                self.story_vars))
            return self.story_vars[ctx.getText()]

    # Visit a parse tree produced by SugarCubeParser#stringAtom.
    def visitStringAtom(self, ctx: SugarCubeParser.StringAtomContext):
        return ctx.getText()

    # Visit a parse tree produced by SugarCubeParser#nilAtom.
    def visitNilAtom(self, ctx: SugarCubeParser.NilAtomContext):
        return None

    # Visit a parse tree produced by SugarCubeParser#text.
    def visitText(self, ctx: SugarCubeParser.TextContext):
        return ctx.getText()

    # Visit a parse tree produced by SugarCubeParser#log.
    def visitLog(self, ctx: SugarCubeParser.LogContext):
        print('SugarCubeParserVisitor found unedintefied token: {}'.format(ctx.getText()))

    def visitParExpr(self, ctx: SugarCubeParser.ParExprContext):
        return ctx.expr().accept(self)

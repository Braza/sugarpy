parser grammar SugarCubeParser;

options { tokenVocab=SugarCubeLexer; }

parse
 : block EOF
 ;

block
 : statement*
 ;

statement
 : assignment
 | if_stat
 | text
 | log
 | atom
 ;

assignment
 : OPENMACRO SET VAR ASSIGN expr CLOSEMACRO
 ;

if_stat
 : OPENMACRO IF condition CLOSEMACRO block (OPENMACRO ELSEIF condition CLOSEMACRO block)* (OPENMACRO ELSE CLOSEMACRO block)? OPENMACRO FI CLOSEMACRO
 ;

condition
 : expr #stat_block
 ;

expr
 : MINUS expr                           #unaryMinusExpr
 | NOT expr                             #notExpr
 | expr op=(MULT | DIV | MOD) expr      #multiplicationExpr
 | expr op=(PLUS | MINUS) expr          #additiveExpr
 | expr op=(LTEQ | GTEQ | LT | GT) expr #relationalExpr
 | expr op=(EQ | NEQ) expr              #equalityExpr
 | expr AND expr                        #andExpr
 | expr OR expr                         #orExpr
 | function                             #funcExpr
 | atom                                 #atomExpr
// expr POW<assoc=right> expr           #powExpr
 ;

atom
 : OPAR expr CPAR #parExpr
 | (INT | FLOAT)  #numberAtom
 | (TRUE | FALSE) #booleanAtom
 | VAR            #varAtom
 | NAKEDVAR       #varAtom
 | STRING         #stringAtom
 | NIL            #nilAtom
 ;

function
  : RANDOM arguments    #randomFunc
  ;

arguments : OPAR atom (COMMA atom)* CPAR;

text
 : TEXT
 ;

log
 : OTHER
 ;

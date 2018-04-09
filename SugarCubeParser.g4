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
 | var_atom
 | str_atom
 | link_macro
 | link
 ;

 link_macro
  : OPENMACRO BACK CLOSEMACRO                                                      #backLinkMacro
  | OPENMACRO RETURN CLOSEMACRO                                                    #returnLinkMacro
  | OPENMACRO ACTIONS ( var_atom | str_atom | link ) ( var_atom | str_atom | link )* CLOSEMACRO  #actionsLinkMacro
  | OPENMACRO CHOICE ( var_atom | str_atom | link ) ( var_atom | str_atom | link )? CLOSEMACRO   #choiceVarsMacro
  ;

  link
  : (OPENLINK | TAGOPENLINK) linktext (LINKDIV linktext)* CLOSELINK
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
 | var_atom                             #atomExpr
 | str_atom                             #atonExpr
// expr POW<assoc=right> expr           #powExpr
 ;

var_atom
 : VAR            #varAtom
 | NAKEDVAR       #varAtom
 ;

str_atom
 : STRING         #stringAtom
 ;

atom
 : OPAR expr CPAR #parExpr
 | (INT | FLOAT)  #numberAtom
 | (TRUE | FALSE) #booleanAtom
 | NIL            #nilAtom
 ;

function
  : RANDOM arguments    #randomFunc
  ;

arguments : OPAR atom (COMMA atom)* CPAR;

linktext
 : LINKTEXT
 ;

text
 : TEXT
 ;

log
 : OTHER
 ;

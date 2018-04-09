lexer grammar SugarCubeLexer;


TEXT
 : ( ~[<$[] | '<' ~'<' )+
 ;

NAKEDVAR : '$' ID;

OPENMACRO: '<<' -> pushMode(InTag);
OPENLINK : OPLINK -> pushMode(InLink);

fragment OPLINK : '[[';
fragment CLLINK : ']]';
fragment DIGIT : [0-9];
fragment ID : [a-zA-Z_] [a-zA-Z_0-9]*;

mode InLink;

    CLOSELINK : CLLINK -> popMode;

    LINKDIV : '|' ;

    LINKTEXT
    : ( ~[|\]] )+
    ;

    LINKVAR
    : '$' ID
    ;

mode InTag;

    CLOSEMACRO : '>>' -> popMode;

    RANDOM : 'random';
    BACK : 'back';
    RETURN : 'return';
    ACTIONS : 'actions';
    CHOICE : 'choice';

    TAGOPENLINK : OPLINK -> pushMode(InLink);

    VAR : '$' ID;
    OR : '||';
    AND : '&&';
    EQ : '==' | 'eq' | 'is';
    NEQ : '!=' | 'neq';
    GT : '>' | 'gt';
    LT : '<' | 'lt';
    GTEQ : '>=' | 'ge';
    LTEQ : '<='| 'le';
    PLUS : '+';
    MINUS : '-';
    MULT : '*';
    DIV : '/';
    MOD : '%';
    POW : '^';
    NOT : '!';

    SCOL : ';';
    ASSIGN : '=' | 'to';
    OPAR : '(';
    CPAR : ')';
    OBRACE : '{';
    CBRACE : '}';


    COMMA : ',';

    TRUE : 'true';
    FALSE : 'false';
    NIL : 'nil';
    IF : 'if';
    ELSEIF : 'elseif';
    FI : '/if';
    ELSE : 'else';
    //WHILE : 'while';
    //LOG : 'log';
    SET : 'set';

    INT
     : DIGIT+
     ;

    FLOAT
     : DIGIT+ '.' DIGIT*
     | '.' DIGIT+
     ;

    STRING
     : '"' (~["\r\n] | '""')* '"'
     ;



//    INNERTEXT
//     : (~["\r\n])+
//     ;

//COMMENT
// : '#' ~[\r\n]* -> skip
// ;

    SPACE
     : [ \t\r\n] -> skip
     ;


    OTHER
     : .
     ;
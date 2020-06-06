grammar Skyline;

root : expr EOF;

expr : variable | operation;

variable : VAR ':=' sky
         | VAR ':=' operation
         ;

sky : simple | compost | aleatori;

simple : '('NUM','NUM','NUM')';

compost : '['simple (','simple)*']';

aleatori : '{'NUM','NUM','NUM','NUM','NUM'}';

operation : '(' operation ')'
         | MENYS operation
         | operation MULT operation
         | operation MULT NUM
         | operation MES operation
         | operation MES NUM
         | operation MENYS NUM
         | VAR
         | sky
         ;


NUM : [0-9]+ ;
MES : '+';
MULT : '*';
MENYS: '-';
WS : [ \t\r\n]+ -> skip ;
VAR : ([a-z] | [A-Z]) + ([a-z] | [A-Z] | [0-9])*;
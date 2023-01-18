%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1 
%}

%token IF
%token ELIF
%token ELSE
%token WHILE
%token FOR
%token AND
%token OR
%token READ
%token SHOW
%token LIST

%token LEFT_ROUND_BRACKET
%token RIGHT_ROUND_BRACKET
%token LEFT_SQUARE_BRACKET
%token RIGHT_SQUARE_BRACKET
%token SEMICOLON
%token DOUBLECOLON
%token DOT
%token COMMA

%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token FLOOR_DIVISION
%token MOD
%token EQUAL
%token ASSIGNMENT
%token DIFFERENT
%token LESS
%token MORE
%token LESS_OR_EQUAL
%token MORE_OR_EQUAL

%token INTEGER
%token STRING
%token CHAR
%token IDENTIFIER

%start program

%%

program : stmtlist
stmtlist : stmt DOT stmtlist | stmt DOT
stmt : simplstmt | structstmt | declaration
declaration : IDENTIFIER DOUBLECOLON type
type : type1
type1 : CHAR | INTEGER | STRING
simplstmt : iostmt | assignstmt
assignstmt : IDENTIFIER ASSIGNMENT expression
expression : term math expression | term
math : PLUS | MINUS | MULTIPLY | DIVISION | FLOOR_DIVISION | MOD
term : IDENTIFIER | INTEGER | LEFT_ROUND_BRACKET expression RIGHT_ROUND_BRACKET | STRING
iostmt : READ LEFT_ROUND_BRACKET IDENTIFIER RIGHT_ROUND_BRACKET | SHOW LEFT_ROUND_BRACKET IDENTIFIER RIGHT_ROUND_BRACKET | SHOW LEFT_ROUND_BRACKET expression RIGHT_ROUND_BRACKET
structstmt : ifstmt | whilestmt | forstmt
ifstmt : IF LEFT_ROUND_BRACKET conditionlist RIGHT_ROUND_BRACKET DOUBLECOLON stmtlist ELSE DOUBLECOLON stmt DOT | IF LEFT_ROUND_BRACKET conditionlist RIGHT_ROUND_BRACKET DOUBLECOLON stmtlist ELIF LEFT_ROUND_BRACKET conditionlist RIGHT_ROUND_BRACKET DOUBLECOLON stmtlist ELSE DOUBLECOLON stmt
whilestmt : WHILE LEFT_ROUND_BRACKET conditionlist RIGHT_ROUND_BRACKET DOUBLECOLON stmtlist
forstmt : FOR LEFT_ROUND_BRACKET assignstmt COMMA condition COMMA assignstmt RIGHT_ROUND_BRACKET DOUBLECOLON stmtlist
conditionlist : condition operation condition | condition
condition : expression relation expression
relation : LESS | LESS_OR_EQUAL | EQUAL | DIFFERENT | MORE_OR_EQUAL | MORE
operation : AND | OR

%%

yyerror(char *s)
{	
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(argc>1) yyin :  fopen(argv[1],"r");
	if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
	if(!yyparse()) fprintf(stderr, "\tProgram is syntactically correct.\n");
}


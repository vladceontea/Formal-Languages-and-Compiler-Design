%{
	#include<stdio.h>
	#include <string.h>	
	#include "yacc_combined.tab.h"
	int currentLine = 1;
%}

%option noyywrap

LETTER [a-zA-Z]
DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
INTEGER 0|[+|-]?{NON_ZERO_DIGIT}{DIGIT}*
CHAR [\'][a-zA-Z0-9_][\']
STRING [\"][a-zA-Z0-9_]*[\"]
IDENTIFIER [a-zA-Z][a-zA-Z0-9_]*

%%

"if"		{printf("Reserved word: %s\n", yytext);return IF;}
"elif"		{printf("Reserved word: %s\n", yytext);return ELIF;}
"else"		{printf("Reserved word: %s\n", yytext);return ELSE;}
"while"		{printf("Reserved word: %s\n", yytext);return WHILE;}
"for"		{printf("Reserved word: %s\n", yytext);return FOR;}
"and" 		{printf("Reserved word: %s\n", yytext);return AND;}
"or" 		{printf("Reserved word: %s\n", yytext);return OR;}
"read" 		{printf("Reserved word: %s\n", yytext);return READ;}
"show" 		{printf("Reserved word: %s\n", yytext);return SHOW;}


"("		{printf("Separator: %s\n", yytext);return LEFT_ROUND_BRACKET;}
")"		{printf("Separator: %s\n", yytext);return RIGHT_ROUND_BRACKET;}
"["		{printf("Separator: %s\n", yytext);return LEFT_SQUARE_BRACKET;}
"]"		{printf("Separator: %s\n", yytext);return RIGHT_SQUARE_BRACKET;}
";"		{printf("Separator: %s\n", yytext);return SEMICOLON;}
":"		{printf("Separator: %s\n", yytext);return DOUBLECOLON;}
"."		{printf("Separator: %s\n", yytext);return DOT;}
","		{printf("Separator: %s\n", yytext);return COMMA;}

"+"		{printf("Operator: %s\n", yytext);return PLUS;}
"-"		{printf("Operator: %s\n", yytext);return MINUS;}
"*"		{printf("Operator: %s\n", yytext);return MULTIPLY;}
"/"		{printf("Operator: %s\n", yytext);return DIVISION;}
"//"		{printf("Operator: %s\n", yytext);return FLOOR_DIVISION;}
"%"		{printf("Operator: %s\n", yytext);return MOD;}
"="		{printf("Operator: %s\n", yytext);return EQUAL;}
"<-"		{printf("Operator: %s\n", yytext);return ASSIGNMENT;}
"<>"		{printf("Operator: %s\n", yytext);return DIFFERENT;}
"<"		{printf("Operator: %s\n", yytext);return LESS;}
">"		{printf("Operator: %s\n", yytext);return MORE;}
"<="		{printf("Operator: %s\n", yytext);return LESS_OR_EQUAL;}
">="		{printf("Operator: %s\n", yytext);return MORE_OR_EQUAL;}

{INTEGER}	{printf("Number: %s\n", yytext);return INTEGER;}
{STRING}	{printf("String: %s\n", yytext);return STRING;}
{CHAR}		{printf("Character: %s\n", yytext);return CHAR;}
{IDENTIFIER}		{printf("Identifier: %s\n", yytext);return IDENTIFIER;}


[ \t]+  	{}
[\n]+ 		{currentLine++;}

[0-9_][a-zA-Z0-9_]*	{printf("Illegal identifier at line %d\n", currentLine); return -1;}
[+|-]0			{printf("Illegal numeric constant at line %d\n", currentLine); return -1;}
.	{printf("Illegal symbol at line %d\n", currentLine); return -1;}

%%

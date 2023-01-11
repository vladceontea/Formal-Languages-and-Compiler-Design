%{
	#include<stdio.h>
	#include <string.h>
%}

%option noyywrap

LETTER [a-ZA-Z]
DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
INTEGER 0|[+|-]?{NON_ZERO_DIGIT}{DIGIT}*
CHAR [\'][a-zA-Z0-9_][\']
STRING [\"][a-zA-Z0-9_]*[\"]
IDENTIFIER [a-zA-Z][a-zA-Z0-9_]*

%%

"if"		{printf("Reserved word: %s\n", yytext);}
"elif"		{printf("Reserved word: %s\n", yytext);}
"else"		{printf("Reserved word: %s\n", yytext);}
"while"		{printf("Reserved word: %s\n", yytext);}
"for"		{printf("Reserved word: %s\n", yytext);}
"and" 		{printf("Reserved word: %s\n", yytext);}
"or" 		{printf("Reserved word: %s\n", yytext);}
"read" 		{printf("Reserved word: %s\n", yytext);}
"show" 		{printf("Reserved word: %s\n", yytext);}
"int" 		{printf("Reserved word: %s\n", yytext);}
"char" 		{printf("Reserved word: %s\n", yytext);}
"string"	{printf("Reserved word: %s\n", yytext);}
"list" 		{printf("Reserved word: %s\n", yytext);}


"("		{printf("Separator: %s\n", yytext);}
")"		{printf("Separator: %s\n", yytext);}
";"		{printf("Separator: %s\n", yytext);}
":"		{printf("Separator: %s\n", yytext);}
"."		{printf("Separator: %s\n", yytext);}
","		{printf("Separator: %s\n", yytext);}

"+"		{printf("Operator: %s\n", yytext);}
"-"		{printf("Operator: %s\n", yytext);}
"*"		{printf("Operator: %s\n", yytext);}
"/"		{printf("Operator: %s\n", yytext);}
"//"		{printf("Operator: %s\n", yytext);}
"%"		{printf("Operator: %s\n", yytext);}
"="		{printf("Operator: %s\n", yytext);}
"<-"		{printf("Operator: %s\n", yytext);}
"!="		{printf("Operator: %s\n", yytext);}
"<"		{printf("Operator: %s\n", yytext);}
">"		{printf("Operator: %s\n", yytext);}
"<="		{printf("Operator: %s\n", yytext);}
">="		{printf("Operator: %s\n", yytext);}

{INTEGER}	{printf("Number: %s\n", yytext);}
{STRING}	{printf("String: %s\n", yytext);}
{CHAR}		{printf("Character: %s\n", yytext);}
{IDENTIFIER}		{printf("Identifier: %s\n", yytext);}

%%
void main(argc, argv)
int argc;
char** argv;
{           
if (argc > 1)
{
    FILE *file;
    file = fopen(argv[1], "r");
    if (!file)
    {
        fprintf(stderr, "Could not open %s\n", argv[1]);
        exit(1);
    }
    yyin = file;
}

yylex();
}
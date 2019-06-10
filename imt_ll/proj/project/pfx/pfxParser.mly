%{
  open PfxAst

  (* Ocaml code here*)

%}

(**************
 * The tokens *
 **************)

(* enter tokens here, they should begin with %token *)
%token EOF PLUS MINUS TIMES DIV MOD PUSH POP
%token <int> INT


(******************************
 * Entry points of the parser *
 ******************************)

(* enter your %start clause here *)
%start <PfxAst.program> program (* Program is a tuple (int, command) *)
(* Extract: type program = int * command list *)

%%

(*************
 * The rules *
 *************)

(* list all rules composing your grammar; obviously your entry point has to be present *)

(*program: i=INT EOF { i,[] }*)
program: a=args t=tot EOF { a, t }

args:
| i=INT { i }

tot:
| t=tot q=command { t@[q] }
| q=command { [q] }

command:
| q=instruction { q }
| v=value { v }

value:
| PUSH c=INT { Push c }

instruction:
| MINUS   { Sub }
| PLUS    { Add }
| TIMES   { Mul }
| DIV     { Div }
| MOD     { Rem }
| POP     { Pop }

%%

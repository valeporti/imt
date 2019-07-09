%{
  open PfxAst

  (* Ocaml code here*)

%}

(**************
 * The tokens *
 **************)

(* enter tokens here, they should begin with %token *)
%token EOF PLUS MINUS TIMES DIV MOD PUSH POP
%token EXEC GET LBRA RBRA
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
program: i=args q=instructions EOF { i, q }

args:
| i=INT { i }

instructions:
| t=instructions q=command { t@[q] }
| q=command { [q] }

command:
| q=base { q }
| v=value { v }
| LBRA s=instructions RBRA { Q s }

value:
| PUSH c=INT { Push c }

base:
| MINUS   { Sub }
| PLUS    { Add }
| TIMES   { Mul }
| DIV     { Div }
| MOD     { Rem }
| POP     { Pop }
| EXEC    { Exec }
| GET     { Get }

%%

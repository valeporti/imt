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

program: i=INT EOF { i,[] }

prev:
| PUSH c=INT command
| 

(* Commands *)
command:
| MINUS { Sub }
| PLUS { Add }
| TIMES  { Mul }
| DIV { Div }
| MOD { Mod }
| PUSH c=INT { Push c } (* we know it comes as an int *)
| POP { Pop }

%%

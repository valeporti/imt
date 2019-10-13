
(* The type of tokens. *)

type token = 
  | TIMES
  | RPAR
  | RA
  | PLUS
  | MOD
  | MINUS
  | LPAR
  | LET
  | INT of (int)
  | IN
  | IDENT of (string)
  | FUN
  | EOF
  | DIV
  | ASSIGN

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val expression: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> ( ExprAst.expression )

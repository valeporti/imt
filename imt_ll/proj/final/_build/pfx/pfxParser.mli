
(* The type of tokens. *)

type token = 
  | TIMES
  | SWAP
  | SEQ
  | PUSH
  | POP
  | PLUS
  | MOD
  | MINUS
  | INT of (int)
  | GET
  | EXEC
  | EOF
  | DIV

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val program: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (PfxAst.program)

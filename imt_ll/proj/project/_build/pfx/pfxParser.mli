
(* The type of tokens. *)

type token = 
  | Psub
  | Ppush
  | Pmul
  | Pmod
  | Pdiv
  | Padd
  | INT of (int)
  | EOF

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val program: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (PfxAst.program)

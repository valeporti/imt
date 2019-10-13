# 1 "pfx/pfxLexerTest.mll"
 
  type token =
    | EOF | PLUS | MINUS | TIMES | DIV | MOD | PUSH | POP | SWAP
    | INT of int | IDENT of string

  let mk_int nb loc =
    try INT (int_of_string nb)
    with Failure _ -> raise (Location.Error(Printf.sprintf "Illegal integer '%s': " nb,loc))

# 12 "pfx/pfxLexerTest.ml"
let __ocaml_lex_tables = {
  Lexing.lex_base =
   "\000\000\242\255\000\000\000\000\001\000\002\000\000\000\036\000\
    \001\000\253\255\006\000\255\255\001\000\006\000\001\000\250\255\
    \000\000\000\000\249\255\001\000\243\255\002\000\000\000\248\255\
    \246\255\002\000\247\255\002\000\000\000\000\000\245\255\244\255\
    ";
  Lexing.lex_backtrk =
   "\255\255\255\255\013\000\013\000\013\000\013\000\013\000\004\000\
    \013\000\255\255\001\000\255\255\000\000\003\000\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    ";
  Lexing.lex_default =
   "\001\000\000\000\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\000\000\255\255\000\000\255\255\013\000\255\255\000\000\
    \255\255\255\255\000\000\255\255\000\000\255\255\255\255\000\000\
    \000\000\255\255\000\000\255\255\255\255\255\255\000\000\000\000\
    ";
  Lexing.lex_trans =
   "\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\010\000\011\000\011\000\010\000\012\000\010\000\010\000\
    \255\255\000\000\010\000\255\255\010\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \010\000\000\000\000\000\000\000\000\000\000\000\010\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\008\000\013\000\000\000\
    \007\000\007\000\007\000\007\000\007\000\007\000\007\000\007\000\
    \007\000\007\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\006\000\000\000\000\000\003\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\004\000\000\000\000\000\
    \002\000\000\000\000\000\005\000\007\000\007\000\007\000\007\000\
    \007\000\007\000\007\000\007\000\007\000\007\000\000\000\000\000\
    \000\000\019\000\018\000\000\000\014\000\015\000\024\000\000\000\
    \030\000\025\000\000\000\000\000\023\000\000\000\000\000\027\000\
    \021\000\020\000\031\000\029\000\000\000\028\000\022\000\017\000\
    \026\000\016\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \009\000\000\000\000\000\000\000\000\000\000\000\255\255\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\000\000\000\000\000\000";
  Lexing.lex_check =
   "\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\000\000\000\000\012\000\000\000\000\000\000\000\010\000\
    \013\000\255\255\010\000\013\000\010\000\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \000\000\255\255\255\255\255\255\255\255\255\255\010\000\255\255\
    \255\255\255\255\255\255\255\255\255\255\000\000\008\000\255\255\
    \000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\
    \000\000\000\000\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\000\000\255\255\255\255\000\000\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\000\000\255\255\255\255\
    \000\000\255\255\255\255\000\000\007\000\007\000\007\000\007\000\
    \007\000\007\000\007\000\007\000\007\000\007\000\255\255\255\255\
    \255\255\016\000\017\000\255\255\006\000\014\000\021\000\255\255\
    \029\000\003\000\255\255\255\255\022\000\255\255\255\255\002\000\
    \004\000\019\000\027\000\028\000\255\255\002\000\004\000\005\000\
    \025\000\005\000\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \000\000\255\255\255\255\255\255\255\255\255\255\013\000\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\255\
    \255\255\255\255\255\255\255\255\255\255";
  Lexing.lex_base_code =
   "";
  Lexing.lex_backtrk_code =
   "";
  Lexing.lex_default_code =
   "";
  Lexing.lex_trans_code =
   "";
  Lexing.lex_check_code =
   "";
  Lexing.lex_code =
   "";
}

let rec token lexbuf =
   __ocaml_lex_token_rec lexbuf 0
and __ocaml_lex_token_rec lexbuf __ocaml_lex_state =
  match Lexing.engine __ocaml_lex_tables __ocaml_lex_state lexbuf with
      | 0 ->
# 19 "pfx/pfxLexerTest.mll"
            ( Location.incr_line lexbuf; token lexbuf )
# 129 "pfx/pfxLexerTest.ml"

  | 1 ->
# 21 "pfx/pfxLexerTest.mll"
            ( token lexbuf )
# 134 "pfx/pfxLexerTest.ml"

  | 2 ->
# 23 "pfx/pfxLexerTest.mll"
             ( EOF )
# 139 "pfx/pfxLexerTest.ml"

  | 3 ->
# 25 "pfx/pfxLexerTest.mll"
                            ( token lexbuf )
# 144 "pfx/pfxLexerTest.ml"

  | 4 ->
let
# 27 "pfx/pfxLexerTest.mll"
               nb
# 150 "pfx/pfxLexerTest.ml"
= Lexing.sub_lexeme lexbuf lexbuf.Lexing.lex_start_pos lexbuf.Lexing.lex_curr_pos in
# 27 "pfx/pfxLexerTest.mll"
                            ( mk_int nb (Location.curr lexbuf))
# 154 "pfx/pfxLexerTest.ml"

  | 5 ->
# 30 "pfx/pfxLexerTest.mll"
            ( PLUS )
# 159 "pfx/pfxLexerTest.ml"

  | 6 ->
# 31 "pfx/pfxLexerTest.mll"
            ( MINUS )
# 164 "pfx/pfxLexerTest.ml"

  | 7 ->
# 32 "pfx/pfxLexerTest.mll"
            ( TIMES )
# 169 "pfx/pfxLexerTest.ml"

  | 8 ->
# 33 "pfx/pfxLexerTest.mll"
            ( DIV )
# 174 "pfx/pfxLexerTest.ml"

  | 9 ->
# 34 "pfx/pfxLexerTest.mll"
            ( MOD )
# 179 "pfx/pfxLexerTest.ml"

  | 10 ->
# 35 "pfx/pfxLexerTest.mll"
            ( PUSH )
# 184 "pfx/pfxLexerTest.ml"

  | 11 ->
# 36 "pfx/pfxLexerTest.mll"
            ( POP )
# 189 "pfx/pfxLexerTest.ml"

  | 12 ->
# 37 "pfx/pfxLexerTest.mll"
            ( SWAP )
# 194 "pfx/pfxLexerTest.ml"

  | 13 ->
let
# 39 "pfx/pfxLexerTest.mll"
         c
# 200 "pfx/pfxLexerTest.ml"
= Lexing.sub_lexeme_char lexbuf lexbuf.Lexing.lex_start_pos in
# 39 "pfx/pfxLexerTest.mll"
            (
      raise (Location.Error(Printf.sprintf "Illegal character '%c': " c, Location.curr lexbuf))
    )
# 206 "pfx/pfxLexerTest.ml"

  | __ocaml_lex_state -> lexbuf.Lexing.refill_buff lexbuf;
      __ocaml_lex_token_rec lexbuf __ocaml_lex_state

;;



module MenhirBasics = struct
  
  exception Error
  
  type token = 
    | INT of (
# 14 "pfx/pfxParser.mly"
       (int)
# 11 "pfx/pfxParser.ml"
  )
    | EOF
  
end

include MenhirBasics

let _eRR =
  MenhirBasics.Error

type _menhir_env = {
  _menhir_lexer: Lexing.lexbuf -> token;
  _menhir_lexbuf: Lexing.lexbuf;
  _menhir_token: token;
  mutable _menhir_error: bool
}

and _menhir_state

# 1 "pfx/pfxParser.mly"
  
  open PfxAst

  (* Ocaml code here*)


# 38 "pfx/pfxParser.ml"

let rec _menhir_discard : _menhir_env -> _menhir_env =
  fun _menhir_env ->
    let lexer = _menhir_env._menhir_lexer in
    let lexbuf = _menhir_env._menhir_lexbuf in
    let _tok = lexer lexbuf in
    {
      _menhir_lexer = lexer;
      _menhir_lexbuf = lexbuf;
      _menhir_token = _tok;
      _menhir_error = false;
    }

and program : (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (
# 22 "pfx/pfxParser.mly"
       (PfxAst.program)
# 55 "pfx/pfxParser.ml"
) =
  fun lexer lexbuf ->
    let _menhir_env = let _tok = Obj.magic () in
    {
      _menhir_lexer = lexer;
      _menhir_lexbuf = lexbuf;
      _menhir_token = _tok;
      _menhir_error = false;
    } in
    Obj.magic (let _menhir_stack = ((), _menhir_env._menhir_lexbuf.Lexing.lex_curr_p) in
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | INT _v ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = (_menhir_stack, _v) in
        let _menhir_env = _menhir_discard _menhir_env in
        let _tok = _menhir_env._menhir_token in
        (match _tok with
        | EOF ->
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_menhir_stack, (i : (
# 14 "pfx/pfxParser.mly"
       (int)
# 81 "pfx/pfxParser.ml"
            ))) = _menhir_stack in
            let _2 = () in
            let _v : (
# 22 "pfx/pfxParser.mly"
       (PfxAst.program)
# 87 "pfx/pfxParser.ml"
            ) = 
# 32 "pfx/pfxParser.mly"
                   ( i,[] )
# 91 "pfx/pfxParser.ml"
             in
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_1 : (
# 22 "pfx/pfxParser.mly"
       (PfxAst.program)
# 98 "pfx/pfxParser.ml"
            )) = _v in
            Obj.magic _1
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            let _menhir_stack = Obj.magic _menhir_stack in
            raise _eRR)
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        let _menhir_stack = Obj.magic _menhir_stack in
        raise _eRR)

# 34 "pfx/pfxParser.mly"
  

# 115 "pfx/pfxParser.ml"

# 233 "/home/valeporti/.opam/system/lib/menhir/standard.mly"
  

# 120 "pfx/pfxParser.ml"

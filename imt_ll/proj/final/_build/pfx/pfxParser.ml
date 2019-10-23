
module MenhirBasics = struct
  
  exception Error
  
  type token = 
    | TIMES
    | SWAP
    | SEQ
    | PUSH
    | POP
    | PLUS
    | MOD
    | MINUS
    | INT of (
# 15 "pfx/pfxParser.mly"
       (int)
# 19 "pfx/pfxParser.ml"
  )
    | GET
    | EXEC
    | EOF
    | DIV
  
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

and _menhir_state = 
  | MenhirState21
  | MenhirState16
  | MenhirState6
  | MenhirState3

# 1 "pfx/pfxParser.mly"
  
  open PfxAst

  (* Ocaml code here*)


# 53 "pfx/pfxParser.ml"

let rec _menhir_goto_instructions : _menhir_env -> 'ttv_tail -> _menhir_state -> (PfxAst.command list) -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s _v ->
    let _menhir_stack = (_menhir_stack, _menhir_s, _v) in
    match _menhir_s with
    | MenhirState6 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        assert (not _menhir_env._menhir_error);
        let _tok = _menhir_env._menhir_token in
        (match _tok with
        | DIV ->
            _menhir_run14 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | EXEC ->
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_s = MenhirState16 in
            let _menhir_env = _menhir_discard _menhir_env in
            let _menhir_stack = Obj.magic _menhir_stack in
            let ((_menhir_stack, _menhir_s), _, (s : (PfxAst.command list))) = _menhir_stack in
            let _3 = () in
            let _1 = () in
            let _v : (PfxAst.command list) = 
# 45 "pfx/pfxParser.mly"
                          ( [Q s]@[Exec] )
# 77 "pfx/pfxParser.ml"
             in
            _menhir_goto_command _menhir_env _menhir_stack _menhir_s _v
        | GET ->
            _menhir_run13 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | MINUS ->
            _menhir_run12 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | MOD ->
            _menhir_run11 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | PLUS ->
            _menhir_run10 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | POP ->
            _menhir_run9 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | PUSH ->
            _menhir_run7 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | SEQ ->
            _menhir_run6 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | SWAP ->
            _menhir_run5 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | TIMES ->
            _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState16
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState16)
    | MenhirState3 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        assert (not _menhir_env._menhir_error);
        let _tok = _menhir_env._menhir_token in
        (match _tok with
        | DIV ->
            _menhir_run14 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | EOF ->
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_s = MenhirState21 in
            let _menhir_stack = Obj.magic _menhir_stack in
            let ((_menhir_stack, (i : (int))), _, (q : (PfxAst.command list))) = _menhir_stack in
            let _3 = () in
            let _v : (
# 23 "pfx/pfxParser.mly"
       (PfxAst.program)
# 118 "pfx/pfxParser.ml"
            ) = 
# 33 "pfx/pfxParser.mly"
                                   ( i, q )
# 122 "pfx/pfxParser.ml"
             in
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_1 : (
# 23 "pfx/pfxParser.mly"
       (PfxAst.program)
# 129 "pfx/pfxParser.ml"
            )) = _v in
            Obj.magic _1
        | GET ->
            _menhir_run13 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | MINUS ->
            _menhir_run12 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | MOD ->
            _menhir_run11 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | PLUS ->
            _menhir_run10 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | POP ->
            _menhir_run9 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | PUSH ->
            _menhir_run7 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | SEQ ->
            _menhir_run6 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | SWAP ->
            _menhir_run5 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | TIMES ->
            _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState21
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState21)
    | _ ->
        ();
        Printf.fprintf Pervasives.stderr "Internal failure -- please contact the parser generator's developers.\n%!";
        assert false

and _menhir_goto_command : _menhir_env -> 'ttv_tail -> _menhir_state -> (PfxAst.command list) -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s _v ->
    match _menhir_s with
    | MenhirState21 | MenhirState16 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = Obj.magic _menhir_stack in
        let (q : (PfxAst.command list)) = _v in
        let (_menhir_stack, _menhir_s, (t : (PfxAst.command list))) = _menhir_stack in
        let _v : (PfxAst.command list) = 
# 39 "pfx/pfxParser.mly"
                            ( t@q )
# 170 "pfx/pfxParser.ml"
         in
        _menhir_goto_instructions _menhir_env _menhir_stack _menhir_s _v
    | MenhirState3 | MenhirState6 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = Obj.magic _menhir_stack in
        let (q : (PfxAst.command list)) = _v in
        let _v : (PfxAst.command list) = 
# 40 "pfx/pfxParser.mly"
                            ( q )
# 180 "pfx/pfxParser.ml"
         in
        _menhir_goto_instructions _menhir_env _menhir_stack _menhir_s _v

and _menhir_goto_base : _menhir_env -> 'ttv_tail -> _menhir_state -> (PfxAst.command) -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s _v ->
    let _menhir_stack = Obj.magic _menhir_stack in
    let _menhir_stack = Obj.magic _menhir_stack in
    let (q : (PfxAst.command)) = _v in
    let _v : (PfxAst.command list) = 
# 43 "pfx/pfxParser.mly"
                          ( [q] )
# 192 "pfx/pfxParser.ml"
     in
    _menhir_goto_command _menhir_env _menhir_stack _menhir_s _v

and _menhir_errorcase : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    match _menhir_s with
    | MenhirState21 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s, _) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState16 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s, _) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState6 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState3 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        raise _eRR

and _menhir_run4 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 53 "pfx/pfxParser.mly"
          ( Mul )
# 223 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_run5 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 58 "pfx/pfxParser.mly"
          ( Swap )
# 235 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_run6 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_stack = (_menhir_stack, _menhir_s) in
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | DIV ->
        _menhir_run14 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | GET ->
        _menhir_run13 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | MINUS ->
        _menhir_run12 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | MOD ->
        _menhir_run11 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | PLUS ->
        _menhir_run10 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | POP ->
        _menhir_run9 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | PUSH ->
        _menhir_run7 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | SEQ ->
        _menhir_run6 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | SWAP ->
        _menhir_run5 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | TIMES ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState6
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState6

and _menhir_run7 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_stack = (_menhir_stack, _menhir_s) in
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | INT _v ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_env = _menhir_discard _menhir_env in
        let _menhir_stack = Obj.magic _menhir_stack in
        let (c : (
# 15 "pfx/pfxParser.mly"
       (int)
# 283 "pfx/pfxParser.ml"
        )) = _v in
        let (_menhir_stack, _menhir_s) = _menhir_stack in
        let _1 = () in
        let _v : (PfxAst.command) = 
# 48 "pfx/pfxParser.mly"
             ( Push c )
# 290 "pfx/pfxParser.ml"
         in
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = Obj.magic _menhir_stack in
        let (v : (PfxAst.command)) = _v in
        let _v : (PfxAst.command list) = 
# 44 "pfx/pfxParser.mly"
                          ( [v] )
# 298 "pfx/pfxParser.ml"
         in
        _menhir_goto_command _menhir_env _menhir_stack _menhir_s _v
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s

and _menhir_run9 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 56 "pfx/pfxParser.mly"
          ( Pop )
# 316 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_run10 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 52 "pfx/pfxParser.mly"
          ( Add )
# 328 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_run11 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 55 "pfx/pfxParser.mly"
          ( Rem )
# 340 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_run12 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 51 "pfx/pfxParser.mly"
          ( Sub )
# 352 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_run13 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 57 "pfx/pfxParser.mly"
          ( Get )
# 364 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_run14 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let _1 = () in
    let _v : (PfxAst.command) = 
# 54 "pfx/pfxParser.mly"
          ( Div )
# 376 "pfx/pfxParser.ml"
     in
    _menhir_goto_base _menhir_env _menhir_stack _menhir_s _v

and _menhir_discard : _menhir_env -> _menhir_env =
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
# 23 "pfx/pfxParser.mly"
       (PfxAst.program)
# 395 "pfx/pfxParser.ml"
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
        let _menhir_env = _menhir_discard _menhir_env in
        let _menhir_stack = Obj.magic _menhir_stack in
        let (i : (
# 15 "pfx/pfxParser.mly"
       (int)
# 416 "pfx/pfxParser.ml"
        )) = _v in
        let _v : (int) = 
# 36 "pfx/pfxParser.mly"
          ( i )
# 421 "pfx/pfxParser.ml"
         in
        let _menhir_stack = (_menhir_stack, _v) in
        let _menhir_stack = Obj.magic _menhir_stack in
        assert (not _menhir_env._menhir_error);
        let _tok = _menhir_env._menhir_token in
        (match _tok with
        | DIV ->
            _menhir_run14 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | GET ->
            _menhir_run13 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | MINUS ->
            _menhir_run12 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | MOD ->
            _menhir_run11 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | PLUS ->
            _menhir_run10 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | POP ->
            _menhir_run9 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | PUSH ->
            _menhir_run7 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | SEQ ->
            _menhir_run6 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | SWAP ->
            _menhir_run5 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | TIMES ->
            _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState3
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState3)
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        let _menhir_stack = Obj.magic _menhir_stack in
        raise _eRR)

# 60 "pfx/pfxParser.mly"
  

# 461 "pfx/pfxParser.ml"

# 233 "/home/valeporti/.opam/system/lib/menhir/standard.mly"
  

# 466 "pfx/pfxParser.ml"

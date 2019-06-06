
module MenhirBasics = struct
  
  exception Error
  
  type token = 
    | TIMES
    | RPAR
    | PLUS
    | MOD
    | MINUS
    | LPAR
    | INT of (
# 7 "expr/exprParser.mly"
       (int)
# 17 "expr/exprParser.ml"
  )
    | IDENT of (
# 8 "expr/exprParser.mly"
       (string)
# 22 "expr/exprParser.ml"
  )
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
  | MenhirState16
  | MenhirState14
  | MenhirState12
  | MenhirState10
  | MenhirState7
  | MenhirState2
  | MenhirState1
  | MenhirState0

# 1 "expr/exprParser.mly"
  
  open ExprAst
  open BinOp

# 56 "expr/exprParser.ml"

let rec _menhir_run7 : _menhir_env -> 'ttv_tail * _menhir_state * (ExprAst.expression) -> 'ttv_return =
  fun _menhir_env _menhir_stack ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState7 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState7 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState7
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState7
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState7

and _menhir_run10 : _menhir_env -> 'ttv_tail * _menhir_state * (ExprAst.expression) -> 'ttv_return =
  fun _menhir_env _menhir_stack ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState10 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState10 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState10
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState10
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState10

and _menhir_run12 : _menhir_env -> 'ttv_tail * _menhir_state * (ExprAst.expression) -> 'ttv_return =
  fun _menhir_env _menhir_stack ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState12 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState12 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState12
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState12
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState12

and _menhir_run16 : _menhir_env -> 'ttv_tail * _menhir_state * (ExprAst.expression) -> 'ttv_return =
  fun _menhir_env _menhir_stack ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState16 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState16 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState16
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState16
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState16

and _menhir_run14 : _menhir_env -> 'ttv_tail * _menhir_state * (ExprAst.expression) -> 'ttv_return =
  fun _menhir_env _menhir_stack ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState14 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState14 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState14
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState14
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState14

and _menhir_goto_expr : _menhir_env -> 'ttv_tail -> _menhir_state -> (ExprAst.expression) -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s _v ->
    let _menhir_stack = (_menhir_stack, _menhir_s, _v) in
    match _menhir_s with
    | MenhirState2 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        assert (not _menhir_env._menhir_error);
        let _tok = _menhir_env._menhir_token in
        (match _tok with
        | DIV ->
            _menhir_run14 _menhir_env (Obj.magic _menhir_stack)
        | MINUS ->
            _menhir_run16 _menhir_env (Obj.magic _menhir_stack)
        | MOD ->
            _menhir_run12 _menhir_env (Obj.magic _menhir_stack)
        | PLUS ->
            _menhir_run10 _menhir_env (Obj.magic _menhir_stack)
        | RPAR ->
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_env = _menhir_discard _menhir_env in
            let _menhir_stack = Obj.magic _menhir_stack in
            let ((_menhir_stack, _menhir_s), _, (e : (ExprAst.expression))) = _menhir_stack in
            let _3 = () in
            let _1 = () in
            let _v : (ExprAst.expression) = 
# 27 "expr/exprParser.mly"
                               ( e )
# 175 "expr/exprParser.ml"
             in
            _menhir_goto_simple_expr _menhir_env _menhir_stack _menhir_s _v
        | TIMES ->
            _menhir_run7 _menhir_env (Obj.magic _menhir_stack)
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_menhir_stack, _menhir_s, _) = _menhir_stack in
            _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s)
    | MenhirState7 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = Obj.magic _menhir_stack in
        let ((_menhir_stack, _menhir_s, (e1 : (ExprAst.expression))), _, (e2 : (ExprAst.expression))) = _menhir_stack in
        let _10 = () in
        let _v : (ExprAst.expression) = let o =
          let _1 = _10 in
          
# 34 "expr/exprParser.mly"
              ( Bmul )
# 196 "expr/exprParser.ml"
          
        in
        
# 23 "expr/exprParser.mly"
                               ( Binop(o,e1,e2) )
# 202 "expr/exprParser.ml"
         in
        _menhir_goto_expr _menhir_env _menhir_stack _menhir_s _v
    | MenhirState10 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        assert (not _menhir_env._menhir_error);
        let _tok = _menhir_env._menhir_token in
        (match _tok with
        | DIV ->
            _menhir_run14 _menhir_env (Obj.magic _menhir_stack)
        | MOD ->
            _menhir_run12 _menhir_env (Obj.magic _menhir_stack)
        | TIMES ->
            _menhir_run7 _menhir_env (Obj.magic _menhir_stack)
        | EOF | MINUS | PLUS | RPAR ->
            let _menhir_stack = Obj.magic _menhir_stack in
            let ((_menhir_stack, _menhir_s, (e1 : (ExprAst.expression))), _, (e2 : (ExprAst.expression))) = _menhir_stack in
            let _10 = () in
            let _v : (ExprAst.expression) = let o =
              let _1 = _10 in
              
# 33 "expr/exprParser.mly"
              ( Badd )
# 225 "expr/exprParser.ml"
              
            in
            
# 23 "expr/exprParser.mly"
                               ( Binop(o,e1,e2) )
# 231 "expr/exprParser.ml"
             in
            _menhir_goto_expr _menhir_env _menhir_stack _menhir_s _v
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_menhir_stack, _menhir_s, _) = _menhir_stack in
            _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s)
    | MenhirState12 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = Obj.magic _menhir_stack in
        let ((_menhir_stack, _menhir_s, (e1 : (ExprAst.expression))), _, (e2 : (ExprAst.expression))) = _menhir_stack in
        let _10 = () in
        let _v : (ExprAst.expression) = let o =
          let _1 = _10 in
          
# 36 "expr/exprParser.mly"
              ( Bmod )
# 250 "expr/exprParser.ml"
          
        in
        
# 23 "expr/exprParser.mly"
                               ( Binop(o,e1,e2) )
# 256 "expr/exprParser.ml"
         in
        _menhir_goto_expr _menhir_env _menhir_stack _menhir_s _v
    | MenhirState14 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = Obj.magic _menhir_stack in
        let ((_menhir_stack, _menhir_s, (e1 : (ExprAst.expression))), _, (e2 : (ExprAst.expression))) = _menhir_stack in
        let _10 = () in
        let _v : (ExprAst.expression) = let o =
          let _1 = _10 in
          
# 35 "expr/exprParser.mly"
              ( Bdiv )
# 269 "expr/exprParser.ml"
          
        in
        
# 23 "expr/exprParser.mly"
                               ( Binop(o,e1,e2) )
# 275 "expr/exprParser.ml"
         in
        _menhir_goto_expr _menhir_env _menhir_stack _menhir_s _v
    | MenhirState16 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        assert (not _menhir_env._menhir_error);
        let _tok = _menhir_env._menhir_token in
        (match _tok with
        | DIV ->
            _menhir_run14 _menhir_env (Obj.magic _menhir_stack)
        | MOD ->
            _menhir_run12 _menhir_env (Obj.magic _menhir_stack)
        | TIMES ->
            _menhir_run7 _menhir_env (Obj.magic _menhir_stack)
        | EOF | MINUS | PLUS | RPAR ->
            let _menhir_stack = Obj.magic _menhir_stack in
            let ((_menhir_stack, _menhir_s, (e1 : (ExprAst.expression))), _, (e2 : (ExprAst.expression))) = _menhir_stack in
            let _10 = () in
            let _v : (ExprAst.expression) = let o =
              let _1 = _10 in
              
# 32 "expr/exprParser.mly"
              ( Bsub )
# 298 "expr/exprParser.ml"
              
            in
            
# 23 "expr/exprParser.mly"
                               ( Binop(o,e1,e2) )
# 304 "expr/exprParser.ml"
             in
            _menhir_goto_expr _menhir_env _menhir_stack _menhir_s _v
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_menhir_stack, _menhir_s, _) = _menhir_stack in
            _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s)
    | MenhirState1 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let _menhir_stack = Obj.magic _menhir_stack in
        let ((_menhir_stack, _menhir_s), _, (e : (ExprAst.expression))) = _menhir_stack in
        let _1 = () in
        let _v : (ExprAst.expression) = 
# 22 "expr/exprParser.mly"
                               ( Uminus e )
# 321 "expr/exprParser.ml"
         in
        _menhir_goto_expr _menhir_env _menhir_stack _menhir_s _v
    | MenhirState0 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        assert (not _menhir_env._menhir_error);
        let _tok = _menhir_env._menhir_token in
        match _tok with
        | DIV ->
            _menhir_run14 _menhir_env (Obj.magic _menhir_stack)
        | EOF ->
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_menhir_stack, _menhir_s, (e : (ExprAst.expression))) = _menhir_stack in
            let _2 = () in
            let _v : (
# 10 "expr/exprParser.mly"
       ( ExprAst.expression )
# 339 "expr/exprParser.ml"
            ) = 
# 19 "expr/exprParser.mly"
                         ( e )
# 343 "expr/exprParser.ml"
             in
            let _menhir_stack = Obj.magic _menhir_stack in
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_1 : (
# 10 "expr/exprParser.mly"
       ( ExprAst.expression )
# 350 "expr/exprParser.ml"
            )) = _v in
            Obj.magic _1
        | MINUS ->
            _menhir_run16 _menhir_env (Obj.magic _menhir_stack)
        | MOD ->
            _menhir_run12 _menhir_env (Obj.magic _menhir_stack)
        | PLUS ->
            _menhir_run10 _menhir_env (Obj.magic _menhir_stack)
        | TIMES ->
            _menhir_run7 _menhir_env (Obj.magic _menhir_stack)
        | _ ->
            assert (not _menhir_env._menhir_error);
            _menhir_env._menhir_error <- true;
            let _menhir_stack = Obj.magic _menhir_stack in
            let (_menhir_stack, _menhir_s, _) = _menhir_stack in
            _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s

and _menhir_goto_simple_expr : _menhir_env -> 'ttv_tail -> _menhir_state -> (ExprAst.expression) -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s _v ->
    let _menhir_stack = Obj.magic _menhir_stack in
    let _menhir_stack = Obj.magic _menhir_stack in
    let (e : (ExprAst.expression)) = _v in
    let _v : (ExprAst.expression) = 
# 24 "expr/exprParser.mly"
                               ( e )
# 376 "expr/exprParser.ml"
     in
    _menhir_goto_expr _menhir_env _menhir_stack _menhir_s _v

and _menhir_errorcase : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    match _menhir_s with
    | MenhirState16 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s, _) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState14 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s, _) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState12 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s, _) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState10 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s, _) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState7 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s, _) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState2 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState1 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        let (_menhir_stack, _menhir_s) = _menhir_stack in
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) _menhir_s
    | MenhirState0 ->
        let _menhir_stack = Obj.magic _menhir_stack in
        raise _eRR

and _menhir_run1 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_stack = (_menhir_stack, _menhir_s) in
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState1 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState1 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState1
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState1
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState1

and _menhir_run2 : _menhir_env -> 'ttv_tail -> _menhir_state -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s ->
    let _menhir_stack = (_menhir_stack, _menhir_s) in
    let _menhir_env = _menhir_discard _menhir_env in
    let _tok = _menhir_env._menhir_token in
    match _tok with
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState2 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState2 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState2
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState2
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState2

and _menhir_run3 : _menhir_env -> 'ttv_tail -> _menhir_state -> (
# 7 "expr/exprParser.mly"
       (int)
# 456 "expr/exprParser.ml"
) -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s _v ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let (i : (
# 7 "expr/exprParser.mly"
       (int)
# 464 "expr/exprParser.ml"
    )) = _v in
    let _v : (ExprAst.expression) = 
# 29 "expr/exprParser.mly"
                               ( Const i )
# 469 "expr/exprParser.ml"
     in
    _menhir_goto_simple_expr _menhir_env _menhir_stack _menhir_s _v

and _menhir_run4 : _menhir_env -> 'ttv_tail -> _menhir_state -> (
# 8 "expr/exprParser.mly"
       (string)
# 476 "expr/exprParser.ml"
) -> 'ttv_return =
  fun _menhir_env _menhir_stack _menhir_s _v ->
    let _menhir_env = _menhir_discard _menhir_env in
    let _menhir_stack = Obj.magic _menhir_stack in
    let (id : (
# 8 "expr/exprParser.mly"
       (string)
# 484 "expr/exprParser.ml"
    )) = _v in
    let _v : (ExprAst.expression) = 
# 28 "expr/exprParser.mly"
                               ( Var id )
# 489 "expr/exprParser.ml"
     in
    _menhir_goto_simple_expr _menhir_env _menhir_stack _menhir_s _v

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

and expression : (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (
# 10 "expr/exprParser.mly"
       ( ExprAst.expression )
# 508 "expr/exprParser.ml"
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
    | IDENT _v ->
        _menhir_run4 _menhir_env (Obj.magic _menhir_stack) MenhirState0 _v
    | INT _v ->
        _menhir_run3 _menhir_env (Obj.magic _menhir_stack) MenhirState0 _v
    | LPAR ->
        _menhir_run2 _menhir_env (Obj.magic _menhir_stack) MenhirState0
    | MINUS ->
        _menhir_run1 _menhir_env (Obj.magic _menhir_stack) MenhirState0
    | _ ->
        assert (not _menhir_env._menhir_error);
        _menhir_env._menhir_error <- true;
        _menhir_errorcase _menhir_env (Obj.magic _menhir_stack) MenhirState0)

# 38 "expr/exprParser.mly"
  

# 538 "expr/exprParser.ml"

# 233 "/home/valeporti/.opam/system/lib/menhir/standard.mly"
  

# 543 "expr/exprParser.ml"

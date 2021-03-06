(* Entry point of the program, should contain your main function: here it is
named parse_eval, it is the function provided after question 6.1 *)

let rec print_list_of_expr = function 
| [] -> ()
| e::l -> print_string (PfxAst.string_of_command e) ; print_string "\n" ; print_list_of_expr l


(* The main function *)
let parse_eval file =
  print_string ("File "^file^" is being treated!\n");
  try
    let input_file = open_in file in
    let lexbuf = Lexing.from_channel input_file in
    begin
      try
        let expr_prog = ExprParser.expression ExprLexer.token lexbuf in
        print_string "Length list: "; print_int (List.length (ExprToPfx.generateV3 0 0 [] expr_prog)); print_string "\n";
        let pfx_prog = 0, (ExprToPfx.generateV3 0 0 [] expr_prog) in
        print_endline (PfxAst.string_of_program pfx_prog);
        PfxEval.eval_program pfx_prog []
      with
      | PfxParser.Error ->
        print_string "Syntax error: ";
        Location.print (Location.curr lexbuf)
      | Location.Error(e,l) ->
  print_string "Location Error: ";
        print_string e;
        Location.print l
    end;
    close_in (input_file)
  with Sys_error s ->
    print_endline ("Can't find file '" ^ file ^ "'")

(* Here we add the parsing of the command line and link to the main function *)
let _ =
  Arg.parse [] parse_eval ""
 
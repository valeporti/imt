(* Entry point of the program, should contain your main function: here it is
 named parse_eval, it is the function provided after question 6.1 *)

(* The arguments, initially empty *)
let args = ref []

let rec print_list = function 
[] -> ()
| e::l -> print_int e ; print_string " " ; print_list l

let rec go = function
	| EOF -> print_string "endof"
	| _ -> print_string "another"

(* The main function *)
let parse_eval file =
  print_string ("File "^file^" is being treated!\n");
  (*let buffer = Lexing.from_string "Push 0";
  print_string(token buffer);*)
  try
  	
  	let buff = Lexing.from_string "Push 0";
  	let el = PfxLexer.token buff;
  	go el;
  	
    let input_file = open_in file in
    let lexbuf = Lexing.from_channel "Push 0" in
    begin

    	try
    		
        (*let pfx_prog = PfxParser.program PfxLexer.token lexbuf in
         PfxEval.eval_program pfx_prog !args*)
      with
      | PfxParser.Error ->
         print_string "Syntax error: ";
         Location.print (Location.curr lexbuf)
      | Location.Error(e,l) ->
         print_string e;
         Location.print l
(*
      try
        let pfx_prog = PfxParser.program PfxLexer.token lexbuf in
         PfxEval.eval_program pfx_prog !args
      with
      | PfxParser.Error ->
         print_string "Syntax error: ";
         Location.print (Location.curr lexbuf)
      | Location.Error(e,l) ->
         print_string e;
         Location.print l
*)
    end;
    close_in (input_file)
  with Sys_error s ->
    print_endline ("Can't find file '" ^ file ^ "'")

(* Here we add the parsing of the command line and link to the main function *)
let _ =
  (* functionn to register arguments *)
  let register_arg i = args := !args@[i] in
  (* each option -a INTEGER is considered as an argument *)
  Arg.parse ["-a",Arg.Int register_arg,"integer argument"] parse_eval ""

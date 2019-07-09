
let rec print_list_of_expr = function 
| [] -> ()
| e::l -> print_string (PfxAst.string_of_command e) ; print_string "\n" ; print_list_of_expr l

let five file = 
  print_string ("File "^file^" is being treated!\n");
  try
    let input_file = open_in file in
    let lexbuf = Lexing.from_channel input_file in
    begin
      try
        let expr_prog = ExprParser.expression ExprLexer.token lexbuf in
        print_string "Length list: "; print_int (List.length (ExprToPfx.generate expr_prog)); print_string "\n";
        print_list_of_expr (ExprToPfx.generate expr_prog);
        let pfx_prog = 0, ExprToPfx.generate expr_prog in
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

(* to test 6.1 exercise *)
let six_one str = 
  print_string ("Starting to analyse string: "^str^"\n");
	let lexbuf = Lexing.from_string str in
	begin
		try
			while true do
				let result = Helpers.go PfxLexerTest.token lexbuf in
					Helpers.print_tk result; print_newline();
					if result = EOF then raise Exit;
			done
		with
			| Exit -> print_string "ended string\n"; 
			|_ -> print_string "error detected!!\n";
  end
  
let six_two file = 
  print_string ("File "^file^" is being treated!\n");
	try
		let input_file = open_in file in
		let lexbuf = Lexing.from_channel input_file in
		begin
			try
				while true do
					let result = Helpers.go PfxLexerTest.token lexbuf in
						Helpers.print_tk result; print_newline();
						if result = EOF then raise Exit;
				done
			with
				| Exit -> print_string "ended string in file\n"; 
				|_ -> print_string "error detected!!\n"; 
    end;
    close_in (input_file)
	with Sys_error s ->
    print_endline ("Can't find file '" ^ file ^ "'")

let seven file = 
  print_string ("File "^file^" is being treated!\n");
	try
		let input_file = open_in file in
		let lexbuf = Lexing.from_channel input_file in
		begin
			try
				(* Initialize Location errors *)
				Location.init lexbuf file;
				(* search all token matches *)
				while true do
					let result = Helpers.go PfxLexerTest.token lexbuf in
						Helpers.print_tk result; print_newline();
						if result = EOF then raise Exit;
				done
			with
				(* First match is the "break" of loop when it ends, so, no error *)
				| Exit -> print_string "ended string in file\n"; 
				(* Error detections *)
				| Location.Error(e, l) ->
					print_string "Found Location Error:\n";
					print_string e;
					Location.print l;
				| _ -> print_string "Non Covered Error Detected!\n"; 
    end;
    close_in (input_file)
	with Sys_error s ->
    print_endline ("Can't find file '" ^ file ^ "'")

let eight file args = 
  print_string ("File "^file^" is being treated!\n");
  try  	
    let input_file = open_in file in
    let lexbuf = Lexing.from_channel input_file in
    begin
      try
        Location.init lexbuf file;
        let pfx_prog = PfxParser.program PfxLexer.token lexbuf in
          print_endline (PfxAst.string_of_program pfx_prog);
          PfxEval.eval_program pfx_prog args
      with
      | PfxParser.Error ->
         print_string "Syntax error: ";
         Location.print (Location.curr lexbuf)
      | Location.Error(e,l) ->
         print_string e;
         Location.print l
    end;
    close_in (input_file)
  with Sys_error s ->
    print_endline ("Can't find file '" ^ file ^ "'")

let ten file args =
  print_string ("File "^file^" is being treated!\n");
  try
    let input_file = open_in file in
    let lexbuf = Lexing.from_channel input_file in
    begin
      try
        Location.init lexbuf file;
        let expr_prog = ExprParser.expression ExprLexer.token lexbuf in
        (*print_string "Length list: "; print_int (List.length (ExprToPfx.generateV2 0 0 expr_prog)); print_string "\n";
        print_list_of_expr (ExprToPfx.generateV2 0 0 expr_prog);*)
        let pfx_prog = 0, (ExprToPfx.generateV2 0 0 expr_prog) in
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
  
let eleven file args =
  print_string ("File "^file^" is being treated!\n");
  try
    let input_file = open_in file in
    let lexbuf = Lexing.from_channel input_file in
    begin
      try
        Location.init lexbuf file;
        let expr_prog = ExprParser.expression ExprLexer.token lexbuf in
        (*print_string "Length list: "; print_int (List.length (ExprToPfx.generateV3 0 0 [] expr_prog)); print_string "\n";
        print_list_of_expr (ExprToPfx.generateV3 0 0 [] expr_prog);*)
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
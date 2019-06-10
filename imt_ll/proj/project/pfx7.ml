open PfxLexerTest  	


let try_this file = 
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
				| _ -> print_string "Non Covered Error Detected!\n"; exit 0;
		end
	with Sys_error s ->
    print_endline ("Can't find file '" ^ file ^ "'")

let _ = 
	Arg.parse [] try_this ""


(*let count_a s = let buffer = Lexing.from_string s in count 0 buffer*)


(*try
	let lexbuf = buff in
	while true do
  	let result =  PfxLexer.token lexbuf in
			print_int result; print_newline(); flush std_out
	done
with Eof -> ()
;;*)

open PfxLexerTest  	

let try_this str = 
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
			|_ -> print_string "exiting\n"; exit 0;
	end

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

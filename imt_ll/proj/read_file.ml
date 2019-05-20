let compile file =
  print_string ("File "^file^" is being treated!\n");
  try
    let input_file = open_in file in
    let lexbuf = Lexing.from_channel input_file in
    (* work on the lexbuf *)
    close_in (input_file)
  with Sys_error s ->
    print_endline ("Can't find file '" ^ file ^ "'")

let _ = Arg.parse [] compile ""

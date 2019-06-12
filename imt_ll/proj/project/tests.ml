

(* The main function *)
let main some = 
  print_string "Hello!\n\n";
  try
    let str_pfx_test = "0 Push 2 Push 3 Add" in
    let file_pfx_test = "tp" in
    let file_expr_test = "tt" in
    let wrong_str_pfx_test = "nothing" in
      print_string " ---- OK Test For the ExprToPfx, Q 5 ----\n";
      TestFun.five file_expr_test; 
      print_string " ---- OK Test For the Lexer, Q 6.1 ----\n";
      TestFun.six_one str_pfx_test; 
      print_string " ---- WRONG Test For the Lexer, Q 6.1 ----\n";
      TestFun.six_one wrong_str_pfx_test; 
      print_string " ---- OK Test For the Parser, Q 6.2 ----\n";
      TestFun.six_two file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 7 ----\n";
      TestFun.seven file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 8 ----\n";
      TestFun.eight file_pfx_test []; (* file args *)
      
  with
    | _ -> print_string "Error on tests"
  

let _ = 
  Arg.parse [] main ""


(* The main function *)
let main () = 
  print_string "Hello!\n\n";
  try
    let str_pfx_test = "0 Push 2 Push 3 Add" in
    let file_pfx_test = "./tests/tp" in
    let file_pfx_test_args = "./tests/tpargs" in
    let file_expr_test = "./tests/tt" in
    let file_fun_9_pfx = "./tests/tpfun" in
    let wrong_str_pfx_test = "nothing" in
    let file_fun_lamda_pfx = "./tests/tpten" in
    let file_fun_lambda_simp_expr = "./tests/ttfunsimp" in
    let file_fun_lambda_comp_expr = "./tests/ttfun" in
    let file_fun_lambda_comp_expr2 = "./tests/ttfuncomp2" in
    let file_fun_lambda_comp_expr3 = "./tests/ttfun3" in
    let file_let_1 = "./tests/ttlet" in
    let file_let_2 = "./tests/ttlet2" in
    let file_let_3 = "./tests/ttlet3" in
    let file_let2_1 = "./tests/tttentwo" in
    let file_let2_2 = "./tests/tttenten" in
      print_string " ---- OK Test For the ExprToPfx, Q 5 ( 3+2-(4/2) = 3 )----\n";
      TestFun.five file_expr_test; 
      print_string " ---- OK Test For the Lexer, Q 6.1 ('0 Push 2 Push 3 Add') ----\n";
      TestFun.six_one str_pfx_test; 
      print_string " ---- WRONG Test For the Lexer, Q 6.1 ('nothing') ----\n";
      TestFun.six_one wrong_str_pfx_test; 
      print_string " ---- OK Test For the Lexer, Q 6.2  Print all tokens: ( 0 Push 1 Push 1 Add Push 3 Add Push 2 Mul Push 2 Div = 5) ----\n";
      TestFun.six_two file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 7 (Optimized Location errors) ----\n";
      TestFun.seven file_pfx_test;
      print_string " ---- OK Test For the Parser, Q 8 pfxPArser test ----\n";
      TestFun.eight file_pfx_test []; (* file args *)
      print_string " ---- OK Test For the Parser with Args, Q 8 (Args are 3, 7, 2) -> result = 5 ----\n";
      TestFun.eight file_pfx_test_args [Int 3; Int 7]; (* file args *)
      print_string " ---- OK Test For the Parser, Q 9 (Testing the adaptation of pfxParser and PfxLexer) ----\n";
      TestFun.eight file_fun_9_pfx []; 
      print_string " ---- OK Test For the Parser, Q 10.1 (\\x.x+1)(2) = 3 ----\n";
      TestFun.eight file_fun_lamda_pfx []; 
      print_string " ---- OK Test For generateV2, Q 10.3 (\\x.x+1)(2) = 3 ----\n";
      TestFun.ten file_fun_lambda_simp_expr []; 
      print_string " ---- OK Test 1 For generateV2, Q 10.3 (fun y -> (fun x->(20-x))(6) + y)(7) = 21  ----\n";
      TestFun.ten file_fun_lambda_comp_expr []; 
      print_string " ---- OK Test 2 For generateV2, Q 10.3 (fun y -> (fun x->(4*x))(6) / y)(2) = 12  ----\n";
      TestFun.ten file_fun_lambda_comp_expr2 []; 
      print_string " ---- OK Test 3 For generateV2, Q 10.3 ((fun y -> (fun x->(x+1))(2) + y)((fun x -> x*3)((fun x -> 3 + x)(2)))) = 18  ----\n";
      TestFun.ten file_fun_lambda_comp_expr3 []; 
      print_string " ---- OK Test 1 For generateV3, Q 11.2 \n\tlet x = 2 in \n\tlet y = 3 in\n\tlet z = x + y in\n\tz  \n\t= 5----\n";
      TestFun.eleven file_let_1 [];
      print_string " ---- OK Test 2 For generateV3, Q 11.2 \n\tlet x = ((fun x -> x+2)(2)) in \n\tlet y = (7+7) in\n\t((fun z -> x + y + z)(2))  \n\t= 20 ----\n";
      TestFun.eleven file_let_2 [];
      print_string " ---- OK Test 3 For generateV3, Q 11.2 \n\t(fun u -> u + 2)\n\t(\n\tlet x = ((fun v -> v+2)(2)) in \n\tlet y = (7+7) in\n\t((fun z -> x + y + z)(2))\n\t)  \n\t= 22 ----\n";
      TestFun.eleven file_let_3 [];
      print_string " ---- OK Test 3 For generateV3, Q 11.2 ((fun x -> fun y -> (x - y)) 12) 8 = 4 ----\n";
      TestFun.eleven file_let2_1 [];
      print_string " ---- OK Test 3 For generateV3, Q 11.2 \n\t(\n\t(\n\t(\n\t(\n\tfun x -> fun y -> fun z -> fun m -> (x - y + (z * m))\n\t) 2\n\t) ((fun n -> n + 2)(1))\n\t) 12\n\t)\n\t= 35 ----\n";
      TestFun.eleven file_let2_2 [];
  with
    | _ -> print_string "Error on tests"
  

let () = main ()
open ExprAst
open PfxAst

let soi i = string_of_int i

let rec getEnvV p n l = match l with
  | [] -> p
  | (Fv name, Pos pos)::tl ->
    begin
      if name = n then
        begin
          if pos = p then pos
          else if pos < p then pos (* Handle scope *)
          else if pos > p then failwith "error in searching pos"
          else getEnvV p n tl
        end
      else getEnvV p n tl
    end

let rec notInEnv v l = match l with
  | [] -> false (* Means, nothing to update in the environment *)
  | (Empty, Pos pos)::tl -> true
  | h::tl -> (notInEnv v tl)

let rec updateEnv v l = match l with
  | [] -> [] (* failwith "Error, nothing to update" *)
  | (Empty, Pos pos)::tl -> (Fv v, Pos pos)::tl
  | h::tl -> h::(updateEnv v tl)
    
let rec generateV3 t p env = (* t-for inner positions, p- for general position, env - free variables list *)  
  function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
			| Badd -> (generateV3 (t+1) (p+1) env e1)@(generateV3 (t+1) (p+1) env e2)@[Add]
			| Bsub -> (generateV3 (t+1) (p+1) env e1)@(generateV3 (t+1) (p+1) env e2)@[Sub]
			| Bmul -> (generateV3 (t+1) (p+1) env e1)@(generateV3 (t+1) (p+1) env e2)@[Mul]
			| Bdiv -> (generateV3 (t+1) (p+1) env e1)@(generateV3 (t+1) (p+1) env e2)@[Div]
			| Bmod -> (generateV3 (t+1) (p+1) env e1)@(generateV3 (t+1) (p+1) env e2)@[Rem]
		end		
  | Uminus e -> (generateV3 (t+1) (p+1) env e)@(generateV3 (t+1) (p+1) env (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) ->
    begin
      match e1, e2 with
      (* if Let detected, save its variable value, execute as App but with [Swap && Pop] *)
      | _, Let(v, e) -> (generateV3 t p env e2)@(generateV3 t (p+1) ([((Fv v), (Pos (p-t)))]@env) e1)@[Swap]@[Pop]
      (* a normal App case, insert into environnement "non able to name" future/now argument *)
      | _, _ -> (generateV3 t p env e2)@(generateV3 t (p+1) ([((Empty), (Pos (p-t)))]@env) e1)
    end
  | Fun(v, e) -> (* decide if environment has to be updated or a new variable should be added *)
    if (notInEnv v env) then 
      [Q (generateV3 0 p (updateEnv v env) e)]@[Exec]@[Swap]@[Pop]
    else
      [Q (generateV3 0 p ([((Fv v), (Pos (p-t)))]@env) e)]@[Exec]@[Swap]@[Pop]
  | Var v -> [Push (getEnvV p v env)]@[Get]
  (* Let Support *)
  | Let (v, e) -> (generateV3 0 p env e)



let rec generateV2 t p = (* t-for inner positions, p- for general position *)  
  function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
      (* []@[]@[] -> pos+1 pos+1 0 *)
			| Badd -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Add]
			| Bsub -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Sub]
			| Bmul -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Mul]
			| Bdiv -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Div]
			| Bmod -> (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Rem]
		end		
  | Uminus e -> (generateV2 (t+1) (p+1) e)@(generateV2 (t+1) (p+1) (Const 0))@[Sub]
  (* Function Support *)
  (* need it to be : Push c [ Push (position c) Get Push 2 Add ] Exec *)
  (* left exp is the function, right exp the argument *)
  | App(e1, e2) -> (generateV2 t p e2)@(generateV2 t p e1)
  | Fun(v, e) -> [Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
  | Var v -> [Push (p-t)]@[Get]

let rec generate = 
  function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
			match op with
			| Badd -> (generate e1)@(generate e2)@[Add]
			| Bsub -> (generate e1)@(generate e2)@[Sub]
			| Bmul -> (generate e1)@(generate e2)@[Mul]
			| Bdiv -> (generate e1)@(generate e2)@[Div]
			| Bmod -> (generate e1)@(generate e2)@[Rem]
		end		
  | Uminus e -> (generate e)@(generate (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> failwith "First Generate Version does not support App"
  | Fun(v, e) -> failwith "First Generate Version does not support Fun"
  | Var v -> failwith "First Generate Version does not support Var"
  | Let(v, e) -> failwith "First Generate Version does not support Let"

(*
let rec generate = function
  | Const c -> failwith "To implement"
  | Binop(op,e1,e2) -> failwith "To implement"
  | Uminus e -> failwith "To implement"
  | Var v -> failwith "Not yet supported"
*)

(* 5.2 *)
(*
let rec generate = function
  | Const c -> [Push c]
  | Binop(Badd,e1,e2) -> [Push e2; Push e1; Add] 
  | Binop(Bsub,e1,e2) -> [Push e2; Push e1; Sub]
  | Binop(Bmul,e1,e2) -> [Push e2; Push e1; Mul]
  | Binop(Bdiv,e1,e2) -> [Push e2; Push e1; Div]
  | Binop(Bmod,e1,e2) -> [Push e2; Push e1; Mod]
  | Uminus e -> [-e]
  | Var v -> failwith "Not yet supported"
*)

(* ----------------------------- PRINT RESULTS VERSIONS ---------------------------------------------------- *)

(* Generate V3 Print version *)
let rec generateV3pp t p env = (* t-for inner positions, p- for general position, env - variables list *)  
  function
  | Const c -> print_string ("Push "^(soi c)^"("^(soi t)^"+1,"^(soi p)^"+1)\n"); [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
			| Badd -> print_string ("Add ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3pp (t+1) (p+1) env e1)@(generateV3pp (t+1) (p+1) env e2)@[Add]
			| Bsub -> print_string ("Sub ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3pp (t+1) (p+1) env e1)@(generateV3pp (t+1) (p+1) env e2)@[Sub]
			| Bmul -> print_string ("Mul ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3pp (t+1) (p+1) env e1)@(generateV3pp (t+1) (p+1) env e2)@[Mul]
			| Bdiv -> print_string ("Div ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3pp (t+1) (p+1) env e1)@(generateV3pp (t+1) (p+1) env e2)@[Div]
			| Bmod -> print_string ("Mod ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV3pp (t+1) (p+1) env e1)@(generateV3pp (t+1) (p+1) env e2)@[Rem]
		end		
  | Uminus e -> (generateV3pp (t+1) (p+1) env e)@(generateV3pp (t+1) (p+1) env (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) ->
    begin
      match e1, e2 with
      | _, Let(v, e) -> print_string ("LetApp "^v^" ("^(string_of_expr e)^")\n"); (generateV3pp t p env e2)@(generateV3pp t (p+1) ([((Fv v), (Pos (p-t)))]@env) e1)@[Swap]@[Pop]
      (*| App(_, _), _ -> print_string ("AppApp \n"); print_string (string_of_env env); print_string "\n"; (generateV3pp t p env e2)@(generateV3pp t (p+1) ([((Empty), (Pos (p-t)))]@env) e1)@[Swap]@[Pop]*)
      | _, _ -> print_string ("App ("^(soi t)^","^(soi p)^")\n"); (generateV3pp t p env e2)@(generateV3pp t (p+1) ([((Empty), (Pos (p-t)))]@env) e1)
    end
  | Fun(v, e) -> 
    print_string ("Fun "^v^" ("^(soi 0)^","^(soi p)^")\n"); 
    print_string (string_of_env env);
    print_string "\n";
    if (notInEnv v env) then 
      [Q (generateV3pp 0 p (updateEnv v env) e)]@[Exec]@[Swap]@[Pop]
    else
      [Q (generateV3pp 0 p ([((Fv v), (Pos (p-t)))]@env) e)]@[Exec]@[Swap]@[Pop]
  | Var v -> 
    print_string ("Var "^v^" Push("^(soi p)^"-"^(soi t)^")\n"); 
    print_string (soi (getEnvV p v env)); 
    print_string "\n"; 
    print_string (string_of_env env);
    [Push (getEnvV p v env)]@[Get]
  | Let (v, e) -> 
    print_string ("Let "^v^" ("^(string_of_expr e)^")\n");
    print_string (string_of_env env);
    print_string "\n"; 
    print_string (soi (List.length(env)));
    print_string "\n"; 
    (*[Push (getEnvV p v env)]@[Get]*)
    (generateV3pp 0 p env e)
    (*(generateV3pp 0 p ([((Fv v), (Pos (p-t)))]@env) e)*)


(* PRINT ALL VAUES generateV2 Version  *)
(*
let rec generateV2 t p = (* t-for inner positions, p- for general position *)  
  function
  | Const c -> print_string ("Push "^(soi c)^"("^(soi t)^"+1,"^(soi p)^"+1)\n"); [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
      (* []@[]@[] -> pos+1 pos+1 and pos-1 *)
			| Badd -> print_string ("Add ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Add]
			| Bsub -> print_string ("Sub ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Sub]
			| Bmul -> print_string ("Mul ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Mul]
			| Bdiv -> print_string ("Div ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Div]
			| Bmod -> print_string ("Mod ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e1)@(generateV2 (t+1) (p+1) e2)@[Rem]
		end		
  | Uminus e -> (generateV2 (t+1) (p+1) e)@(generateV2 (t+1) (p+1) (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> (* need it to be : Push c [ Push (position c) Get Push 2 Add ] Exec *)
    begin
      match e1, e2 with 
      (* Handle simple App(\x.e , expression) *)
      | Fun(v, e), _ -> print_string ("Fun ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 t p e2)@[Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
      | _, _ -> failwith "Not Supported App Case"
      (*
      | ea, eb -> 
        print_string "  ||  "; 
        print_string (string_of_expr ea); 
        print_string "  ||  "; 
        print_string (string_of_expr eb); 
        print_string "\n"; 
        [Push 0]; *)
    end
  | Fun(v, e) -> print_string ("FunFun ("^(soi 0)^","^(soi p)^")\n"); failwith "Not Supported Function Case"; (generateV2 0 p e)
  | Var v -> print_string ("Var "^v^" Push("^(soi p)^"-"^(soi t)^")\n"); [Push (p-t)]@[Get]
*)

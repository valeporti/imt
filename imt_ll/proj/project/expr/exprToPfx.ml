open ExprAst
open PfxAst

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
let soi i = string_of_int i

(*
let rec findSize t s = function (* temp size *)
| [] -> print_string ("end("^(soi s)^")\n"); s
| Exec::tl -> print_string ("Exec("^(soi t)^")\n"); t
| (Add|Mul|Div|Sub|Rem|Swap)::tl -> print_string ("***("^(soi t)^","^(soi s)^")\n"); findSize (t-1) (s-1) tl (* Decrease one once applied *) 
| Push(c)::tl -> print_string ("Push("^(soi t)^","^(soi s)^")\n"); findSize (t+1) (s+1) tl (* Increase one *)
| Pop::tl -> print_string ("Pop("^(soi t)^","^(soi s)^")\n"); findSize (t-1) (s-1) tl (* Decrease one *)
| Get::tl -> print_string ("Get("^(soi t)^","^(soi s)^")\n"); findSize t s tl (* do nothing since it pops and add to stak *)
| Q(ins)::tl -> print_string ("Q("^(soi t)^","^(soi s)^")\n"); findSize (findSize 0 s ins) s tl (* start counting "internally" temp *) 
*)

(* PRINT ALL VAUES generateV2 Version 
let rec generateV2 t p = (* t-for inner positions, p- for general position *)  
  function
  | Const c -> print_string ("Push "^(soi c)^"("^(soi t)^"+1,"^(soi p)^"+1)\n"); [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
      (* []@[]@[] -> pos+1 pos+1 and pos-1 *)
			| Badd -> print_string ("Add ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Add]
			| Bsub -> print_string ("Sub ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Sub]
			| Bmul -> print_string ("Mul ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Mul]
			| Bdiv -> print_string ("Div ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Div]
			| Bmod -> print_string ("Mod ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Rem]
		end		
  | Uminus e -> (generateV2 (t+1) (p+1) e)@(generateV2 (t+1) (p+1) (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> (* need it to be : Push c [ Push (position c) Get Push 2 Add ] Exec *)
    begin
      match e1, e2 with 
      | Fun(v, e), _ -> print_string ("Fun ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 t p e2)@[Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
      | _, Fun(v, e) -> print_string ("Fun ("^(soi t)^"+1,"^(soi p)^"+1)\n"); (generateV2 t p e1)@[Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
      | _, _ -> failwith "Not Supported App Case"
    end
  | Fun(v, e) -> print_string ("FunFun ("^(soi 0)^","^(soi p)^")\n"); (generateV2 0 p e)
  | Var v -> print_string ("Var Push("^(soi p)^"-"^(soi t)^")\n"); [Push (p-t)]@[Get]
*)

let rec generateV2 t p = (* t-for inner positions, p- for general position *)  
  function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
      match op with
      (* []@[]@[] -> pos+1 pos+1 and pos-1 *)
			| Badd -> (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Add]
			| Bsub -> (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Sub]
			| Bmul -> (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Mul]
			| Bdiv -> (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Div]
			| Bmod -> (generateV2 (t+1) (p+1) e2)@(generateV2 (t+1) (p+1) e1)@[Rem]
		end		
  | Uminus e -> (generateV2 (t+1) (p+1) e)@(generateV2 (t+1) (p+1) (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> (* need it to be : Push c [ Push (position c) Get Push 2 Add ] Exec *)
    begin
      match e1, e2 with 
      | Fun(v, e), _ -> (generateV2 t p e2)@[Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
      | _, Fun(v, e) -> (generateV2 t p e1)@[Q (generateV2 0 p e)]@[Exec]@[Swap]@[Pop]
      | _, _ -> failwith "Not Supported App Case"
    end
  | Fun(v, e) -> (generateV2 0 p e)
  | Var v -> [Push (p-t)]@[Get]


let rec generate = 
  (*let sumOne x = x + 1 in
  let pos = -1 in*)
  function
  | Const c -> [Push c]
  | Binop(op,e1,e2) -> 
		begin
			match op with
			| Badd -> (generate e2)@(generate e1)@[Add]
			| Bsub -> (generate e2)@(generate e1)@[Sub]
			| Bmul -> (generate e2)@(generate e1)@[Mul]
			| Bdiv -> (generate e2)@(generate e1)@[Div]
			| Bmod -> (generate e2)@(generate e1)@[Rem]
		end		
  | Uminus e -> (generate e)@(generate (Const 0))@[Sub]
  (* Function Support *)
  | App(e1, e2) -> (* need it to be : Push c [ Get Push 2 Add ] Exec *)
    begin
      match e1, e2 with 
      (*
      | Const c, _ -> [Push c]@[Push (sumOne pos)]@[Q (generate e2)]@[Exec]
      | _, Const c -> [Push c]@[Push (sumOne pos)]@[Q (generate e1)]@[Exec]
      *)
      (*
      | Fun(v, e), _ -> (generate e2)@[Push (findSize 0 0 (generate e2))]@[Q (generate e)]@[Exec]
      | _, Fun(v, e) -> (generate e1)@[Push (findSize 0 0 (generate e1))]@[Q (generate e)]@[Exec] 
      *)
      | Fun(v, e), _ -> (generate e2)@[Q (generate e)]@[Exec]
      | _, Fun(v, e) -> (generate e1)@[Q (generate e)]@[Exec] 
      | _, _ -> failwith "Not Supported App Exption"
    end
  | Fun(v, e) -> generate e
  | Var v -> [Get]
  (*
  | Var v -> failwith "Not yet supported"
  *)

  (* ISSUE: How to calculate the size of the STACK? *)
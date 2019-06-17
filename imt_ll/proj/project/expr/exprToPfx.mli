(* Function that generate a Pfx program from an Expr program *)
val generate : ExprAst.expression -> PfxAst.command list

val generateV2 : int -> int -> ExprAst.expression -> PfxAst.command list

val generateV3 : int -> int -> (ExprAst.free_v * ExprAst.free_v) list -> ExprAst.expression -> PfxAst.command list

val generateV3pp: int -> int -> (ExprAst.free_v * ExprAst.free_v) list -> ExprAst.expression -> PfxAst.command list
import z3

Q = [ z3.Int('Q_%i' %(i +1)) for i in range(8) ]

val = [ z3.And(0 <= Q[i], Q[i] <= 7) for i in range(8)]

col = [ z3.Distinct(Q) ]

diag = [ z3.And( Q[i]-Q[j] != i-j, Q[i]-Q[j] != j-i) for i in range(8) for j in range(8) if i!=j]

s = z3.Solver()

s.add(val + col + diag)

print(s.check())
print(s.model())
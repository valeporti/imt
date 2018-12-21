# District Heating Genetic Hybrid Algorithm

###### Hello :)

Usage: 

use **main.py** as the principal file, all files will be called from there.

Use
```
python3 main.py
```

Requirements: 
- Built-in: * random, math, time, os *
- to import (pip3): * pandas, pprint, operator *
- to analyse data: * pandas, numpy, matplotlib.pyplot * 

The idea is that every single run will be saved so at one moment, you can mix every single file and study the behavior with next command: 

```
df1 = pandas.read_pickle(data_directory)
[...]
frames = [df1, df2, df3]
```

calling function is "run_GA" with Arguments:
```
(
  1. How many runs you want to test,
  2. DATA (make sure you are calling the expected excel data and format),
  3. Choice for left crossover operator,
  4. Choice for right crossover operator,
  5. Choice for left mutation operator,
  6. Choice for right mutation operator,
  7. Maximum iterations on GA,
  8. Population Size,
  9. Percentage of usage of Local Search outside the GA,
  10. Proposed configuration {'elitism':...},
  11. Name of the folder where to save results,
  12. Name of the file to save
)
```
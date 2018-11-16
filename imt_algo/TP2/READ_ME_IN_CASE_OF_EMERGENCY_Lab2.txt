
/* ------------------------------ SELECTION sort ---------------------------- */

  int i, j;
  int min;

    for(i = 0; i < size-1; i++)
      {
         min = i;

         for(j = i+1; j <= size-1; j++)
           {
             if (data[j] < data[min])  
               min = j;
           }
         echanger(data, min, i);
      }
    
/* ------------------------------ INSERTION sort ---------------------------- */

  int i, j;
  int v;

    for (i = 1; i <= size-1; i++)
      {
        v = data[i];
        j = i;

        while ( (j>0) && (data[j-1] > v) )
          {
            data[j] = data[j-1];
            j--;
          }
        data[j] = v;       
      }


/* ------------------------------ BUBBLE sort ---------------------------- */

  int i, j;

    for(i = size-1; i >= 1; i--)
      {
        for (j = 1; j <= i; j++)
          {
            if (data[j-1] > data[j])
              {
              echanger(data, j-1, j);
              }
          }
      }


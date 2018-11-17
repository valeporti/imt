void exchange (float *x, float *y)
{
	float temp; /* = null */

	temp = *x; /* dont loose x */
	*x = *y; /* assign y */
	*y = temp; /* get temp value */
}
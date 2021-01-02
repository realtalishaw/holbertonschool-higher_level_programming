#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - fjdsdfs
 * @p: jfddf
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *element;

	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

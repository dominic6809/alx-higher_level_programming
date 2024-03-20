#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints bytes object information
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	long int size_of_bytes, i;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		size_of_bytes = PyBytes_Size(p);
		printf("  size: %ld\n", size_of_bytes);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		if (size_of_bytes >= 10)
			size_of_bytes = 10;
		else
			size_of_bytes++;
		printf("  first %ld bytes:", size_of_bytes);
		for (i = 0; i < size_of_bytes; i++)
			printf(" %02x", (int) PyBytes_AsString(p)[i] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_list - Prints list object information
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

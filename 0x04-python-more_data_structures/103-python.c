#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints bytes object information
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	char *bytes_data;
	long int size, i, limit;

	printf("[.] bytes object info\n");

	/* Check if the input is a valid bytes object */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid bytes object\n");
		return;
	}

	/* Obtain the size and data of the bytes object */
	size = ((PyVarObject *)p)->ob_size;
	bytes_data = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_data);

	/* Determine the limit for printing the bytes */
	limit = (size >= 10) ? 10 : size;

	printf("  first %ld bytes:", limit);

	/* Print the first 'limit' bytes in hexadecimal format */
	for (i = 0; i < limit; i++)
		printf(" %02x", bytes_data[i] & 0xFF);

	printf("\n");
}

/**
 * print_python_list - Prints list object information
 * @p: Python list object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list_obj;
	PyObject *element;

	size = ((PyVarObject *)p)->ob_size;
	list_obj = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list_obj->allocated);

	/* Iterate over each element in the list */
	for (i = 0; i < size; i++)
	{
		element = list_obj->ob_item[i];
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

		/* If the element is a bytes object, print its information */
		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}

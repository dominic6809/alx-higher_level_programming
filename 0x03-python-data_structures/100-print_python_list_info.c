#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: Pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (pyListObject *)p;

	printf("[*] size of the python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s", i, Py_TYPE(obj->ob_item[i])->tp_name);
	}
}

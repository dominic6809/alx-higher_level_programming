#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - displays data of the PyFloatObject
 * @p: the PyObject
 * Return: success
 */
void print_python_float(PyObject *p)
{
    double value = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] float object info\n");

    if (!PyFloat_CheckExact(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }
    
    value = PyFloat_AsDouble(p);
    string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", string);
}

/**
 * print_python_bytes - displays data of the PyBytesObject
 * @p: the PyObject
 * Return: success
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size = 0, n = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] bytes object info\n");
    
    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    
    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);
    
    string = PyBytes_AsString(p);
    printf("  trying string: %s\n", string);
    printf("  first %zd bytes:", size < 10 ? size : 10);
    
    while (n < size && n < 10)
    {
        printf(" %02hhx", string[i]);
        n++;
    }
    
    printf("\n");
}

/**
 * print_python_list - displays data of the PyListObject
 * @p: the PyObject
 * Return: success
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size = 0;
    int n = 0;

    fflush(stdout);
    printf("[*] Python list info\n");
    
    if (PyList_CheckExact(p))
    {
        size = PyList_GET_SIZE(p);
        printf("[*] Size of the Python List = %zd\n", size);

        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
        
        while (n < size)
        {
            PyObject *item = PyList_GET_ITEM(p, n);
            printf("Element %d: %s\n", n, Py_TYPE(item)->tp_name);
            
            if (PyBytes_Check(item))
                print_python_bytes(item);
            else if (PyFloat_Check(item))
                print_python_float(item);
            
            n++;
        }
    }
    else
    {
        printf("  [ERROR] Invalid List Object\n");
    }
}

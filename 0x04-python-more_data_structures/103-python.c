#include <stdio.h>
#include <Python.h>

/* Print Python list information */
void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid Python list\n");
        return;
    }

    Py_ssize_t size = ((PyVarObject *)p)->ob_size;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject *element = ((PyListObject *)p)->ob_item[i];
        const char *type_name = element->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type_name);
    }
}

/* Print Python bytes information */
void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Python bytes object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);

    printf("  first 10 bytes:");
    for (Py_ssize_t i = 0; i < ((PyVarObject *)p)->ob_size && i < 10; ++i) {
        printf(" %02hhx", ((char *)(((PyBytesObject *)p)->ob_sval))[i]);
    }
    printf("\n");
}

#include <Python.h>

static PyObject*
show(PyObject* self, PyObject* args)
{
    const char* content;

    if (!PyArg_ParseTuple(args, "s", &content))
        return NULL;

    printf("%s!\n", content);

    Py_RETURN_NONE;
}

static PyMethodDef Methods[] =
{
     {"show", show, METH_VARARGS, "Print input"},
     {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
inithelloworld(void)
{
     (void) Py_InitModule("helloworld", Methods);
}

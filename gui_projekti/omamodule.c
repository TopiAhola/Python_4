

/*
Note Since Python may define some pre-processor definitions which affect the standard headers on some systems, you must include Python.h before any standard headers are included.
#define PY_SSIZE_T_CLEAN was used to indicate that Py_ssize_t should be used in some APIs instead of int. It is not necessary since Python 3.13, but we keep it here for backward compatibility. See Strings and buffers for a description of this macro.
*/

#define PY_SSIZE_T_CLEAN  //mitä tämä tekee?

#include <Python.h>  //tämä täytyy importata ennen muita header fileja

//placeholder for errors
/*Since OmaError is a global variable, it will be overwritten every time the module is reinitialized, when the Py_mod_exec function is called.*/
static PyObject * OmaError = NULL;


//initializes the module?
static int
oma_module_exec(PyObject *m)
{

    if (OmaError != NULL) {
        PyErr_SetString(PyExc_ImportError,
                        "cannot initialize module more than once");
        return -1;
    }

    OmaError = PyErr_NewException("oma.error", NULL, NULL);
    if (PyModule_AddObjectRef(m, "OmaError", OmaError) < 0) {
        return -1;
    }

    return 0;
}

/*
There is a straightforward translation from the argument list in Python (for example, the single expression "ls -l") to the arguments passed to the C function. The C function always has two arguments, conventionally named self and args.
The self argument points to the module object for module-level functions; for a method it would point to the object instance.
The args argument will be a pointer to a Python tuple object containing the arguments. Each item of the tuple corresponds to an argument in the call’s argument list. The arguments are Python objects — in order to do anything with them in our C function we have to convert them to C values. The function PyArg_ParseTuple() in the Python API checks the argument types and converts them to C values. It uses a template string to determine the required types of the arguments as well as the types of the C variables into which to store the converted values. More about this later.
PyArg_ParseTuple() returns true (nonzero) if all arguments have the right type and its components have been stored in the variables whose addresses are passed. It returns false (zero) if an invalid argument list was passed. In the latter case it also raises an appropriate exception so the calling function can return NULL immediately (as we saw in the example).
*/

static PyObject *
funktio1(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    // parses args tuple as "s" format into command char memory location "s" is 'const char *'
    if (!PyArg_ParseTuple(args, "s", &command)
        return NULL;

    //pass command char* string as system command return response value as long number
    sts = system(command);

    //this sets error message to OmaError
    if (sts < 0) {
        PyErr_SetString(OmaError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}

/**
* If you have a C function that returns no useful argument (a function returning void), the corresponding Python function must return None. You need this idiom to do so (which is implemented by the Py_RETURN_NONE macro):

Py_INCREF(Py_None);
return Py_None;
 *
 */


static PyObject *
integer_sum(PyObject *self, PyObject *args)
{

    const int *a;
    const int *b;
    int result = 0;

    // parses args tuple as 2 integers
    if (!PyArg_ParseTuple(args, "i", &a, &b) {
        result = *a + *b;
    } else {
        PyErr_SetString(OmaError, "Wrong number of arguments");
        return NULL;
    }

    return PyInt_FromInt(result);
}



/*The self argument points to the module object for module-level functions; for a method it would point to the object instance.

The args argument will be a pointer to a Python tuple object containing the arguments.
Each item of the tuple corresponds to an argument in the call’s argument list.
The arguments are Python objects — in order to do anything with them in our C function we have to convert them to C values.
The function PyArg_ParseTuple() in the Python API checks the argument types and converts them to C values.
It uses a template string to determine the required types of the arguments as well as the types of the C variables into
which to store the converted values. More about this later.

PyArg_ParseTuple() returns true (nonzero) if all arguments have the right type and its components have been stored
in the variables whose addresses are passed. It returns false (zero) if an invalid argument list was passed.
In the latter case it also raises an appropriate exception so the calling function can return NULL immediately (as we saw in the example).
*/

/*
 *Module method table and initialization function
 *Note the third entry (METH_VARARGS). This is a flag telling the interpreter the
 *calling convention to be used for the C function.
 *It should normally always be METH_VARARGS or METH_VARARGS | METH_KEYWORDS;
 *a value of 0 means that an obsolete variant of PyArg_ParseTuple() is used.
 *
*When using only METH_VARARGS, the function should expect the Python-level parameters
*to be passed in as a tuple acceptable for parsing via PyArg_ParseTuple();
*

The METH_KEYWORDS bit may be set in the third field if keyword arguments should be
passed to the function. In this case, the C function should accept
a third PyObject * parameter which will be a dictionary of keywords.
Use PyArg_ParseTupleAndKeywords() to parse the arguments to such a function.
 */

static PyMethodDef oma_methods[] = {
    ...
    {"system",  oma_system, METH_VARARGS,"Execute a shell command."},
    {"integer_sum", integer_sum, METH_VARARGS,"Sums 2 integers"},
    ...
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef oma_module = {
    ...
    .m_methods = oma_methods,
    ...
};

//PyMODINIT_FUNC declares the function as PyObject * return type,
//declares any special linkage declarations required by the platform,
//and for C++ declares the function as extern "C".
PyMODINIT_FUNC
PyInit_oma(void)
{
    return PyModuleDef_Init(&oma_module);
}
/*
 * When embedding Python, the PyInit_oma() function is not called automatically
 * unless there’s an entry in the PyImport_Inittab table.
 * To add the module to the initialization table, use PyImport_AppendInittab(),
 * optionally followed by an import of the module
 */
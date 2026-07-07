

/*
Note Since Python may define some pre-processor definitions which affect the standard headers on some systems, you must include Python.h before any standard headers are included.
#define PY_SSIZE_T_CLEAN was used to indicate that Py_ssize_t should be used in some APIs instead of int. It is not necessary since Python 3.13, but we keep it here for backward compatibility. See Strings and buffers for a description of this macro.
*/

#define PY_SSIZE_T_CLEAN  //mitä tämä tekee?

#include <Python.h>  //tämä täytyy importata ennen muita header fileja


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
    return PyLong_FromLong(sts);
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
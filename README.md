# C style and coding rules

This document describes C code style used by Tilen MAJERLE in his projects and libraries.

# General rules

Here are listed most obvious and important general rules. Please check them carefully before you continue with other chapters.

- Do not use tabs, use spaces instead
- Use `4` spaces per indent level
- Use `1` space between keyword and opening bracket
- Do not use space between function name and opening bracket
- Opening curly bracket is always on the same line as keyword (`for`, `while`, `do`, `switch`, `if`, ...)
- Use single space before and after comparison and assignments operators
- Use single space after every comma (`func_name(param1, param2)`)
- Do not initialize `static` and `global` variables to `0` (or `NULL`), let compiler do it for you
- Declare all local variables of the same type in the same line
- Except `char`, always use types declared in `stdint.h` library, eg. `uint8_t` for `unsigned 8-bit`, etc.
- Always compare pointers against `NULL` value, eg. `if (ptr != NULL) { ... }` (or `ptr == NULL`), do not use `if (ptr) { ... }`
- Never compare against `true`, eg. `if (check_func() == 1)`, use `if (check_func()) { ... }`
- Always use `/* comment */` for comments, even when *single-line* comment
- Always include check for `C++` with `extern` keyword in header file
- Every function must include *doxygen-enabled* comment, even if function is `static`
- Use English names/text for functions, variables, comments
- Never cast function returning `void *`, eg. `uint8_t* ptr = (uint8_t *)func_returning_void_ptr();` as `void *` is safely promoted to any other pointer type
- Always respect code style already used in project or library

# Comments

- Comments starting with `//` are not allowed. Always use `/* comment */`, even for single-line comment
```c
//This is comment (wrong)
/* This is commenet (ok) */
```

- For multi-line comments use `space+asterix` for every line

```c
/*
 * This is multi-line comments,
 * written in 2 lines (ok)
 */
 
/**
 * Wrong, use double-asterix only for doxygen documentation
 */
 
/*
* Single line comment without space before asterix (wrong)
*/

/*
 * Single line comment in multi-line configuration (wrong)
 */

/* Single line comment (ok) */
```

Use `12` indents (`12 * 4` spaces) offset when commenting. If statement is larger than `12` indents, make comment `4-spaces` aligned (examples below)

```c
void
my_func(void) {
    char a, b;
                                                
    a = call_func_returning_char_a(a);          /* This is comment with 12*4 spaces indent from beginning of line */
    b = call_func_returning_char_a_but_func_name_is_very_long(a);   /* This is comment, aligned to 4-spaces indent */
}
```

# Functions

- Every function which may be access from outside module, must include function *prototype* (or *declaration*)
- Function names must be lowercase, optionally separated with underscore `_` character
```c
/* OK */
void my_func(void);
void myfunc(void);

/* Wrong */
void MYFunc(void);
void myFunc();
```

- When function returns pointer, asterix character must be left aligned without space
```c
/* OK */
const char* my_func(void);
my_struct_t* my_func(int a, int b);

/* Wrong */
const char *my_func(void);
my_struct_t * my_func(void);
```
- Align all function prototypes (with the same/similar functionality) for better readability
```c
/* OK, function names aligned */
void        set(int a);
my_type_t   get(void);

/* Wrong */
void set(int a);
const char* get(void);
```

- Function implementation must include return type and optional other keywords in separate line
```c
/* OK */
int
foo(void) {
    return 0;
}

/* OK */
static const char *
get_string(void) {
    return "Hello world!\r\n";
}

/* Wrong */
int foo(void) {
    return 0;
}
```

- When function returns pointer, asterix character must include space between type and character (`char *`)
```c
/* OK */
const char *
foo(void) {
    return "test";
}

/* Wrong */
const char*
foo(void) {
    return "test";
}
```

# Variables

- Make variable name all lowercase with optional underscore `_` character
```c
/* OK */
int a;
int my_var;
int myvar;

/* Wrong */
int A; 
int myVar;
int MYVar;
```

- Group local variables together by `type`
```c
void
foo(void) {
    int a, b;   /* OK */
    char a;
    char b;     /* Wrong, char type already exists */
}
```

- Do not declare variable after first executable statement
```c
void
foo(void) {
    int a;
    a = bar();
    int b;      /* Wrong, there is already executable statement */
}
```

- You may declare new variables inside next indent level
```c
int a, b;
a = foo();
if (a) {
    int c, d;   /* OK, c and d are in if-statement scope */
    c = foo();
    int e;      /* Wrong, there was already executable statement inside block */
}
```

- Declare pointer variables with asterix aligned to type
```c
/* OK */
char* a;

/* Wrong */
char *a;
char * a;
```

- When declaring multiple pointer variables, you may declare them with asterix alighed to variable name
```c
/* OK */
char *p, *n;
```

# Structures and enumerations

- Structure or enumeration name must be lowercase with optional underscore `_` character between words
- Structure or enumeration may contain `typedef` keyword
- All structure members must be lowercase
- All enumeration members must be uppercase
- Declare every member in its own line, even if they share the same type, eg. do not do `int a, b`
- Structure/enumeration must follow doxygen documentation syntax

When structure is declared, it may use one of `3` different options:

1. When structure is declared with *name only*, it *must not* contain `_t` suffix after its name.
```c
struct struct_name {
    char* a;
    char b;
};
```
2. When structure is declared with *typedef only*, it *has to* contain `_t` suffix after its name.
```c
typedef struct {
    char* a;
    char b;
} struct_name_t;
```
3. When structure is declared with *name and typedef*, it *must not* contain `_t` for basic name and it *has to* contain `_t` suffix after its name for typedef part.
```c
typedef struct struct_name {
    char* a;
    char b;
    char c;
} struct_name_t;
```

Examples of bad declarations and their suggested corrections
```c
/* a and b must be separated to 2 lines */
/* Name of structure with typedef must include _t suffix */
typedef struct {
    int a, b;
} a;

/* Corrected version */
typedef struct {
    int a;
    int b;
} a_t;

/* Wrong name, it must not include _t suffix */
struct name_t {
    int a;
    int b;
};

/* Wrong parameters, must be all uppercase */
typedef enum {
    MY_ENUM_TESTA,
    my_enum_testb,
} my_enum_t;
```

# Compound statements

- Every compound statement must include opening and closing curly braces, even if there is only `1` statement
- Every compound statement must include single indent, when nesting statements, include `1` indent for each nest

```c
/* OK */
if (c) {
    do_a();
} else {
    do_b();
}

/* Wrong */
if (c)
    do_a();
else
    do_b();
    
/* Wrong */
if (c) do_a();
else do_b();
```

- In case of `if` or `if-else-if` statement, `else` must be in the same line as closing bracket of first statement
```c
/* OK */
if (a) {

} else if (b) {

} else {

}

/* Wrong */
if (a) {

} 
else {

}

/* Wrong */
if (a) {

} 
else
{

}
```

- In case of `do-while` statement, `while` part must be in the same line as closing bracket of `do` part
```c
/* OK */
do {
    int a;
    a = do_a();
    do_b(a);
} while (check());

/* Wrong */
do
{
/* ... */
} while (check());

/* Wrong */
do {
/* ... */
}
while (check());
```

- Indentation is required for every opening bracket
```c
if (a) {
    do_a();
} else {
    do_b();
    if (c) {
        do_c();
    }
}
```

- Never do compound statement without braces, even in case of single statement. Example below shows bad practice.
```c
if (a) do_b();
else do_c();
```

### Switch statement

- Make single `indent` for every case statement
```c
/* OK, every case has single indent */
switch (check()) {
    case 0:
        do_a();
        break;
    case 1:
        do_b();
        break;
    default:
        break;
}

/* Wrong, case indent missing */
switch (check()) {
case 0:
    do_a();
    break;
case 1:
    do_b();
    break;
default:
    break;
}

/* Wrong */
switch (check()) {
    case 0:
        do_a();
    break;      /* Wrong, break must have indent as it is under case */
    case 1:
    do_b();     /* Wrong, indent under case is missing */
    break;
    default:
        break;
}
```

- Always include `default` statement
```c
/* Wrong, default is missing */
switch (var) {
    case 0: 
        do_job(); 
        break;
}
```

- If local variables are required, use curly brackets and put `break` statement inside. Put curly bracket in the same line as `case` statement
```c
switch (a) {
    /* OK */
    case 0: {
        int a, b;
        char c;
        a = 5;
        /* ... */
        break;
    }
    
    /* Wrong */
    case 1:
    {
        int a;
        break;    
    }
}
```

# Documentation

Documented code allows doxygen to parse and general html/pdf/latex output, thus it is very important to do it properly.

- Use doxygen-enabled documentation style for `variables`, `functions` and `structures/enumerations`
- Always use `\` for doxygen, do not use `@`
- Always use `5x4` spaces (`5` tabs) offset from beginning of line for text
```c
/**
 * \brief           Holds pointer to first entry in linked list
 *                  Beginning of this text is 5 tabs (20 spaces) from beginning of line
 */
static type_t* list;
```

- Every structure/enumeration member must include documentation
- Use `12x4 spaces` offset for beginning of comment
```c
/**
 * \brief           This is point struct
 * \note            This structure is used to calculate all point 
 *                      related stuff
 */
typedef struct {
    int x;                                      /*!< Point X coordinate */
    int y;                                      /*!< Point Y coordinate */
    int size;                                   /*!< Point size.
                                                    Since comment is very big,
                                                    you may go to next line */
} point_t;

/**
 * \brief           Point color enumeration
 */
typedef enum {
    COLOR_RED,                                  /*!< Red color. This comment has 12x4
                                                    spaces offset from beginning of line */
    COLOR_GREEN,                                /*!< Green color */
    COLOR_BLUE,                                 /*!< Blue color */
} point_color_t;
```

- Function must include `brief` and all parameters documentation
- Every parameter must be noted if it is `in` or `out` for *input* and *output* respectively
- Function must include `return` parameter if it returns something. This does not apply for `void` functions
- Function can include other doxygen keywords, such as `note` or `warning`
- Use colon `:` between parameter name and its description
```c
/**
 * \brief           Sum `2` numbers
 * \param[in]       a: First number
 * \param[in]       b: Second number
 * \return          Sum of input values
 */
int
sum(int a, int b) {
    return a + b;
}

/**
 * \brief           Sum `2` numbers and write it to pointer
 * \note            This function does not return value, it stores it to pointer instead
 * \param[in]       a: First number
 * \param[in]       b: Second number
 * \param[out]      result: Output variable used to save result
 */
void
void_sum(int a, int b, int* result) {
    *result = a + b;
}
```

- If function returns member of enumeration, use `ref` keyword to specify which one
```c
/**
 * \brief           My enumeration
 */
typedef enum {
    MY_ERR,                                     /*!< Error value */
    MY_OK                                       /*!< OK value */
} my_enum_t;

/**
 * \brief           Check some value
 * \return          \ref MY_OK on success, member of \ref my_enum_t otherwise
 */
my_enum_t
check_value(void) {
    return MY_OK;
}
```

- Use notation (\`NULL\` => `NULL`) for constants or numbers
```c
/**
 * \brief           Get data from input array
 * \param[in]       in: Input data
 * \return          Pointer to output data on success, `NULL` otherwise
 */
const void *
get_data(const void* in) {
    return in;
}
```

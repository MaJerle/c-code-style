# C style and coding rules

This document describes C code style used by Tilen MAJERLE in his projects and libraries.

# General global rules

Here are listed most obvious and important general rules. Please check them carefully before you continue with other chapters.

- Do not use tags, use `4 spaces` per level instead
- Use `1` space between keyword and opening bracket
- Do not use space between function name and opening bracket
- Opening curly bracket is always on the same line as keyword (`for`, `while`, `do`, `switch`, `if`, ...)
- Use single space before and after comparison and assignments comparison
- Do not initialize `static` and `global` variables to `0`, compiler will do it for you
- Always respect code style already used in project or library
- Declare all local variables of the same type in the same line
- Except `char`, always use types declared in `stdint.h` library, eg. `uint8_t` for `unsigned 8-bit`, etc.
- Do not use `stdbool.h` library in any case. Use `1` or `0` for `true`or `false` respectively
- Always compare pointers against `NULL` value, eg. `if (ptr != NULL) { ... }` (or `ptr == NULL`), do not use `if (ptr) { ... }`
- Never compare against `true`, eg. `if (check_func() == 1)`, use `if (check_func()) { ... }`
- Always use `/* comment */` for comments, even when *single-line* comment
- Always include check for `C++` with `extern` keyword in header file
- Every function must include *doxygen-enabled* comment, even if function is `static`

# Comments and documentation

# Functions

- Every function which may be access from outside module, must include function *prototype* (or *declaration*)
- Function names must be lowercase, optionally separated with underscore character
- When function returns pointer, character must be left aligned without space (see example below)
- Align all function names for better readability
- Function implementation must include return type and optional other keywords in separate line

```c
/* Good declarations */

int     sum(int a, int b);
char*   get_char(void);

/* Inside module */
static int divide(int a, int b);

/* Bad declarations */

char *get_char(void);
char * get_char();
int sum(int a,int b); /* Space missing after comma */
int sum (int a, int b); /* No space between function name and opening bracket */
```
After function declaration, implement functions in module .c file

```c
/* Good implementations */

int
sum(int a, int b) {
    return a + b;
}

static int
divide(int a, int b) {
    return a + b;
}

/* Asterix is followed by space */
char *     
get_str(void) {
    return str;
}

/* Bad implementations */

int sum(int a, int b) /* Return type must be in separate line */
{   /* Curly opening bracket must be in the same line as keyword */
    return a + b;
}
int
sum(int a, int b) {
int tmp;   /* Local variables must have indent */
    tmp = a + b;
    return tmp;
}
```

# Structures and enumerations

### General rules

- Structure name must be all lowercase with underscore `_` character between words
- Structure may contain `typedef` keyword
- All structure members must be lowercase
- All enumeration members must be uppercase
- Structure/enumeration must follow doxygen documentation syntax
- Declare every member in its own line, even if they share the same type

### Declaration

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
3. When structure is declared with *name and typedef*, it *must not* container `_t` for basic name and it *has to* contain `_t` suffix after its name for typedef part.
```c
typedef struct struct_name {
    char* a;
    char b;
    char c;
} struct_name_t;
```

### Examples of bad declarations

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

### General rules

- Every compound statement must include opening and closing curly braces, even if there is only `1` statement
- In case of `if` statement, `else` must be in the same line as closing bracket of first statement
- In case of `do-while` statement, `while` part must be in the same line as closing bracket of `do` part
- The same applies for `if-else` statement
- Indentation is required for every opening bracket

Every such statement *has to* include braces.

```c
if (c) {
    do_a();
} else {
    do_b();
}
```
Or in case of `if-else` statement

```c
if (c) {
    do_a();
} else if (b) {
    do_b();
} else {
    do_c();
}
```

Or with `if-if-else` statement

```c
if (a) {
    if (b) {
        do_b();
    } else {
        do_c();
    }
}
```

Never do compound statement without braces, even in case of single statement. Example below shows bad practice.

```c
if (a) do_b();
else do_c();
```

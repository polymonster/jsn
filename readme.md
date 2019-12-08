# jsn
[![Build Status](https://travis-ci.org/polymonster/jsn.svg?branch=master)](https://travis-ci.org/polymonster/jsn) [![codecov](https://codecov.io/gh/polymonster/jsn/branch/master/graph/badge.svg)](https://codecov.io/gh/polymonster/jsn) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

jsn is a user-friendly data format that can be reliably edited by humans by addressing some of the common mistakes that occur when using standard json. 

It adds powerful features such as inheritence, variables, includes and syntax improvements to make jsn files more compact and re-usable than a json counterpart, it is an ideal solution for complex multi-platform build configuration and is currently being used in a number of personal and professional projects.

jsn can be used directly in python as a dictionary, or it can be converted to json to be used with other languages and tools and libraries which have json support.

If you are using hand edited json in any projects currently, jsn will easily integrate into your existing workflow and improve efficiency and reliability.


# Features
- Includes / file import.
- Inheritance (hierarchicle and multiple).
- Environment style scoped variables.
- Quoteless keys.
- Quoteless strings.
- Single quotes.
- Single and multi-line comments.
- Multi-line strings / line breaks.
- Hex, binary, bit shifts, int and float improvements.

# CLI

You can convert jsn to json using the commandline, clone this repository and add jsn to your path.

```
jsn -i example.jsn -o example.json
```

```
jsn -help
--------------------------------------------------------------------------------
jsn ----------------------------------------------------------------------------
--------------------------------------------------------------------------------
commandline arguments:
    -help display this message
    -i list of input files or directories to process
    -o output file or directory 
    -p print output to console 
```

# Python API

jsn can be used just like json as a python dictionary.

```python
import jsn
json_dict = jsn.loads(open("jsn_file.jsn", "r").read())
```

## Example .jsn

```c++
import import.jsn
{   
    // sytax highlights quite nicely in most editors with c or c++ syntax      
    
    // allow comments
    
    /*
    multi-
    line 
    comments
    */
    
    //        tabs and any whitespace allowed

    // compatible with json
    "json":
    {
        "bool": true,
        "int": 1,
        "float": 1.0,
        "string": "yes",
        "array": [1, 2, 3]
    },
    
    // compatible with json5
    json5:
    {
        unquoted: 'and you can quote me on that',
        single_quotes: 'I can use "double quotes" here',
        hexadecimal: 0xdecaf,
        line_breaks: "Look, Mom! No \
\\n's!",
          leading_decimal_point: .8675309, and_trailing: 8675309.,
          positive_sign: +1,
          trailing_comma: 'in objects', and_in: ['arrays',],
    },
    
    // jsn features
    jsn:
    {
        unquoted_string: without_whitespace, // cannot contain whitespace or special chars (see str_test)
        unquoted: [strings, in, arrays],
        binary_literal: 0b10011,
        bit_shifts: 1<<16 | 1<<8,
        
        // you can define variables to be re-used
        jsn_vars: 
        {
            data: "path/to/data",
            var_str: "hello",
            var_int: 10
        },
        
        // evaluate variables with ${} inside quotes..
        variable_data_path: "${data}/subdir",
        variable_int: "${var_int}",
        array_of_vars: ["${data}", "${var_str}"],
        
        // inheritance below..
        base: "foo",
        sub_object:
        {
            one: "1",
            two: "2",
            nested_var: "${var_int}", // variable comes from outer scope.
        }, // allow trailing commas
    },
    
    inheritence(jsn): // add object name to inherit inside brackets
    {        
        // inheritance adds keys from jsn object
        // ..
        
        // duplicated keys are overridden by the derived object
        base: "bar",
        
        // inheritance on sub-objects continues recursively
        sub_object:
        {
            three: "3"
            //..
        }
    },
    
    // multiple and hierarchical inheritance
    objb: { b: "b" },
    
    multiple_inheritence(inheritence, objb):
    {
        // vars can also be shadowed / overriden..
        jsn_vars: 
        {
            data: "another/path/to/data",
            var_int: 22
        },
        
        c: "c"
    },
    
    //**
    str_test: ":[{}]'+.,0b0x" // this tests ignoring special chars inside quotes
}
```

## Output json from .jsn

```json
{
    "json": {
        "bool": true,
        "int": 1,
        "float": 1.0,
        "string": "yes",
        "array": [
            1,
            2,
            3
        ]
    },
    "json5": {
        "unquoted": "and you can quote me on that",
        "single_quotes": "I can use \"doublequotes\" here",
        "hexadecimal": 912559,
        "line_breaks": "Look, Mom! No \\n's!",
        "leading_decimal_point": 0.8675309,
        "and_trailing": 8675309.0,
        "positive_sign": 1,
        "trailing_comma": "in objects",
        "and_in": [
            "arrays"
        ]
    },
    "jsn": {
        "unquoted_string": "without_whitespace",
        "unquoted": [
            "strings",
            "in",
            "arrays"
        ],
        "binary_literal": 19,
        "bit_shifts": 65792,
        "variable_data_path": "path/to/data/subdir",
        "variable_int": 10,
        "array_of_vars": [
            "path/to/data",
            "hello"
        ],
        "base": "foo",
        "sub_object": {
            "one": "1",
            "two": "2",
            "nested_var": 10
        }
    },
    "inheritence": {
        "base": "bar",
        "sub_object": {
            "three": "3",
            "one": "1",
            "two": "2",
            "nested_var": 10
        },
        "unquoted_string": "without_whitespace",
        "unquoted": [
            "strings",
            "in",
            "arrays"
        ],
        "binary_literal": 19,
        "bit_shifts": 65792,
        "variable_data_path": "path/to/data/subdir",
        "variable_int": 10,
        "array_of_vars": [
            "path/to/data",
            "hello"
        ]
    },
    "objb": {
        "b": "b"
    },
    "multiple_inheritence": {
        "c": "c",
        "base": "bar",
        "sub_object": {
            "three": "3",
            "one": "1",
            "two": "2",
            "nested_var": 22
        },
        "unquoted_string": "without_whitespace",
        "unquoted": [
            "strings",
            "in",
            "arrays"
        ],
        "binary_literal": 19,
        "bit_shifts": 65792,
        "variable_data_path": "another/path/to/data/subdir",
        "variable_int": 22,
        "array_of_vars": [
            "another/path/to/data",
            "hello"
        ],
        "b": "b"
    },
    "str_test": ":[{}]'+.,0b0x",
    "another_file": {
        "jsn": "can import content from other files"
    }
}
```


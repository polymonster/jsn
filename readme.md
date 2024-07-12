# jsn
[![tests](https://github.com/polymonster/jsn/actions/workflows/tests.yaml/badge.svg)](https://github.com/polymonster/jsn/actions/workflows/tests.yaml) 
[![build-release](https://github.com/polymonster/jsn/actions/workflows/release.yaml/badge.svg)](https://github.com/polymonster/jsn/actions/workflows/release.yaml) 
[![publish-pypi](https://github.com/polymonster/jsn/actions/workflows/pypi.yaml/badge.svg)](https://github.com/polymonster/jsn/actions/workflows/pypi.yaml) 
[![codecov](https://codecov.io/gh/polymonster/jsn/branch/master/graph/badge.svg)](https://codecov.io/gh/polymonster/jsn) 
[![PyPI Version](https://img.shields.io/pypi/v/jsn.svg)](https://pypi.org/project/jsn/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) 

jsn is a user-friendly data format that can be easily read and reliably edited by humans. 

It adds powerful features such as inheritance, variables, includes and syntax improvements to make jsn files more compact and re-usable than a json counterpart, it is an ideal solution for multi-platform build configuration, packaging and content buidling pipelines.

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
- TextMate langauge included for enhanced syntax highlighting.

# CLI

You can convert jsn to json using the commandline, clone this repository and add jsn to your path.

```
jsn -i example.jsn -o example.json -I import_dir
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
    -I list of import directories, to search for imports
    -p print output to console
    -keep_vars keep jsn_vars in the output json
```

# Python API

Install via pip:

```
python3 -m pip install jsn
```

Or alternatively copy jsn.py where you need it.

jsn can be used just like json as a python dictionary.

```python
import jsn
json_dict = jsn.loads(open("jsn_file.jsn", "r").read())
```

# Releases

You can install `jsn` as a binary release found along with this repository [here](https://github.com/polymonster/jsn/releases)

## Example .jsn

```jsonnet
import import.jsn
import test.jsn
{   
    // sytax highlights quite nicely in most editors with c or c++ syntax
    // jsonnet highlights nicely in GitHub
    // TextMate grammar included for visual studio, vscode or other compatible editors
    
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
    	// ditch the quotes and commas!
        unquoted_string: without_whitespace // cannot contain whitespace or special chars (see str_test)
        unquoted: [strings, in, arrays]
        binary_literal: 0b10011
        bit_shifts: 1<<16 | 1<<8
        
        // mixed newline and commas
        object_members_separated_by_newline: {
            no_commas: yes
            with_new_lines: "if you like"
            but: "you can", still: "use them here"
        }
        arrays_elements_separated_by_newline:[
            "no need for commas"
            "if you use newlines"
            "still", "separate", "using commas", "on the same line"
    	]

        // you can define variables to be re-used
        jsn_vars: 
        {
            data: "path/to/data"
            var_str: "hello"
            var_int: 10
        }
        
        // evaluate variables with ${} inside quotes..
        variable_data_path: "${data}/subdir"
        variable_int: "${var_int}"
        array_of_vars: ["${data}", "${var_str}"]

        // you can use special variables:
        // inject the current script directory into a string
        // - this is the directory name of the file this variable is used in
        script_directory: "${script_dir}"

        // env vars can also be injected, if no variable is found in the script jsn will fallback to check if an env var exists
        env_vars: ${OS_ENV_VAR}
        
        // subobjects can be merged and inherited recursively see ** inheritence(jsn)
        base: "foo"
        sub_object:
        {
            one: "1"
            two: "2"
            nested_var: "${var_int}" // variable comes from outer scope.
        }
        
        // use <windows, mac, linux> in angled brackets to conditionally include or exclude keys
        // the platform specific keys will be merged into the base key if one exists
        platform:
        {
            base: "exists"
        }
        
        // useful for selecting platform specific paths and executables
        platform<windows>:
        {
            exe: "path/windows/program.exe"
        }
        
        platform<mac>:
        {
            exe: "path/mac/program"
        }
    },
    
    //** 
    inheritence(jsn): // add object name to inherit inside parenthesis
    {        
        // inheritance adds keys from 'jsn' object
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
    
    xxx:
    {
        // some test cases
        empty_object: {},

        empty_array: [],

        array_of_objects:[
            {object: 1, other: "value"},
            {object: 2, other: "value"}
        ],
        
        array_with_string_commas:[
            "test,2",
            "test,3"
        ],
        
        nested_objects:
        {
            yes: true,
            and:
            {
                deeper: nesting
            }
        },
        
        multi_type_arrays:[
            1,
            [2, 3]
        ],
        
        array_of_arrays:[
            [hello, world],
            [goodbye, world]
        ],

        array_of_values:[
            +255,
            0b11111111,
            0xff,
            1 << 1,
            1 << 2 | 1,
            1 << 2 | 1,
            .255
        ],
        
        jsn_vars: 
        {
            va: "path/to/data",
            vb: "hello",
        },

        value: null,
        array_of_null: [null, null, null]
	
        array_of_array_vars: [
            ["${va}", "${vb}"],
            ["${vb}", "non var"]
        ],
        
        multiple_vars: "${va}/${vb}.bin",
        
        q1: "small 'quotes' inside",
        q2: 'double "quotes" inside',
        q3: "double escaped \"quotes\" inside"
    },
    
    //**
    str_test: ":[{}]'+.,0b0x" // this tests ignoring special chars inside quotes
}
```

# jsn

jsn is a user-friendly data format that can be edited by humans by improving some of the common mistakes that occur when using standard json. 

It can be used directly in python as a dictionary just like json, or it can be converted to json to be used with other languages and tools which already support json.

If you are using hand edited json in any projects currently, jsn will easily integrate into your workflow and make editing simple.

# Feature Summary

- quoteless keys.
- quoteless strings.
- single quotes.
- single and multi-line comments.
- includes / file import.
- inheritance (hierarchicle and multiple).
- multi-line strings / line breaks.
- hex.
- binary.
- leading and trailing decimal in floats.

# Python API

The python API mirrors json, you can use jsn just like json as a python dictionary.

```python
import jsn
json_dict = jsn.loads(open("jsn_file.jsn", "r").read())
```

# CLI

For usage in langauges other than python you can convert jsn to json using the commandline.

```
python3 jsn.py -i <list of input files or directories> -o <output file or directory>
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
    
    //		tabs and any whitespace allowed

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
        binary: 0b10011,
        binary_shift: 1<<16,
        
        // inheritance below..
        base: "foo",
        sub_object:
        {
            one: "1",
            two: "2"
        }, // allow trailing commas
    },
    
    inheritence(jsn): // add object name to inherit inside brackets
    {        
        // inheritance adds keys from jsn object
        
        // unquoted_string: without_whitespace,
        // binary: 0b10011,
        // binary_shift: 1<<16,
        
        // duplicated keys are overridden by the derived object
        base: "bar",
        
        // inheritance on sub-objects continues recursively
        sub_object:
        {
            three: "3"
            // one: "1",
            // two: "2"
        }
    },
    
    // multiple and hierarchical inheritance
    objb: { b: "b" },
    
    multiple_inheritence(inheritence, objb):
    {
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
        "binary": 19,
        "binary_shift": "1<<16",
        "base": "foo",
        "sub_object": {
            "one": "1",
            "two": "2"
        }
    },
    "inheritence": {
        "base": "bar",
        "sub_object": {
            "three": "3",
            "one": "1",
            "two": "2"
        },
        "unquoted_string": "without_whitespace",
        "binary": 19,
        "binary_shift": "1<<16"
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
            "two": "2"
        },
        "unquoted_string": "without_whitespace",
        "binary": 19,
        "binary_shift": "1<<16",
        "b": "b"
    },
    "str_test": ":[{}]'+.,0b0x",
    "another_file": {
        "jsn": "can import content from other files"
    }
}
```


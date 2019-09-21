# jsn

## Usage

Write .jsn files and convert them to json then pass the compliant json code to any other tools and languages:

```
python3 jsn.py -i <list of input files or directories> -o <output file or directory>
```

Use in python as dict just like json:

```python
import jsn.jsn as jsn
json_dict = jsn.loads(open("jsn_file.jsn", "r").read())
```

## Example .jsn

```c++
// syntax highlights nicely in most text editors with c++

{         
    // allow comments
    
    // include files (relative to current working directory)
    jsn_include: ["include_file.jsn"],
    
    // standard json
    "json":
    {
        "array": [1, 2, 3],
        "bool": true,
        "int": 0,
        "float": 1.0
    },
    
    object:
    {
        base: "foo",
        unquoted_keys: "hello",
        unquoted_strings: string,
        another: unquoted_string, // unquoted strings cannot contain whitespace
        hex: 0xff,
        
        sub_object:
        {
            one: "1",
            two: "2"
        }
    },
    
    /*
    Allow multi-line comments
    block:
    {
        key: "a",
        value: "pair"
    }
    */
    
    new_object:
    {
        // inheritance
        jsn_inherit: ["object"],
        
        base: "bar (overrides hello)",
        
        sub_object:
        {
            three: "3"
        }
        
    }, // allow trailing commas
}

```

## Output json from .jsn

```json
{
    "json": {
        "array": [
            1,
            2,
            3
        ],
        "bool": true,
        "int": 0,
        "float": 1.0
    },
    "object": {
        "base": "foo",
        "unquoted_keys": "hello",
        "unquoted_strings": "string",
        "another": "unquoted_string",
        "hex": 255,
        "sub_object": {
            "one": "1",
            "two": "2"
        }
    },
    "new_object": {
        "base": "bar(overrideshello)",
        "sub_object": {
            "three": "3",
            "one": "1",
            "two": "2"
        },
        "unquoted_keys": "hello",
        "unquoted_strings": "string",
        "another": "unquoted_string",
        "hex": 255
    }
}
```


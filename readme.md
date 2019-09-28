# jsn

Write .jsn files and jsn.py will convert them to json so you can pass the compliant json to any other tools and languages which support it:

```
python3 jsn.py -i <list of input files or directories> -o <output file or directory>
```

Use in python as dict just like json:

```python
import jsn
json_dict = jsn.loads(open("jsn_file.jsn", "r").read())
```

## Example .jsn

```c++
// syntax highlights nicely in most text editors with c++

{         
    // allow comments
    
    /*
    Allow multi-line comments
    block:
    {
        key: "a",
        vakue: "pair"
    }
    */
    
    // standard json
    "json":
    {
        "array": [1, 2, 3],
        "bool": true,
        "int": 0,
        "float": 1.0
    },
    
    // friendly jsn
    unquoted_keys:
    {
        unquoted_strings: string,
        another: unquoted_string, // unquoted strings cannot contain whitespace
        hex: 0xff,
        binary: 0b10011,
        
        // inheritance below..
        base: "foo",
        sub_object:
        {
            one: "1",
            two: "2"
        }
    },
    
    derrived_object:
    {
        // inheritance
        jsn_inherit: ["unquoted_keys"],
        
        // adds keys
        // unquoted_strings: string,
        // another: unquoted_string,
        // hex: 0xff,
        // binary: 0b10011,
        
        // overrides foo
        base: "bar",
        
        // merges sub-object
        sub_object:
        {
            three: "3"
            // one: "1",
            // two: "2"
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
    "unquoted_keys": {
        "unquoted_strings": "string",
        "another": "unquoted_string",
        "hex": 255,
        "binary": 19,
        "base": "foo",
        "sub_object": {
            "one": "1",
            "two": "2"
        }
    },
    "derrived_object": {
        "base": "bar",
        "sub_object": {
            "three": "3",
            "one": "1",
            "two": "2"
        },
        "unquoted_strings": "string",
        "another": "unquoted_string",
        "hex": 255,
        "binary": 19
    }
}
```


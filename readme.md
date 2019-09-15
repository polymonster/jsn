# jsn

A simple json like syntax that is processed and converted to compliant json through a single python script. The intention of this project is to provide a more user friendly and lenient language than json that can directly be plugged into existing languages or libraries which support fully complient json.

There are other json variants such as json5 that achieve the same goal but I wanted a simple replacement that did not require pip, jsn can be used anywhere by simply including jsn.py into your pipelines as a pre-process step and actual json is used from there on.

## Requirements

python3

## Usage

Write .jsn files and convert them to json then pass the compliant json code to any other tools and languages.

```
python3 jsn.py -i <list of input files or directories> -o <output directory>
```

## Example

```javascript
// syntax highlights nicely in most text editors with c++

{         
    // allow comments
    
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
        another: "unquoted_string", // unquoted strings cannot contain whitespace
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
        vakue: "pair"
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

## Output JSON

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


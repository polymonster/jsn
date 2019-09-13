# jsn

A simple Json like syntax that is processed and converted to compliant Json through a single python script. 

The aim of jsn is to provide a more user friendly and lenient language than Json that can directly be plugged into existing languages or libraries which support fully complient Json. Json is great but it can be at times infuritating to work with when fixing errors with trailing commas or having to contiually quote strings!

Other Json variants such as Json5 or other languages such as toml that achieve the same goal but I wanted a simple replacement that did not require pip for python and wanted to plug into all the languages, tools and apis which support Json directly, so jsn can be used anywhere by simply including jsn.py into your pipelines as a pre-process step and standard Json is used from there on..

## Requirements

python3

## Usage

Write .jsn files and convert them to json then pass the compliant json code to any other tools and languages:

```
python3 jsn.py -i <list of input files or directories> -o <output directory>
```

Convert jsn to json in a python script and pass to native python json.

```python
import jsn

standard_json = json.loads(to_json(open("file.jsn", "r").read()))

```
 
## Example jsn

```c++
// syntax highlights nicely in most text editors with c++

views:
{
    // allows comments
    
    // includes (not yet implemented)
    include: "other.jsn",
    
    main_view:
    {
        // member wise object inheritence (not yet implemented)
        inherit: ["another_key"],
        
        target             : ["main_colour", "main_depth"],
        clear_colour       : [0.0, 0.0, 0.0, 1.0],
        clear_depth        : 1.0,
        colour_write_mask  : 0xf,
        blend_state        : "disabled",
        viewport           : [0.0, 0.0, 1.0, 1.0],
        raster_state       : "default",
        depth_stencil_state: "default",
        scene              : "main_scene",
        camera             : "model_viewer_camera",
        scene_views        : ["ces_render_scene"],
        render_flags       : ["forward_lit"]

        sampler_bindings:
        [
            { texture: "shadow_map", unit: 15, state: "wrap_linear", shader: "ps" },
            { texture: "area_light_textures", unit: 11, state: clamp_linear, shader: "ps" },
        ], // allows trailing commas
    },
 }

```

# jsn

A simple json like syntax that is processed and converted to compliant json through a single python script. The intention of this project is to provide a more user friendly and lenient language than json that can directly be plugged into existing languages or libraries which support fully complient json.

There are other json variants such as json5 that achieve the same goal but I wanted a simple replacement that did not require pip, jsn can be used anywhere by simply including jsn.py into your pipelines as a pre-process step and actual json is used from there on.

## Requirements

python3

## Usage

Write .jsn files and convert them to json then pass the compliant json code to any other tools and languages.

```
python3 jsn.py -i <list of input files or directories> -o <output directory>"
```

## Example

```c++
// syntax highlights nicely in most text editors with c++

views:
{
    // allows comments
    main_view:
    {
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

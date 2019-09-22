# lightweight json format without the need for quotes, allowing comments and more
import json
import sys
import os
import traceback

# build info for jobs
class build_info:
    inputs = []
    output_dir = ""


# do c like (u32)-1
def us(v):
    if v == -1:
        return sys.maxsize
    return v


# return string inside "quotes" to make code gen cleaner
def in_quotes(string):
    if len(string) >= 2:
        if string[0] == "\"" and string[len(string)-1] == "\"":
            return string
    return '"' + string + '"'


# create a new dir if it doesnt already exist and not throw an exception
def create_dir(dst_file):
    dir = os.path.dirname(dst_file)
    if not os.path.exists(dir):
        os.makedirs(dir)


# change extension
def change_ext(file, ext):
    return os.path.splitext(file)[0] + ext


# is_file
def is_file(file):
    if len(os.path.splitext(file)[1]) > 0:
        return True
    return False


# parse command line args passed in
def parse_args():
    info = build_info()
    if len(sys.argv) == 1:
        display_help
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-i":
            j = i + 1
            while j < len(sys.argv) and sys.argv[j][0] != '-':
                info.inputs.append(sys.argv[j])
                j = j + 1
            i = j
        if sys.argv[i] == "-o":
            info.output_dir = sys.argv[i + 1]
    return info


# help
def display_help():
    print("commandline arguments:")
    print("    -help display this message")
    print("    -i list of input files or directories to process")
    print("    -o output directory")


# python json style dumps
def format(jsn, indent=4):
    nl = ["{", "[", ","]
    el = ["}", "]"]
    id = ["{", "["]
    fmt = ""
    cur_indent = 0
    for char in jsn:
        if char in el:
            fmt += "\n"
            cur_indent -= 4
            for i in range(0, cur_indent):
                fmt += " "
        fmt += char
        if char in nl:
            fmt += "\n"
            if char in id:
                cur_indent += 4
            for i in range(0, cur_indent):
                fmt += " "
        if char == ":":
            fmt += " "
    return fmt


# remove whitespace and newlines to simply subsequent ops
def clean_src(jsn):
    clean = ""
    inside_quotes = False
    for char in jsn:
        if char == '\"':
            inside_quotes = not inside_quotes
        strip_char = char.strip()
        clean += strip_char
    return clean


# remove comments, taken from polymonster/stub-format/stub_format.py ()
def remove_comments(file_data):
    lines = file_data.split("\n")
    inside_block = False
    conditioned = ""
    for line in lines:
        if inside_block:
            ecpos = line.find("*/")
            if ecpos != -1:
                inside_block = False
                line = line[ecpos+2:]
            else:
                continue
        cpos = line.find("//")
        mcpos = line.find("/*")
        if cpos != -1:
            conditioned += line[:cpos] + "\n"
        elif mcpos != -1:
            conditioned += line[:mcpos] + "\n"
            inside_block = True
        else:
            conditioned += line + "\n"
    return conditioned


# find first char in chars in string from pos
def find_first(string, pos, chars):
    first = us(-1)
    for char in chars:
        first = min(us(string.find(char, pos)), first)
    return first


# def get value type, object array
def get_value_type(value):
    value = value.strip()
    if len(value) > 0:
        if value[0] == "{":
            return "object"
        if value[0] == "[":
            return "array"
        if value == 'true' or value == 'false':
            return "bool"
        if value.find(".") != -1:
            try:
                float(value)
                return "float"
            except ValueError:
                pass
        if value.find("0x") != -1:
            try:
                int(value[2:], 16)
                return "hex"
            except ValueError:
                pass
        try:
            int(value)
            return "int"
        except ValueError:
            pass
    return "string"


# add quotes to unquoted keys
def quote_keys(jsn):
    delimiters = [",", "{"]
    pos = 0
    quoted = ""
    while True:
        cur = pos
        pos = jsn.find(":", pos)
        if pos == -1:
            quoted += jsn[cur:]
            break
        delim = 0
        for d in delimiters:
            dd = jsn[:pos].rfind(d)
            if dd != -1:
                delim = max(dd, delim)
        key = jsn[delim+1:pos].strip()
        qkey = in_quotes(key)
        quoted += jsn[cur:delim+1]
        quoted += qkey
        quoted += ":"
        pos += 1
        next = find_first(jsn, pos, [",", "]", "}"])
        value = jsn[pos:next]
        if get_value_type(value) == "string":
            value = in_quotes(value)
            quoted += value
            pos = next
        if get_value_type(value) == "hex":
            hex_value = int(value[2:], 16)
            quoted += str(hex_value)
            pos = next
    return quoted


# remove trailing commas
def remove_trailing_commas(jsn):
    trail = ["}", "]"]
    clean = ""
    for i in range(0, len(jsn)):
        j = i + 1
        char = jsn[i]
        if char == "," and j < len(jsn):
            if jsn[j] in trail:
                continue
        clean += char
    return clean


# inherit dict
def inherit_dict(dest, second):
    for k, v in second.items():
        if type(v) == dict:
            if k not in dest or type(dest[k]) != dict:
                dest[k] = dict()
            inherit_dict(dest[k], v)
        else:
            if k not in dest:
                dest[k] = v


# recursively merge dicts
def inherit_dict_recursive(d, d2):
    for k, v in d.items():
        if k == "jsn_inherit":
            if type(v) == list:
                for i in v:
                    if i in d2.keys():
                        inherit_dict(d, d2[i])
                        d.pop("jsn_inherit", None)
                        return
            else:
                print("jsn error: jsn_inherit must be an array of keys to inherit")
        if type(v) == dict:
            inherit_dict_recursive(v, d)


# add jsn includes
def add_jsn_includes(j):
    if "jsn_include" in j.keys():
        if type(j["jsn_include"]) == list:
            for i in j["jsn_include"]:
                include_dict = loads(open(i, "r").read())
                inherit_dict(j, include_dict)
        else:
            print("jsn error: jsn_include must be an array of files to include")
    return j


# convert jsn to json
def loads(jsn):
    jsn = remove_comments(jsn)
    jsn = clean_src(jsn)
    jsn = remove_trailing_commas(jsn)
    jsn = quote_keys(jsn)
    jsn = format(jsn)

    # validate
    try:
        j = json.loads(jsn)
    except:
        jsn_lines = jsn.split("\n")
        for l in range(0, len(jsn_lines)):
            print(str(l+1) + " " + jsn_lines[l])
        traceback.print_exc()
        exit(1)

    # include
    add_jsn_includes(j)

    # inherit
    inherit_dict_recursive(j, j)
    return j


# convert jsn to json and
def convert_jsn(input_file, output_file):
    print("converting: " + input_file + " to " + output_file)
    file = open(input_file, "r")
    output_file = open(output_file, "w+")
    jdict = loads(file.read())
    output_file.write(json.dumps(jdict, indent=4))
    output_file.close()
    file.close()


# output .jsn files as json,
if __name__ == "__main__":
    print("--------------------------------------------------------------------------------")
    print("jsn ----------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    info = parse_args()
    if len(info.inputs) == 0 or info.output_dir == None:
        display_help()
        exit(1)
    for i in info.inputs:
        if os.path.isdir(i):
            for root, dirs, files in os.walk(i):
                for file in files:
                    output_file = info.output_dir
                    if not is_file(output_file):
                        output_file = os.path.join(info.output_dir, file)
                        output_file = change_ext(output_file, ".json")
                        create_dir(output_file)
                    convert_jsn(os.path.join(root, file), output_file)
        else:
            output_file = info.output_dir
            if not is_file(output_file):
                output_file = os.path.join(info.output_dir, i)
                output_file = change_ext(output_file, ".json")
                create_dir(output_file)
            convert_jsn(i, output_file)
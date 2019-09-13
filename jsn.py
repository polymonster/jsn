# lightweight json format without the need for quotes, allowing comments and more
import json
import sys
import os

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
    return '"' + string + '"'


# create a new dir if it doesnt already exist and not throw an exception
def create_dir(dst_file):
    dir = os.path.dirname(dst_file)
    if not os.path.exists(dir):
        os.makedirs(dir)


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
    return quoted


# remove trailing commas
def remove_trailing_commas(jsn):
    whitespace = [" ", "\n", "\r"]
    pos = 0
    conditioned = ""
    while True:
        cur = pos
        pos = jsn.find(",", pos)
        if pos == -1:
            conditioned += jsn[cur:]
            break
        np = pos
        pos += 1
        next = " "
        while next in whitespace:
            np += 1
            next = jsn[np]
        if next == "}" or next == "]":
            conditioned += jsn[cur:pos-1]
        else:
            conditioned += jsn[cur:pos]
    return conditioned


# convert jsn to json
def to_json(jsn):
    jsn = remove_comments(jsn)
    jsn = quote_keys(jsn)
    jsn = remove_trailing_commas(jsn)
    # validate
    j = json.loads(jsn)
    fmt = json.dumps(j, indent=4)
    return fmt


# convert jsn to json and
def convert_jsn(input_file, output_file):
    print("converting: " + input_file + " to " + output_file)
    file = open(input_file, "r")
    output_file = open(output_file, "w+")
    output_file.write(to_json(file.read()))
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
            for root, dirs, files in os.walk(source):
                for file in files:
                    output_file = os.path.join(info.output_dir, file)
                    create_dir(output_file)
                    convert_jsn(os.path.join(root, file), output_file)
        else:
            output_file = os.path.join(info.output_dir, i)
            create_dir(output_file)
            convert_jsn(i, output_file)
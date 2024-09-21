
import json
import pyparsing as pp


def pp_action_remove(tokens):
    return ''

pp_remove_javascript_comment = pp.cpp_style_comment.set_parse_action(pp_action_remove)

def remove_javascript_comment(text):
    """
    移除javascript中的注释
    """
    text = pp_remove_javascript_comment.transform_string(text)
    return text


pp_semicolon = pp.Literal(';')

def pp_action_remove_semicolon(tokens):
    return '\n'


def remove_javascript_semicolon(text):
    """
    方便后续处理，将分号转成换行
    """
    text = pp_semicolon.set_parse_action(pp_action_remove_semicolon).transform_string(text)
    return text


ident = pp.Word(pp.identchars, pp.identbodychars)

pp_var_definition = (
    pp.Literal("var")
    + ident.setResultsName("name")
    + "="
    + pp.restOfLine.setResultsName("value")
)

def parse_var_definition(text):
    data = {}
    for t, _, _ in pp_var_definition.scan_string(text):
        var_name = t.name
        var_value = t.value
        data[var_name] = var_value

    return data

def load_pyvalue(data):
    new_data = {}
    for key,value in data.items():
        py_value = json.loads(value)
        new_data[key] = py_value

    return new_data


def js_file_loader(text):
    data = {}
    text = remove_javascript_comment(text)
    text = remove_javascript_semicolon(text)
    data = parse_var_definition(text)
    data = load_pyvalue(data)
    return data

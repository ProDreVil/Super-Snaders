from pathlib import Path
import ast
import operator
import re

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def load_txt(relative_path):
    file_path = PROJECT_ROOT / relative_path
    return file_path.read_text(encoding="utf-8").splitlines()

def rand_name():
    pass

def load_primary_stats():
    lines = load_txt("data/features/stats.txt")
    stats = {}
    current_section = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1]
            continue
        if current_section != "PRIMARY":
            continue
        name, remainder = line.split("<", 1)
        value, remainder = remainder.split(">", 1)
        point_value = remainder.split("{", 1)[1].split("}", 1)[0]
        stats[name.strip()] = {
            "value": value.strip(),
            "point_value": point_value.strip()
        }
    return stats

def calculate_expression(expression, variables):
    variable_names = {}
    for index, (name, value) in enumerate(variables.items()):
        placeholder = f"variable_{index}"
        expression = re.sub(rf"\b{re.escape(name)}\b", placeholder, expression)
        variable_names[placeholder] = value
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
    }
    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.Name) and node.id in variable_names:
            return variable_names[node.id]
        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            return operators[type(node.op)](evaluate(node.left), evaluate(node.right))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = evaluate(node.operand)
            return value if isinstance(node.op, ast.UAdd) else -value
        raise ValueError(f"Unsupported expression: {ast.dump(node)}")
    tree = ast.parse(expression, mode="eval")
    result = evaluate(tree.body)
    if not isinstance(result, (int, float)) or isinstance(result, bool):
        raise ValueError("Expression must produce a number.")
    return int(result) if isinstance(result, float) and result.is_integer() else result

def parse_stat_value(value, variables=None):
    value = value.strip()
    if value.startswith("`") and value.endswith("`"):
        if variables is None:
            return value
        expression = value[1:-1]
        return calculate_expression(expression, variables)
    if "/" in value:
        current, maximum = value.split("/", 1)
        return {"current": int(current), "maximum": int(maximum)}
    try:
        return int(value)
    except ValueError:
        return value
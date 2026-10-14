from pathlib import Path
import ast
import operator
import re

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))

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

def load_dice_definitions():
    lines = load_txt("data/features/dice.txt")
    dice_definitions = {}
    current_tier = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            current_tier = line[1:-1]
            continue
        if current_tier is None:
            continue
        match = re.fullmatch(
            r'(.+?)\s*\(F:\s*(\d+)~(\d+)\s*\|\s*'
            r'R:\s*(\d+)\s*MP\s*\|\s*'
            r'S:\s*(\d+)\s*MP\)\s*"(.+)"',
            line
        )
        if not match:
            raise ValueError(f"Invalid dice definition: {line}")
        name, min_face, max_face, roll_cost, shake_cost, descriptions = (match.groups())
        roll_description, shake_description = descriptions.split("||", 1)
        face_range = f"{min_face}~{max_face}"
        roll_description = roll_description.replace("`faces`", face_range)
        shake_description = shake_description.replace("`faces`", face_range)
        dice_definitions[name.strip()] = {
            "tier": current_tier,
            "faces": {"min": int(min_face), "max": int(max_face)},
            "roll_cost": int(roll_cost),
            "shake_cost": int(shake_cost),
            "descriptions": {"roll": roll_description.strip(), "shake": shake_description.strip()}
        }
    return dice_definitions

if __name__ == "__main__":
    dice = load_dice_definitions()
    for name, definition in dice.items():
        print(f"\n{name}")
        print(f"Tier: {definition['tier']}")
        print(f"Faces: {definition['faces']['min']}~{definition['faces']['max']}")
        print(f"Roll Cost: {definition['roll_cost']} MP")
        print(f"Shake Cost: {definition['shake_cost']} MP")
        print(f"Roll: {definition['descriptions']['roll']}")
        print(f"Shake: {definition['descriptions']['shake']}")
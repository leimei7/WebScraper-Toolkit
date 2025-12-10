import esprima
import escodegen


def deobfuscate_code(code):
    try:
        ast = esprima.parseScript(code)
        transformed_ast = process_control_flow_flattening(ast)
        return escodegen.generate(transformed_ast)
    except Exception as e:
        print(f"Error: {str(e)}")
        return code


def process_control_flow_flattening(ast):
    if isinstance(ast, dict):
        if ast.get('type') == 'FunctionDeclaration':
            process_function(ast)
        for key, value in ast.items():
            ast[key] = process_control_flow_flattening(value)
    elif isinstance(ast, list):
        return [process_control_flow_flattening(item) for item in ast]
    return ast


def process_function(func_ast):
    body = func_ast.get('body', {})
    if body.get('type') != 'BlockStatement':
        return

    statements = body.get('body', [])
    state_var = find_state_variable(statements)
    if not state_var:
        return

    switch_stmt = find_switch_statement(statements, state_var)
    if not switch_stmt:
        return

    state_table = build_state_table(switch_stmt, state_var)
    if not state_table:
        return

    initial_state = find_initial_state(statements, state_var)
    if initial_state is None:
        return

    new_body = reconstruct_body(state_table, initial_state)
    if new_body:
        func_ast['body']['body'] = new_body


def find_state_variable(statements):
    assignments = {}
    for stmt in statements:
        if stmt.get('type') == 'VariableDeclaration':
            for decl in stmt.get('declarations', []):
                if decl.get('id', {}).get('type') == 'Identifier':
                    var_name = decl['id']['name']
                    assignments[var_name] = assignments.get(var_name, 0) + 1
        elif stmt.get('type') == 'ExpressionStatement':
            expr = stmt.get('expression', {})
            if expr.get('type') == 'AssignmentExpression':
                left = expr.get('left', {})
                if left.get('type') == 'Identifier':
                    var_name = left['name']
                    assignments[var_name] = assignments.get(var_name, 0) + 1
    if assignments:
        return max(assignments, key=assignments.get)
    return None


def find_switch_statement(statements, state_var):
    for stmt in statements:
        if stmt.get('type') == 'WhileStatement':
            test = stmt.get('test', {})
            if test.get('type') == 'Literal' and test.get('value') is True:
                while_body = stmt.get('body', {}).get('body', [])
                for s in while_body:
                    if (s.get('type') == 'SwitchStatement' and
                            s.get('discriminant', {}).get('type') == 'Identifier' and
                            s.get('discriminant', {}).get('name') == state_var):
                        return s
    return None


def build_state_table(switch_stmt, state_var):
    state_table = {}
    for case in switch_stmt.get('cases', []):
        if case.get('test', {}).get('type') != 'Literal':
            continue

        current_state = case['test']['value']
        actions = []
        next_state = None

        for stmt in case.get('consequent', []):
            if (stmt.get('type') == 'ExpressionStatement' and
                    stmt.get('expression', {}).get('type') == 'AssignmentExpression' and
                    stmt.get('expression', {}).get('left', {}).get('type') == 'Identifier' and
                    stmt.get('expression', {}).get('left', {}).get('name') == state_var):
                right = stmt.get('expression', {}).get('right', {})
                if right.get('type') == 'Literal':
                    next_state = right['value']
            else:
                actions.append(stmt)

        if next_state is not None:
            state_table[current_state] = (actions, next_state)

    return state_table


def find_initial_state(statements, state_var):
    for stmt in statements:
        if stmt.get('type') == 'VariableDeclaration':
            for decl in stmt.get('declarations', []):
                if (decl.get('id', {}).get('name') == state_var and
                        decl.get('init', {}).get('type') == 'Literal'):
                    return decl['init']['value']
    return None


def reconstruct_body(state_table, initial_state):
    new_body = []
    current_state = initial_state
    visited = set()

    while current_state not in visited and current_state in state_table:
        visited.add(current_state)
        actions, next_state = state_table[current_state]
        new_body.extend(actions)
        current_state = next_state

    return new_body


if __name__ == "__main__":
    obfuscated_code = """
    function calculate(a, b) {
        var state = 0;
        var result;
        while (true) {
            switch (state) {
                case 0:
                    result = a;
                    state = 1;
                    break;
                case 1:
                    result += b;
                    state = 2;
                    break;
                case 2:
                    return result;
            }
        }
    }
    """

    deobfuscated_code = deobfuscate_code(obfuscated_code)
    print("去混淆后的代码:")
    print(deobfuscated_code)
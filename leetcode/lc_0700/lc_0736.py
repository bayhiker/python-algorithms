class Solution:
    def evaluate(self, expression: str) -> int:
        return self.eval_stmt(expression, {})

    def eval_stmt(self, stmt: str, variables: dict[str:int]) -> int:
        if stmt.startswith("(let "):
            stmt = stmt[5:-1]
            var_pairs = ""
            return_stmt = ""
            if stmt[-1] == ")":
                # let return value is an expression
                left_parenthesis_index = self.find_matching(stmt, ")")
                return_stmt = stmt[left_parenthesis_index : len(stmt)]
                var_pairs = stmt[0 : left_parenthesis_index - 1]
            else:
                last_space_index = stmt.rfind(" ")
                return_stmt = stmt[last_space_index + 1 : len(stmt)]
                var_pairs = stmt[0:last_space_index]
            # Parse var pairs, and store in variables
            while var_pairs:
                space_index = var_pairs.find(" ")
                var_name = var_pairs[0:space_index]
                var_pairs = var_pairs[space_index + 1 : len(var_pairs)]
                if var_pairs.startswith("("):
                    matching_index = self.find_matching(var_pairs, "(")
                    var_expr = var_pairs[0 : matching_index + 1]
                    variables[var_name] = self.eval_stmt(var_expr, variables.copy())
                    # +2 to skip space
                    var_pairs = var_pairs[matching_index + 2 : len(var_pairs)]
                else:
                    # This is not an expression, must be a simple variable name or int value
                    space_index = var_pairs.find(" ")
                    if space_index >= 0:
                        variables[var_name] = self.get_value(
                            variables, var_pairs[0:space_index]
                        )
                        var_pairs = var_pairs[space_index + 1 : len(var_pairs)]
                    else:
                        variables[var_name] = self.get_value(variables, var_pairs)
                        var_pairs = ""
            return self.eval_stmt(return_stmt, variables.copy())
        elif stmt.startswith("(mult ") or stmt.startswith("(add "):
            is_add = stmt.startswith("(add ")
            stmt = stmt[5:-1] if is_add else stmt[6:-1]
            num_1 = 0
            num_2 = 0
            if stmt[0] == "(":
                # First mult param is an expr
                right_parenthesis_index = self.find_matching(stmt, "(")
                num1_expr = stmt[0 : right_parenthesis_index + 1]
                # +2 to skip the space after )
                stmt = stmt[right_parenthesis_index + 2 : len(stmt)]
                num_1 = self.eval_stmt(num1_expr, variables.copy())
            else:
                space_index = stmt.find(" ")
                num_1 = self.get_value(variables, stmt[0:space_index])
                stmt = stmt[space_index + 1 : len(stmt)]
            if stmt[0] == "(":
                # Second mult param is an expr
                num_2 = self.eval_stmt(stmt, variables.copy())
            else:
                # Just a var name or plain int value
                num_2 = self.get_value(variables, stmt)
            return num_1 + num_2 if is_add else num_1 * num_2
        else:
            # Otherwise simple statement with one single variable or value
            return self.get_value(variables, stmt)

    def find_matching(self, s: str, to_find: str) -> int:
        if to_find == "(":
            unpaired = 0
            for i in range(len(s)):
                c = s[i]
                if c == "(":
                    unpaired += 1
                if c == ")":
                    unpaired -= 1
                if unpaired == 0:
                    return i
            raise ValueError(f"No matching {to_find} in {s}")
        elif to_find == ")":
            unpaired = 0
            for i in range(len(s) - 1, -1, -1):
                c = s[i]
                if c == ")":
                    unpaired += 1
                if c == "(":
                    unpaired -= 1
                if unpaired == 0:
                    return i
            raise ValueError(f"No matching {to_find} in {s}")
        else:
            raise ValueError(f"Invalid {to_find} to look for in {s}")

    def get_value(self, variables: dict[str:int], name_or_value: str):
        if name_or_value in variables:
            return variables[name_or_value]
        else:
            try:
                return int(name_or_value)
            except ValueError as e:
                print(f"Failed to convert !{name_or_value}! to int. {str(e)}")

s = input().strip()
stack = []  # 存储左括号类型，不存索引
temp = ""   # 先处理右括号匹配，生成中间字符串

# 第一步：遍历原字符串，处理右括号不匹配的情况
for char in s:
    if char in '([':
        stack.append(char)
        temp += char  # 左括号直接加入中间字符串
    elif char == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            temp += char  # 匹配成功，加入右括号
        else:
            temp += '()'  # 匹配失败，补充左括号+当前右括号
    elif char == ']':
        if stack and stack[-1] == '[':
            stack.pop()
            temp += char  # 匹配成功，加入右括号
        else:
            temp += '[]'  # 匹配失败，补充左中括号+当前右中括号

# 第二步：处理栈中剩余的左括号（未匹配的）
result = ""
# 先把中间字符串反转，方便从后往前补右括号
reversed_temp = temp[::-1]
# 再把栈也反转，保证补的括号顺序正确
reversed_stack = stack[::-1]

for char in reversed_temp:
    if reversed_stack and char == reversed_stack[0]:
        # 遇到未匹配的左括号，补充对应的右括号
        if char == '(':
            result += ')' + char
        else:
            result += ']' + char
        reversed_stack.pop(0)
    else:
        result += char

# 再反转回来得到最终结果
final_result = result[::-1]
print(final_result)
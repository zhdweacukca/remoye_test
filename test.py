
def add_two_numbers(a, b):
    """计算两个数的和"""
    return a + b


def get_input_and_calculate():
    """从键盘获取两个数并计算它们的和"""
    try:
        num1 = float(input("请输入第一个数: "))
        num2 = float(input("请输入第二个数: "))
        result = add_two_numbers(num1, num2)
        print(f"结果: {num1} + {num2} = {result}")
        return result
    except ValueError:
        print("错误: 请输入有效的数字")
        return None


if __name__ == "__main__":
    get_input_and_calculate()

"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

import string, random

class Activation_code(object):
    def __init__(self, select: str) -> None:
        """:param select: 从传入的字符串或列表中产生验证码"""
        self._select = select

    def generate(self,length: int) -> str:
        """生成单个验证码
        :param length: 需要产生的验证码长度
        :return 返回验证码字符串
        """
        self._code = ""
        for _ in range(length):
            self._code += random.choice(self._select)
        return self._code

    def generate_mul(self, length: int, sum: int = 1) -> list:
        """生成多个验证码
        :param length: 需要产生的验证码长度
        :param sum: 需要产生的验证码数量
        :return 返回所有的验证码列表
        """
        self._code_list = []
        for _ in range(sum):
            self._code_list.append(self.generate(length))
        return self._code_list


def main():
    # 传入所有字母和数字
    code = Activation_code(string.ascii_letters + string.digits)
    # 用 \n 分割验证码列表并输出
    print("\n".join(code.generate_mul(20, 200)))

if __name__ == "__main__":
    main()

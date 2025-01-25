def interpret(command):
    com1 = command.replace('()', 'o') # 字符串replace后必须重新赋值
    com2 = com1.replace('(al)', 'al')
    return com2


if __name__ == '__main__':
    command = "G()(al)"
    com = interpret(command)
    print(com)
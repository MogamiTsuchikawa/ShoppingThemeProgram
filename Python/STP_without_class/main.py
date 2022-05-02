item_names = []
item_values = []
item_counts = []
flag = True
while flag:
    cmd = input('STP>')
    cmds = cmd.split(' ')
    if cmds[0] == 'exit':
        flag = False
    if cmds[0] == 'add':
        name = cmds[1]
        value = int(cmds[2])
        item_names.append(name)
        item_values.append(value)
        item_counts.append(0)
        print(f'{value}円の{name}を登録しました')
    if cmds[0] == 'show':
        for i in range(len(item_names)):
            print(f'{i}:{item_names[i]}:{item_values[i]}円')
    if cmds[0] == 'buy':
        target_index = int(cmds[1])
        item_counts[target_index] += 1
        print(f'{item_names[target_index]}を購入しました')
    if cmds[0] == 'checkout':
        total = 0
        for i in range(len(item_names)):
            total += item_values[i] * item_counts[i]
            print(f'{item_names[i]} {item_values[i]}円×{item_counts[i]}')
            item_counts[i] = 0
        print(f'合計金額:{total}円')

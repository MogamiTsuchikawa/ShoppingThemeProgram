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
        print('{}円の{}を登録しました'.format(value, name))
    if cmds[0] == 'show':
        for i in range(len(item_names)):
            print('{}:{}:{}円'.format(i, item_names[i], item_values[i]))
    if cmds[0] == 'buy':
        target_index = int(cmds[1])
        item_counts[target_index] += 1
        print('{}を購入しました'.format(item_names[target_index]))
    if cmds[0] == 'checkout':
        sum = 0
        for i in range(len(item_names)):
            sum += item_values[i] * item_counts[i]
            print('{} {}円×{}'.format(item_names[i], item_values[i], item_counts[i]))
            item_counts[i] = 0
        print('合計金額:{}円'.format(sum))

import json
import random

title_ele = [
    '美味',
    '快手',
    '高压锅',
    '简易',
    '新手版',
    '爸爸的',
    '超嫩',
    '中医经典食补：',
    '零失败',
    '美容养颜',
    '懒人版',
]

prepare_op = [
    '提前洗净浸泡',
    '切块',
    '切片',
    '切丝',
    '切末',
    '切成小段',
    '去皮',
    '焯好水控干水分',
    '加一点料酒，腌制30分钟',
    '加少许白醋浸泡3分钟',
    '抹上少许盐',
]

add_op = [
    '放入',
    '加一勺',
    '裹上',
    '倒入',
]

cook_op = [
    '翻炒1分钟',
    '下油锅小火炸至金黄酥脆',
    '等水中放少许盐和食用油,放入锅中滚30秒',
    '煸炒半分钟',
    '煎成两面金黄',
    '搅拌均匀',
    '加入热水，然后全部倒入高压锅，上汽吹六七分钟关火等它自然降压',
]

end_op = [
    '改大火勾芡,装盘出锅',
    '这样就做好啦',
    '加少许盐，等待收汁装盘即可',
    '鲜，甜，嫩！',
    '隔壁家的小孩都馋哭了',
    '放入速冻箱，冷藏后口感更佳',
    '啊，好吃～～～',
]


def gen_menu():
    with open('ins.json', 'r') as f:
        data = json.loads(f.read())
    ins = random.choice(data)

    title = random.choice(title_ele)
    for i in range(random.randint(1, 2)):
        title += random.choice(list(ins.keys()))
    print('菜名：', title)

    print('用料:')
    for k, v in ins.items():
        print(k, v)

    print('第一步:')
    step = ''
    for i in range(random.randint(2, 5)):
        op = prepare_op[random.randint(0, len(prepare_op) - 1)]
        step += random.choice(list(ins.keys())) + op + ','
    print(step)

    print('第二步:')
    step = random.choice(list(ins.keys())) + random.choice(cook_op) + ','
    for i in range(random.randint(2, 5)):
        op = add_op[random.randint(0, len(add_op) - 1)]
        ins_key = random.choice(list(ins.keys()))
        step += op + ins_key + ins[ins_key] + ','
    print(step)

    print('第三步:')
    print(random.choice(end_op))


if __name__ == '__main__':
    gen_menu()

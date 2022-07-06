#!/usr/bin/python3
# @File: demo01.py
# --coding: utf-8--
# @Author: 昊昊反思
# @Time: 2022年 03月 24日 09:25
"""
说明:
"""
import pandas as pd
import matplotlib.pyplot as plt

def main():
    get_shuju()


def get_shuju():
    df = pd.DataFrame(pd.read_excel('test02shuju.xlsx', index_col=0))
    su = df[["技", "器", "控", "灵", "超", "玄"]]
    # 求均值和能力总和
    df["能"] = su.sum(axis=1)
    df["均"] = su.mean(axis=1)
    # 将更新后的数据写入csv文件
    write_csv(df)
    # 查找“均”大于50的编号和名并输出
    var = df[50 < df.均]["名"]
    print(var)
    # 查找“命”等于“死”的编号和名并输出
    var = df[df.命 == "死"]["名"]
    print(var)
    # 按照“能”降序输出
    df.sort_values(by="能",inplace=True, ascending=False)
    print(df)
    # 绘制六种能力的箱线图
    xiangxiantu(df)
    # 六种能力的柱状图
    zhuzhuangtu(df)
    # 性别分布的扇形图
    shanxingtu(df)
    # 原图中各种能力的折线图
    zhexiantu(df)


def zhexiantu(df):
    box_1, box_2, box_3, box_4 , box_5, box_6 = df.loc[:, '技'], df.loc[:, '器'], df.loc[:, '控'], df.loc[:, '灵'], df.loc[:, '超'], df.loc[:, '玄']
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
    plt.figure(figsize=(15, 8), dpi=80)

    plt.plot(range(len(box_1)), box_1, label='技', color="r")
    plt.plot(range(len(box_2)), box_2, label='器', color="b")
    plt.plot(range(len(box_3)), box_3, label='控', color="y")
    plt.plot(range(len(box_4)), box_4, label='灵', color="g")
    plt.plot(range(len(box_5)), box_5, label='超')
    plt.plot(range(len(box_6)), box_6, label='玄')

    # 设置x,y坐标
    plt.xticks(range(1,len(box_1)+1))
    plt.yticks(range(10))
    # 设置网格线
    plt.grid(alpha=0.2)
    plt.legend(loc="upper left")
    plt.title('收益周周乐开奖折线图')
    plt.show()


def shanxingtu(df):
    plt.axis('equal')
    plt.title("性别统计", fontproperties='KaiTi', fontsize=30, color="red")  # 添加图名
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
    labels = "雄", "雌", "其他"
    man = 0
    woman = 0
    other = 0
    for x in df["性别"]:
        if x == "雄":
            man += 1
        elif x == "雌":
            woman += 1
        else:
            other += 1
    size = [man,woman,other]
    plt.pie(size,  # 加载绘图数据
            labels=labels,  # 各球队标签
            radius=1.2,  # 设置饼图半径
            counterclock=False,  # 设置为顺时针方向开始绘图
            labeldistance=1.1,  # 设置标签位置
            autopct='%.2f%%',  # 设置百分比格式，这里保存两位小数
            textprops={'fontsize': 12, 'color': 'black'},  # 设置文本属性,字体大小为12，颜色为黑
            wedgeprops={'linewidth': 0.7, 'edgecolor': 'black'},  # 设置边框，宽度为0.7，颜色为黑
            shadow=True,  # 添加阴影
            startangle=90  # 设置开始绘图的角度
            )
    plt.show()


def zhuzhuangtu(df):
    df.plot(kind='bar',width = 1)  # 柱状图
    plt.figure(figsize=(13, 6))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
    plt.rcParams["font.size"] = 10  # 设置字体大小
    plt.show()


# 箱型图查询
def xiangxiantu(df):
    df.plot(color='r', kind='bar')  # 柱状图
    box_1, box_2, box_3, box_4 , box_5, box_6 = df['技'], df['器'], df['控'], df['灵'], df['超'], df['玄']
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
    plt.rcParams["font.size"] = 10  # 设置字体大小
    plt.title('能力', fontsize=20)  # 标题，并设定字号大小
    labels = '技', '器', '控', '灵', '超', '玄'  # 图例
    plt.boxplot([box_1, box_2, box_3, box_4, box_5, box_6], labels=labels)  # grid=False：代表不显示背景中的网格线
    # data.boxplot()#画箱型图的另一种方法，参数较少，而且只接受dataframe，不常用
    plt.show()



def write_csv(df):
    df.to_csv("./害羞.csv")

if __name__ == "__main__":
    main()

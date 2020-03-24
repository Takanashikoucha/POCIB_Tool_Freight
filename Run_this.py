# -*- coding: UTF-8 -*-
# @LastAuthor: TakanashiKoucha
# @Date: 2020-03-23 08:38:59
import os
import time

print('''
欢迎使用TakanashiKoucha开发的小工具。
预算只包括采购费用不包括运费。
只支持整装不支持散装。
按ctrl+c可退出！
''')
try:
    print("---------------------- 开始初始化配置")
    all_money = input("你可用于交易的预算是：  ")
    price_20GP = input("20GP的运费单价是：    ")
    price_40GP = input("40GP的运费单价是：    ")
    price_40HQ = input("40HQ的运费单价是：    ")
    price_20GP_C = input("20GP_C的运费单价是：  ")
    price_40GP_C = input("40GP_C的运费单价是：  ")
    price_40HQ_C = input("40HQ_C的运费单价是：  ")
    print("---------------------- 初始化配置结束")
except:
    print("检测到异常，正在退出")
    time.sleep(1)
    os._exit(0)

w_limit_20GP = 25
s_limit_20GP = 33
w_limit_40GP = 29
s_limit_40GP = 67
w_limit_40HQ = 29
s_limit_40HQ = 76
w_limit_20GP_C = 21
s_limit_20GP_C = 27
w_limit_40GP_C = 26
s_limit_40GP_C = 58
w_limit_40HQ_C = 26
s_limit_40HQ_C = 66


def output(name, token, p, p_size):
    p_size = float(p_size)
    i_all_money = float(all_money)
    print(name, round(token, 2), round(token * p, 2), round(p_size / token, 2),
          i_all_money // (token * p), i_all_money // (token * p) * p_size)


def do(price, rate, mao, tiji):
    a = w_limit_20GP // mao * rate
    b = w_limit_40GP // mao * rate
    c = w_limit_40HQ // mao * rate
    d = w_limit_20GP_C // mao * rate
    e = w_limit_40GP_C // mao * rate
    f = w_limit_40HQ_C // mao * rate
    g = s_limit_20GP // tiji * rate
    h = s_limit_40GP // tiji * rate
    i = s_limit_40HQ // tiji * rate
    j = s_limit_20GP_C // tiji * rate
    k = s_limit_40GP_C // tiji * rate
    l = s_limit_40HQ_C // tiji * rate
    print("请从下面自行选择合适的货柜（体积/重量,干/冷）")
    print("每行的含义如下：")
    print("开头w为按重量s为按体积带C为冷藏/一柜可以装几个/一柜收购价多少钱/平均一个多少钱运费/预算最多能几箱/总共运费多少")
    output("w-20GP", a, price, price_20GP)
    output("w-40GP", b, price, price_40GP)
    output("w-40HQ", c, price, price_40HQ)
    output("w-20GP_C", d, price, price_20GP_C)
    output("w-40GP_C", e, price, price_40GP_C)
    output("w-40HQ_C", f, price, price_40HQ_C)
    output("s-20GP", g, price, price_20GP)
    output("s-40GP", h, price, price_40GP)
    output("s-40HQ", i, price, price_40HQ)
    output("s-20GP_C", j, price, price_20GP_C)
    output("s-40GP_C", k, price, price_40GP_C)
    output("s-40HQ_C", l, price, price_40HQ_C)


def Do():
    os.system("cls")
    print("---------------------- 开始优化运费")
    price = input("请输入采购单价：  ")
    rate = input("请输入1包装单位等于多少销售单位：  ")
    mao = input("请输入包装单位毛重：  ")
    tiji = input("请输入包装单位体积：  ")
    do(float(price), float(rate), float(mao), float(tiji))
    input()


if __name__ == "__main__":
    while True:
        try:
            Do()
        except:
            print("检测到异常，正在退出")
            time.sleep(1)
            os._exit(0)

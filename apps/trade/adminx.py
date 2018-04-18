# -*- coding:utf-8 -*-
__author__ = 'cao.yh'
__date__ = '2018/3/28 下午6:05'

import xadmin
from .models import ShoppingCar, OrderInfo, OrderGoods


class ShoppingCarAdmin(object):
    list_display = ["user", "goods", "nums", ]


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn", "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


xadmin.site.register(ShoppingCar, ShoppingCarAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
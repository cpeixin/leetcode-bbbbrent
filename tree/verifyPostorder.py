#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/1 10:01 下午
# @Author  : CongPeiXin
# @Email   : congpeixin@dongqiudi.com
# @File    : verifyPostorder.py
# @Description:
class Solution:
    def verifyPostorder(postorder):
        if not postorder: return False

        root = postorder[-1]
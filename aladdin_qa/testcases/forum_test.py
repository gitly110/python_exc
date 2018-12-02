# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/24
from service import forum
"""
测试自动化脚本
"""
class TestForum:
    def test_create_topic(self):
        result = forum.create_a_topic(1623375237, 1015964, "test by syy1")
        assert result == 200

    def test_delete_topic(self):
        result = forum.delete_a_topic(1623375237, 1015964, 865)
        assert result == 200
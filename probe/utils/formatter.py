# -*- coding: utf-8 -*-

"""
@summary: HTML文本处理模块, 提供通用的文本处理方法
"""

import re

# html中可能出现的空格的正则表达式，有中文符号时必须是Unicode字符串：编码问题
# ----------------------空格正则--------------------#
HTML_SPACE = u"(\s|　| ){2,}"  # 空格正则表达式 连续两个或以上的空格才会被去掉
# 除了<p><table><tbody><th><tr><td><tfoot>及其关闭标签和<br><img>外所有标签
HTML_TAG = "<[^tbi/][^>]+?>|</[^t][^>]+?>|<[^p]>|</[^p]>|<b[^r][^>]*?>|<i[^m][^>]+?>"

class HtmlFormatter(object):

    @staticmethod
    def format_content(content):
        """
        @summary: HTML文本处理类
        @param content: str类型, html本文
        @return: 格式化正文, 无法格式化则返回None
        """
        content = re.sub("<style[\s\S]*?</style>", "", content)  # 去掉<style>标签
        content = re.sub("<script[\s\S]*?</script>", "", content)  # 去掉<script>标签
        content = re.sub("<!--[\s\S]*?-->", "", content)  # 去掉注释
        content = re.sub(HTML_SPACE, "", content)  # 去掉空格(包含回车)
        content = re.sub("^[^>]*?>", "", content)
        content = re.sub("<[^<]*?$", "", content)  # 去掉开头结尾的<div>和</div>
        content = re.sub("<div", "<p", content)
        content = re.sub("<span", "<p", content)   # 有的用span标签来对文字编辑，替换为<p>标签
        content = re.sub("</span>", "</p>", content)
        content = re.sub("<a[\s\S]*?>", "", content)  # 去掉<a>标签
        content = re.sub("</a>", "", content)  # 去掉</a>标签
        content = re.sub("</div>", "</p>", content)  # <div>转为<p>

        content = re.sub("<table[^>]*?>", "<table>", content)  # 去掉<table>标签的属性
        content = re.sub("<tbody[^>]*?>", "<tbody>", content)  # 去掉<tbody>标签的属性
        content = re.sub("<th[^>]*?>", "<th>", content)  # 去掉<th>标签的属性
        content = re.sub("<tr[^>]*?>", "<tr>", content)  # 去掉<tr>标签的属性
        content = re.sub("<td[^>]*?>", "<td>", content)  # 去掉<td>标签的属性
        content = re.sub("<tfoot[^>]*?>", "<tfoot>", content)  # 去掉<tfooot>标签的属性
        content = re.sub("<p[^>]*?>", "<p>", content)  # 去掉<p>标签的属性
        content = re.sub("<br[^>]*?>", "<br>", content)  # 去掉<br>标签的属性
        content = re.sub(HTML_TAG, "", content)  # 去掉其他标签
        content = re.sub("<p><p><p>|<p><p>", "<p>", content)  # 去掉重复的<p>标签
        content = re.sub("</p></p></p>|</p></p>", "</p>", content)  # 去掉重复的</p>标签
        content = re.sub("<p></p>", "", content)
        return "<div>"+content+"</div>"

    @staticmethod
    def format_content_tencent_json(content):
        """
        @summary: 腾讯财经解析ajax得到json格式的网页内容
        @param content: list类型, list里是dict类型
        @return: 格式化的html, 无法格式化则返回None
        """
        info = ''
        for i in content:
            if i['type'] == 'img_url':
                info += '<p>' + '<img src="'+ i['img_url'] + '" />' + '</p>'
            elif i['type'] == 'cnt_article':
                info += '<p>' + i['desc'] + '</p>'
        return "<div>"+info+"</div>"

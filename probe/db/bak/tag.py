# -*- coding: UTF-8 -*-

class Tag(object):
    """
    @summary: 标签对象
    """
    def __init__(self, name):
        self.__name = name              # 标签名称
    def get_name(self):
        return self.__name


class TagRelation(object):
   """
   @summary: 标签关系
   """
   def __init__(self, parent_id, child_id):
       self.__parent_id = parent_id     # 父亲节点 标签id
       self.__child_id = child_id       # 孩子节点 标签id
   def get_parent_id(self):
       return self.__parent_id
   def get_child_id(self):
       return self.__child_id


class TagMap(object):
   """
   @summary: 资讯标签映射关系
   """
   def __init__(self, info_id, tag_id):
       self.__info_id = info_id         # 资讯id
       self.__tag_id = tag_id           # 标签id
   def get_info_id(self):
       return self.__info_id
   def get_tag_id(self):
       return self.__tag_id

# -*- coding: utf-8 -*-

class Stock(object):
    """
    @summary: 股票基本信息
    """
    def __init__(self,full_code,code,name,acronym,market,totals,outstanding,total_assets,liquid_assets,fixed_assets,pd,reps,eps,bvps,reserved,crps,listed_date):
        self.__full_code=full_code          # 完整股票代码
        self.__code=code                    # 股票代码
        self.__name=name                    # 股票名称
        self.__acronym=acronym              # 股票简写
        self.__market=market                # 市场
        self.__totals=totals                # 总股本(万股)
        self.__outstanding=outstanding      # 流通股本(万股)
        self.__total_assets=total_assets    # 总资产(万元)
        self.__liquid_assets=liquid_assets  # 流动资产(万元)
        self.__fixed_assets=fixed_assets    # 固定资产(万元)
        self.__pd=pd                        # 市净率
        self.__reps=reps                    # 近12个月每股收益 
        self.__eps=eps                      # 每股收益
        self.__bvps=bvps                    # 每股净资产
        self.__reserved=reserved            # 公积金
        self.__crps=crps                    # 每股公积金
        self.__listed_date=listed_date      # 上市日期
    def get_full_code(self):
        return self.__full_code
    def get_code(self):
        return self.__code
    def get_name(self):
        return self.__name
    def get_acronym(self):
        return self.__acronym
    def get_market(self):
        return self.__market
    def get_totals(self):
        return self.__totals
    def get_outstanding(self):
        return self.__outstanding
    def get_total_assets(self):
        return self.__total_assets
    def get_liquid_assets(self):
        return self.__liquid_assets
    def get_fixed_assets(self):
        return self.__fixed_assets
    def get_pd(self):
        return self.__pd
    def get_reps(self):
        return self.__reps
    def get_eps(self):
        return self.__eps
    def get_bvps(self):
        return self.__bvps
    def get_reserved(self):
        return self.__reserved
    def get_crps(self):
        return self.__crps
    def get_listed_date(self):
        return self.__listed_date


class StockResearch(object):
    # 表单信息
    table = 'stock_research'  
    columns = ['title','digest','content','publish_time','stock_id','source_website','source_url','crawl_website','crawl_url','attachment_url','author','institution','grade']
    
    """ 
    @summary: 研报资讯 
    """
    def __init__(self, title, digest, content, publish_time, stock_id, source_website, source_url, crawl_website, crawl_url, attachment_url, author, institution, grade):
        self.__title = title                    #  标题
        self.__digest = digest                  #  摘要
        self.__content = content                #  正文
        self.__publish_time = publish_time      #  发布时间
        self.__stock_id = stock_id              #  股票id
        self.__source_website = source_website  #  发布资讯发布源
        self.__source_url = source_url          #  发布资讯的源URL
        self.__crawl_website = crawl_website    #  抓取资讯的网站名
        self.__crawl_url = crawl_url            #  抓取资讯的URL
        self.__attachment_url = attachment_url  #  附件URL
        self.__author = author                  #  作者
        self.__institution = institution        #  机构名称
        self.__grade = grade                    #  评级
    def get_title(self):
        return self.__title
    def get_digest(self):
        return self.__digest
    def get_content(self):
        return self.__content
    def get_publish_time(self):
        return self.__publish_time
    def get_stock_id(self):
        return self.__stock_id
    def get_source_website(self):
        return self.__source_website
    def get_source_url(self):
        return self.__source_url
    def get_crawl_website(self):
        return self.__crawl_website
    def get_crawl_url(self):
        return self.__crawl_url
    def get_attachment_url(self):
        return self.__attachment_url
    def get_author(self):
        return self.__author
    def get_institution(self):
        return self.__institution
    def get_grade(self):
        return self.__grade

    @staticmethod
    def toObject(data):
        return StockNotice(data['title'],data['digest'],data['content'],data['publish_time'],data['stock_id'],data['source_website'],data['source_url'],data['crawl_website'],data['crawl_url'],data['attachment_url'],data['author'],data['institution'],data['grade'])


class StockNotice(object):

    # 表单信息
    table = 'stock_notice'
    columns = ['title','digest','content','publish_time','stock_id','source_website','source_url','crawl_website','crawl_url','attachment_url']

    """
    @summary: 公告资讯 
    """
    def __init__(self, title, digest, content, publish_time, stock_id, source_website, source_url, crawl_website, crawl_url, attachment_url):
        self.__title = title                    #  标题
        self.__digest = digest                  #  摘要
        self.__content = content                #  正文
        self.__publish_time = publish_time      #  发布时间
        self.__stock_id = stock_id              #  股票id
        self.__source_website = source_website  #  发布资讯发布源
        self.__source_url = source_url          #  发布资讯的源URL
        self.__crawl_website = crawl_website    #  抓取资讯的网站名
        self.__crawl_url = crawl_url            #  抓取资讯的URL
        self.__attachment_url = attachment_url  #  附件URL
    def get_title(self):
        return self.__title
    def get_digest(self):
        return self.__digest
    def get_content(self):
        return self.__content
    def get_publish_time(self):
        return self.__publish_time
    def get_stock_id(self):
        return self.__stock_id
    def get_source_website(self):
        return self.__source_website
    def get_source_url(self):
        return self.__source_url
    def get_crawl_website(self):
        return self.__crawl_website
    def get_crawl_url(self):
        return self.__crawl_url
    def get_attachment_url(self):
        return self.__attachment_url

    @staticmethod
    def toObject(data):
        return StockNotice(data['title'],data['digest'],data['content'],data['publish_time'],data['stock_id'],data['source_website'],data['source_url'],data['crawl_website'],data['crawl_url'],data['attachment_url'])

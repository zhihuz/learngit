# -*- coding: utf-8 -*-

from probe.db.service.StockDB import requestStocks
#from probe.crawler.configs.solar import
from probe.crawler.configs.auto import auto360, autohome, caam, chinaev
from probe.crawler.configs.stock import eastmoney_news, sina, netease, eastmoney_research, cninfo, tencent

contents = {'EastmoneyNews':eastmoney_news, 'SinaNews':sina, 'NeteaseNews':netease, 'TencentNews':tencent, 'EastmoneyResearch':eastmoney_research, 'CninfoNotice':cninfo, 'Autohome':autohome, 'Auto360':auto360, 'Caam':caam, 'Chinaev':chinaev}

stock_spiders = ['EastmoneyNews', 'SinaNews', 'NeteaseNews', 'TencentNews', 'EastmoneyResearch', 'CninfoNotice']

def make_configs(spider):
    config = {'source_name':contents[spider].source_name}
    configs = {'spider_name':spider, 'config':config}
    #configs = {'spider_name':spider, 'source_name':contents[spider].source_name} 
    if spider in stock_spiders:
        config['entrance'] = ['000001.SZ', '600000.SH']#[str(stk['full_code']) for stk in requestStocks(stypes=['上证A','深证A'], attributes=['full_code'])]
        config['base_url'] = contents[spider].entrance
        config['keyword'] = contents[spider].keyword
        if spider == 'EastmoneyNews':
            config['search_url'] = contents[spider].search_url
        if spider == 'EastmoneyResearch':
            config['report_url'] = contents[spider].report_url
        return configs
    config['entrance'] = contents[spider].entrance
    return configs


if __name__=='__main__':
    for spider in ['EastmoneyNews', 'SinaNews', 'NeteaseNews', 'TencentNews', 'EastmoneyResearch', 'CninfoNotice', 'Autohome', 'Auto360', 'Caam', 'Chinaev']:
        configs = make_configs(spider)
        print configs


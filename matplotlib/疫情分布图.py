from pyecharts.charts import Map
from pyecharts import options as opts

province_list=["湖北","浙江","广东","河南","湖南","江西","安徽","重庆","山东","四川","江苏","上海","北京","福建","广西","陕西","河北","云南",
               "黑龙江","海南","辽宁","山西","天津","甘肃","宁夏","内蒙古","新疆","贵州","吉林","香港","台湾","青海","澳门","西藏"]
province_value=[5806,537,393,352,332,240,237,206,178,177,168,128,121,101,87,87,82,76,59,50,45,39,32,29,21,20,17,15,14,12,9,8,7,1]
province_info=[[province_list[i],province_value[i]] for i in range(len(province_list))]
china_map=Map()
china_map.set_global_opts(title_opts=opts.TitleOpts(title="2020年1月31日全国疫情数据统计"),visualmap_opts=opts.VisualMapOpts(max_=200))
china_map.add("2020年1月31日全国疫情数据统计",province_info,maptype="china")
china_map.render('map1.html')
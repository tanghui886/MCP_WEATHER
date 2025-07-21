from spider.get_city_list import get_city_list
from spider.get_weather_by_cityId import get_weather_by_cityId

def get_weather(input_str:str)->str:
    # 清洗输入：去除"市"、"区"，分割城市和区
    city,district=input_str.replace("市","").replace("区","").split()
    data = get_city_list()
    result=[item for item in data
            if item['city_cn'] == city
            and item['district_cn'] == district]
    if result:
        return get_weather_by_cityId(result[0]['city_id'])
    else:
        return ''

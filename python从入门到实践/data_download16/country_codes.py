from pygal_maps_world.i18n import COUNTRIES


# 返回指定国家的国别码
def get_country_codes(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
            # 如果没有找到指定国家，就返回None
    return None


# print(get_country_codes('China'))

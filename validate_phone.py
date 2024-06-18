from dadata import Dadata

token = "c5b835a64a4eec3d0c28810210dbb2cfa0f465ae"
secret = "ee5573db0f4aaf049a440830c6d91cae67ed21a7"

with Dadata(token, secret) as dadata:
    # d_t = dadata.clean(name="phone", source="91790300501")
    # d_t = dadata.clean("phone", "раб.: 8(843)264-73-00")
    # d_ad = dadata.clean(name="address", source="куюки полевая 13а")
    # d_p = dadata.clean(name="passport", source="92 05 849819")
    d_e = dadata.clean(name="email", source="Dfdss@mail.ru")
    d_e2 = dadata.suggest(name="email", query="Dfdss@")
    stat_day = dadata.get_daily_stats()
    # print(d_t)
    # print(d_ad)
    # print(d_p)
    print(d_e)
    print(d_e2)
    print(stat_day)

# dadata = Dadata(token, secret)
# ...
# dadata.close()



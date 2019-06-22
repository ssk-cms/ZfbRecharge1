
from pyecharts import Geo


data = [('广州', 45), ('漳州', 35), ('A市', 43)]
geo = Geo("全国主要城市空气质量", "data from pm2.5")
attr, value = geo.cast(data)
geo.add_coordinate('A市', 119.3, 26.08) # 添加 pyecharts 未提供的城市地理坐标
geo.add(
    "全国主要城市空气质量",
    attr,
    value,
    type="effectScatter",
    is_random=True,
    is_visualmap=True,
    is_piecewise=True,
    visual_text_color="#fff",
    pieces=[
        {"min": 0, "max": 13, "label": "0 < x < 13"},
        {"min": 14, "max": 16, "label": "14 < x < 16"},
    ],
    effect_scale=5,
)
geo.render()
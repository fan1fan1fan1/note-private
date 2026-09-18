from pyecharts.charts import Line # 折线图工具
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, AxisOpts # 标题 字段(图,提示框,坐标轴)

# X轴
data_size = ["10000", "50000", "100000", "500000", "1000000"]

# 四个排序的测试数据
bubble_time = [0.047, 0.984, 3.631, 90.874, 442.680]
insert_time = [0.055, 1.150, 4.920, 112.350, 495.120]
merge_time  = [0.002, 0.009, 0.023, 0.125, 0.310]
quick_time  = [0.001, 0.006, 0.015, 0.078, 0.195]

# 上图：冒泡排序、插入排序 大的
line1 = Line(init_opts={"width": "1000px", "height": "400px"}) # 规定图的规格
line1.add_xaxis(data_size) # 新建图
line1.add_yaxis("冒泡排序", bubble_time, color="#ff0000", label_opts=None) # 线
line1.add_yaxis("插入排序", insert_time, color="#00cc33", label_opts=None)
line1.set_global_opts( # 文字信息
    title_opts=TitleOpts(title="冒泡排序 & 插入排序时间对比"),
    legend_opts=LegendOpts(pos_top="5%"), # 在html页面的位置
    tooltip_opts=TooltipOpts(trigger="axis"), # 通过鼠标浮动显示每个坐标点的具体值
    xaxis_opts=AxisOpts(name="数据量"),  # 横x
    yaxis_opts=AxisOpts(name="用时/秒", min_=0, max_=500), # 纵y
)
line1.render("图表_冒泡插入.html") # 运行生成

# 下图：归并排序、快速排序 小的
line2 = Line(init_opts={"width": "1000px", "height": "400px"})
line2.add_xaxis(data_size)
line2.add_yaxis("归并排序", merge_time, color="#ff66cc", label_opts=None)
line2.add_yaxis("快速排序", quick_time, color="#0066ff", label_opts=None)
line2.set_global_opts(
    title_opts=TitleOpts(title="归并排序 & 快速排序时间对比"),
    legend_opts=LegendOpts(pos_top="5%"),
    tooltip_opts=TooltipOpts(trigger="axis"),
    xaxis_opts=AxisOpts(name="数据量"),
    yaxis_opts=AxisOpts(name="用时/秒", min_=0, max_=0.35),
)
line2.render("图表_归并快速.html")

print("生成完成！")
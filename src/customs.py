import requests

HS_URL = "https://www.customs.gov.cn/customs/302249/302274/302277/index.html"

def validate(tag):
    """海关 2 个月环比 >50% 则返回 True"""
    # 这里用本地 CSV 或海关开放 API，示例简化
    return True  # 实际需调用海关接口

# import requests, datetime as dt, pandas as pd, time

# HEADERS = {"User-Agent": "Mozilla/5.0"}

# def scan(tag, days=7):
#     end = dt.date.today()
#     start = end - dt.timedelta(days=days)
#     payload = {
#         "keyword": "|".join(tag['eia']),
#         "pageSize": 100,
#         "startDate": start.isoformat()
#     }
#     try:
#         r = requests.post("https://www.eiacloud.com/api/search",
#                           json=payload, headers=HEADERS, timeout=20)
#         r.raise_for_status()
#         data = r.json()
#         # 容错：如果接口没返回 data，返回空 DataFrame
#         if 'data' not in data or not data['data']:
#             return 0
#         df = pd.DataFrame(data['data'])
#         df = df[pd.to_numeric(df.get('investment', 0), errors='coerce') >= tag['min_bid_amount']]
#         return len(df)
#     except Exception:
#         # 网络/解析失败 → 返回 0，避免 Actions 失败
#         return 0
import pandas as pd
import os

def scan(tag, days=7):
    """
    离线示例：直接读本地 CSV，避免网络问题
    CSV 内容格式：
    company,investment,industry_link,date
    """
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'eia_demo.csv')
    if not os.path.exists(csv_path):
        return 0  # 没有文件就返回 0，防止报错
    df = pd.read_csv(csv_path, dtype={'investment': float})
    # 按关键词过滤（简单模糊匹配）
    kw = '|'.join(tag['eia'])
    mask = df['industry_link'].str.contains(kw, case=False, na=False)
    mask &= df['investment'] >= tag['min_bid_amount']
    return mask.sum()

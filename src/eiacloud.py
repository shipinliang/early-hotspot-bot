import requests, datetime as dt, pandas as pd

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scan(tag, days=7):
    """返回 7 天内关键词命中次数"""
    end = dt.date.today()
    start = end - dt.timedelta(days=days)
    payload = {
        "keyword": "|".join(tag['eia']),
        "pageSize": 100,
        "startDate": start.isoformat()
    }
    r = requests.post("https://www.eiacloud.com/api/search", json=payload, headers=HEADERS, timeout=20)
    df = pd.DataFrame(r.json()['data'])
    # 过滤金额
    df = df[df['investment'] >= tag['min_bid_amount']]
    return len(df)

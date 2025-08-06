import requests, datetime as dt, pandas as pd, time

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scan(tag, days=7):
    end = dt.date.today()
    start = end - dt.timedelta(days=days)
    payload = {
        "keyword": "|".join(tag['eia']),
        "pageSize": 100,
        "startDate": start.isoformat()
    }
    try:
        r = requests.post("https://www.eiacloud.com/api/search",
                          json=payload, headers=HEADERS, timeout=20)
        r.raise_for_status()
        data = r.json()
        # 容错：如果接口没返回 data，返回空 DataFrame
        if 'data' not in data or not data['data']:
            return 0
        df = pd.DataFrame(data['data'])
        df = df[pd.to_numeric(df.get('investment', 0), errors='coerce') >= tag['min_bid_amount']]
        return len(df)
    except Exception:
        # 网络/解析失败 → 返回 0，避免 Actions 失败
        return 0

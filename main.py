import os
import requests
import datetime as dt

def main():
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')
    key = os.getenv("WECOM_KEY")
    msg = f"### 【EarlyHotspot 日报 {now}】\n测试消息：GitHub Actions 已连通 ✅"
    if key:
        url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
        requests.post(url, json={"msgtype": "markdown", "markdown": {"content": msg}}, timeout=10)

if __name__ == "__main__":
    main()

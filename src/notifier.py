import os, requests, json, datetime as dt

def send(alerts):
    key = os.getenv("WECOM_KEY")
    if not alerts or not key:
        return
    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')
    lines = [f"### 【EarlyHotspot {now}】"]
    for a in alerts:
        lines.append(f"- **{a['tag']}** 标的：{','.join(a['codes'])}")
    msg = "\n".join(lines)
    url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"
    requests.post(url, json={"msgtype": "markdown", "markdown": {"content": msg}}, timeout=10)

import yaml, datetime as dt
from src import eiacloud, customs, lhb, report_blank, notifier

with open('config.yml', 'r', encoding='utf-8') as f:
    cfg = yaml.safe_load(f)

def main():
    alerts = []
    for tag in cfg['keywords']:
        # Step1 环评/招标/专利
        eia_cnt = eiacloud.scan(tag, days=7)
        if eia_cnt < cfg['thresholds']['eia_hot']:
            continue

        # Step2 海关验证
        if not customs.validate(tag):
            continue

        # Step3 龙虎榜+大宗
        codes = lhb.filter_codes(tag)
        if not codes:
            continue

        # Step4 研报空白
        blanks = [c for c in codes if report_blank.is_blank(c, days=cfg['thresholds']['report_blank_days'])]
        if not blanks:
            continue

        # 组装消息
        alerts.append({
            'tag': tag['name'],
            'codes': blanks,
            'eia_cnt': eia_cnt
        })

    notifier.send(alerts)

if __name__ == '__main__':
    main()

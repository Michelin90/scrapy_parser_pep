import csv
import datetime
from collections import defaultdict

from .settings import BASE_DIR, DT_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.res = defaultdict(int)
        self.total = 0

    def process_item(self, item, spider):
        self.res[item['status']] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        res_list = [(k, v) for k, v in self.res.items()]
        res_dir = BASE_DIR / 'results'
        res_dir.mkdir(exist_ok=True)
        now = datetime.datetime.now()
        now_formated = now.strftime(DT_FORMAT)
        file_name = f'status_summary_{now_formated}.csv'
        file_path = res_dir / file_name
        with open(
            file_path, 'w', encoding='utf-8'
        ) as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(('Status', 'Amount'))
            writer.writerows(res_list)
            writer.writerow(('Total', self.total))

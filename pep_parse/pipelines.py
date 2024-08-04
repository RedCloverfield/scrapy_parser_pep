from collections import defaultdict
import csv
import datetime as dt

from constants import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:
    statuses = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_datetime = dt.datetime.now().strftime(DATETIME_FORMAT)
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        filename = f'status_summary_{current_datetime}.csv'
        file_path = results_dir / filename
        results = [
            ('Статус', 'Количество'),
            *self.statuses.items(),
            ('Всего', sum(self.statuses.values())),
        ]
        with open(file_path, 'w', encoding='utf-8') as file:
            csv.writer(file, dialect=csv.unix_dialect()).writerows(results)

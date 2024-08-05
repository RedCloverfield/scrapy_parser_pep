from collections import defaultdict
import csv
import datetime as dt

from constants import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        current_datetime = dt.datetime.now().strftime(DATETIME_FORMAT)
        filename = f'status_summary_{current_datetime}.csv'
        file_path = self.results_dir / filename
        with open(file_path, 'w', encoding='utf-8') as file:
            csv.writer(
                file, dialect=csv.unix_dialect(), quoting=csv.QUOTE_NONE
            ).writerows(
                ('Статус', 'Количество'),
                *self.statuses.items(),
                ('Всего', sum(self.statuses.values())),
            )

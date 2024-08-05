from constants import RESULTS_DIR, PEP_SPIDER

BOT_NAME = 'pep_parse'

SPIDER_MODULES = [PEP_SPIDER]
NEWSPIDER_MODULE = PEP_SPIDER

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

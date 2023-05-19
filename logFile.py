import logging
from faker import Faker
# FORMAT = '%(asctime)s %(service)s %(host)s %(payload)s %(latency)s %(status)s [%(api)s] %(request)s %(cpu_latency)s %(error_code)s %(error_code2)s %(exception)s %(from_address)s'
# logging.basicConfig(format=FORMAT)
# d = {'services': 'imap', 'host': 'machine10.dovecotservice.datacenter3.mail.emailcompany.com', 'payload': 10, 'latency': 23, 'status': 200, 'api': 'api/done', 'request': '/message/scan/id=messageHash6hjg76989g', 'cpu_latency': 2, 'error_code': 'nosuchmailbox', 'error_code2': 'bad filer', 'exception': 'bad encoding', 'from_address': '10.56.765.56'}
# logger = logging.getLogger('tcpserver')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)

fake = Faker()
n = 100
log_entries = [{'clientip': fake.ipv4(), 'user': fake.user_name()} for _ in range(n)]

for log_entry in log_entries:
    logger = logging.getLogger('tcpserver')
    logger.warning('User name with IP Address', extra=log_entry)
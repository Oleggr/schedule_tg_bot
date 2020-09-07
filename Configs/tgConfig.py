BOT_TOKEN = "token must be here"
MONITORING_BOT_TOKEN = "monitoring bot token must be here"

NOTIFICATION_CHAT_ID = -000000000

#Config for web-server
WEBHOOK_HOST = ''
WEBHOOK_PORT = 80  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './private.key'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (BOT_TOKEN)

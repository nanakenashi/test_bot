import logging
import os

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Slack'

SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
BOT_IDENTITY = {
    'token': SLACK_BOT_TOKEN
}

BOT_DATA_DIR = r'/web/test_bot/data'
BOT_EXTRA_PLUGIN_DIR = '/web/test_bot/plugins'

BOT_LOG_FILE = r'/web/test_bot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

SLACK_BOT_ADMIN = os.getenv('SLACK_BOT_ADMIN')
BOT_ADMINS = (SLACK_BOT_ADMIN)

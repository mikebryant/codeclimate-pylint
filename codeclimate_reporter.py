"""Codeclimate compatible JSON reporter"""
import json

from pylint.interfaces import IReporter
from pylint.reporters import BaseReporter


class CodeClimateReporter(BaseReporter):
    """Report messages and layouts in JSON."""

    __implements__ = IReporter
    name = 'codeclimate'
    extension = 'json'
    category_map = {
        'convention': ['Clarity', 'Style'],
        'refactor': ['Clarity', 'Complexity'],
        'warning': ['Bug Risk'],
        'error': ['Bug Risk'],
        'fatal': ['Bug Risk'],
    }
    severity_map = {
        'convention': 'info',
        'refactor': 'info',
        'warning': 'normal',
        'error': 'critical',
        'fatal': 'critical',
    }

    def __init__(self, *args, **kwargs):
        super(CodeClimateReporter, self).__init__(*args, **kwargs)
        with open('/config.json') as config_file:
            self.config = json.loads(config_file.read())

    def handle_message(self, message):
        """Manage message of different type and in the context of path."""

        if './' not in self.config['include_paths']:
            for include_path in self.config['include_paths']:
                if message.path.startswith(include_path):
                    break
            else:
                return

        for exclude_path in self.config['exclude_paths']:
            if message.path.startswith(exclude_path):
                return

        msg = {
            'type': 'issue',
            'check_name': message.symbol,
            'description': message.msg.replace('\'', '`').splitlines()[0],
            'categories': self.category_map[message.category],
            'location': {
                'path': message.path,
                'lines': {
                    'begin': message.line,
                    'end': message.line,
                },
            },
            'severity': self.severity_map[message.category],
        }
        if '\n' in message.msg:
            msg['content'] = message.msg
        msg_json = json.dumps(msg, indent=4)
        self.writeln("%s\0" % msg_json)

    def _display(self, layout):
        """Reports are not supported."""

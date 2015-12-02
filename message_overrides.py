'''
    Allow overriding individual message details
'''

BASELINE_REMEDIATION_VALUE = 50000
EASY_REMEDIATION = BASELINE_REMEDIATION_VALUE
MEDIUM_REMEDIATION = BASELINE_REMEDIATION_VALUE * 3
HARD_REMEDIATION = BASELINE_REMEDIATION_VALUE * 6

OVERRIDES = {
    'backtick': {
        'remediation_points': EASY_REMEDIATION,
    },
    'bad-classmethod-argument': {
        'remediation_points': EASY_REMEDIATION,
    },
    'bad-mcs-classmethod-argument': {
        'remediation_points': EASY_REMEDIATION,
    },
    'bad-mcs-method-argument': {
        'remediation_points': EASY_REMEDIATION,
    },
    'bad-whitespace': {
        'remediation_points': EASY_REMEDIATION,
    },
    'line-too-long': {
        'remediation_points': EASY_REMEDIATION,
    },
    'lowercase-l-suffix': {
        'remediation_points': EASY_REMEDIATION,
    },
    'missing-final-newline': {
        'remediation_points': EASY_REMEDIATION,
    },
    'multiple-statements': {
        'remediation_points': EASY_REMEDIATION,
    },
    'no-self-argument': {
        'remediation_points': EASY_REMEDIATION,
    },
    'superfluous-parens': {
        'remediation_points': EASY_REMEDIATION,
    },
    'trailing-whitespace': {
        'remediation_points': EASY_REMEDIATION,
    },
    'unused-argument': {
        'remediation_points': EASY_REMEDIATION,
    },
    'unused-import': {
        'remediation_points': EASY_REMEDIATION,
    },
    'unused-variable': {
        'remediation_points': EASY_REMEDIATION,
    },
}

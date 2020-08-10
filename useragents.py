#!/usr/bin/env python3 -u

import json
import fileinput
from user_agents import parse


for line in fileinput.input():
    ua_text = line.rstrip()
    ua = parse(ua_text)
    print (json.dumps({
        'ua_string': ua.ua_string,
        'browser': {
            'version': ua.browser.version,
            'family': ua.browser.family,
            'version_string': ua.browser.version_string,
        },
        'device': {
            'brand': ua.device.brand,
            'family': ua.device.family,
            'model': ua.device.model,
        },
        'os': {
            'version': ua.os.version,
            'family': ua.os.family,
            'version_string': ua.os.version_string,
        },
        'is_bot': ua.is_bot,
        'is_email_client': ua.is_email_client,
        'is_mobile': ua.is_mobile,
        'is_tablet': ua.is_tablet,
        'is_touch_capable': ua.is_touch_capable,
        'is_pc': ua.is_pc,
    }
))


 
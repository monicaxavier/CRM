#Mining Twitter Data
#Author: Rick Rejeleene
#Anatomy of Tweet

import re

emoticons_str = r"""
    (?:[:=;]#Eyes
        [oO\-]?#Nose(optional)
        [D\)\]\(\]/\\OpP])"""


regex_str = [emoticons_str,r'<[^>]+>',
                            r'(?:@[\w_]+)',
                            r"(?:\#+[\w_]+[\w\'_\-]([\w_]+)",
                            r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
                            r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
                            r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
                            r'(?:[\w_]+)', # other words
                            r'(?:\S)' # anything else
                            ]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')',re.VERBOSE | re.IGNORECASE)
emoticon_e = re.compile(r'^'+emoticons_str+'$',re.VERBOSE|re.IGNORECASE)


print tokens_re

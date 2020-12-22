DIGIT_MAP = {
    'zero': '0',
    'one':  '1',
    'two':  '2',
    'three':'3',
    'four': '4',
    'five': '5',
    'six':  '6',
    'seven':'7',
    'eight':'8',
    'nine': '9',

}
import sys

def convert(s):
    try: # Raise exception
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion successed! x= {x}")
    except (KeyError,TypeError) as e: # handle key error exception only. You do can use except without specific error type to handle all.
        x = -1
        print(f"Conversion failed: {e!r}",
                file=sys.stderr)
        raise

    return x


from math import log


def string_log(s):
    v = convert(s)
    return log(v)

print(convert("one three three seven".split()))
print(convert("hello world".split()))
print(convert(332))
string_log("ouch".split())
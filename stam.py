"""
Extract stem of Dutch verb

>>> stam('lopen')
'loop'

>>> stam('loppen')
'lop'
"""
def stam(infinitief):
    cut = infinitief[:-2]

    # the vowel of the last syllabus is short if the consonant is repeated after it
    kort = cut[-1] == cut[-2]

    # in the case of one consonant in the end, and simple vowel, the following formula works
    if kort:
        return cut[:-1]
    return cut[:-1] + cut[-2:]

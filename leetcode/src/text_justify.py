"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
For example,
    words: ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth(L): 16.
Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    result = []
    line = []
    words_len = len(words)
    word_count = 0
    for i in range(words_len):
        word_count += len(words[i])
        n = word_count - maxWidth
        if n > 0:
            extra_spaces = len(words[i]) - n + 1
            text = fill_space(line, maxWidth, extra_spaces)
            result.append(text)
            line = []
            word_count = len(words[i])

        line.append(words[i])
        word_count += 1

    if len(line) > 0:
        text = ' '.join(line)
        text += ' ' * (maxWidth - len(text))
        result.append(text)

    print result
    return result


def fill_space(line, max_width, extra_spaces):
    result = ''
    c = len(line) - 1
    if c == 0:
        c = 1
    space = ' '
    avg_spaces = 0
    _extra_spaces = 0
    if extra_spaces > 0:
        avg_spaces = extra_spaces / c
        _extra_spaces = extra_spaces % c

    if len(line) - 1 > 0:
        avg_spaces += 1
    for word in line:
        if len(result) > max_width:
            break
        result += word
        if _extra_spaces > 0:
            result += space
            _extra_spaces -= 1
        if len(result) < max_width:
            result += space * avg_spaces

    return result



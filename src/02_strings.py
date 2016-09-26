value = input('Enter a string: ')
print('UPPER CASE: {}'.format(value.lower()))
print('lower case: {}'.format(value.upper()))
print('Title Case: {}'.format(value.title()))
print('List of words: {}'.format(value.split(' ')))
substr = input('Enter a substring: ')
count = value.count(substr)
print('The string contains {} instance(s) of the substring.'.format(count) if count > 0 else 'The string contains no instances of the substring.')

# Design and implement a simple HTML pretty printing algorithm.
# (Assume that each opening/closing tag that signals an indent change starts on a new line.)

def pretty_print(html):
    level = 0
    indent = '    '                                                                                 # spaces > tabs ;)
    tags = (('html', 'body', 'div', 'nav', 'span', 'ul', 'li', 'header', 'footer', 'table', 'tr'))  # other tags may need to be added
    opening_tags = ['<{}>'.format(tag) for tag in tags]
    closing_tags = ['</{}>'.format(tag) for tag in tags]
    for line in html.split('\n'):
        line = line.strip()
        if any(line.startswith(tag) for tag in closing_tags):
            level -= 1
            print('{}{}'.format(level * indent, line)) 
        elif any(line.startswith(tag) for tag in opening_tags):
            print('{}{}'.format(level * indent, line))
            level += 1
        else:
            print('{}{}'.format(level * indent, line))
            
with open('resources/sample.html', 'r') as fin:
    html = fin.read()    
    pretty_print(html)

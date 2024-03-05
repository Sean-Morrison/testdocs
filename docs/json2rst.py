
#!/usr/bin/env python
"""To launch: ``$ python update.py > animals.rst``  """

import json

def headline(text, adorn='='):
    return text + '\n' + adorn*len(text)

def main():
    header = headline('Full Command Documention') + '\n'
    footer = '\n.. End of document\n'
    mask = '\n{name}\n\n{fmt}\n {doc}'

    with open('doc.json', 'r') as infile:
        data = json.load(infile)

    with open('sphinx/doc.rst', 'w') as out:
        out.write(header)
        for cmd in data['cmd']:
            out.write(mask.format(fmt = '^'*len(cmd['name']), **cmd))
        out.write(footer)

if __name__ == '__main__':
    main()

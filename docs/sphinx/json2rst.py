
#!/usr/bin/env python

import json

def headline(text, adorn='='):
    return text + '\n' + adorn*len(text)

def main():
    header = headline('Full Command Documention') + '\n'
    footer = '\n.. End of document\n'
    
    mask = '\n.. _{name}:\n\n{name}\n{fmt}\n::\n \n    {doc}\n'

    try:
        with open('../doc.json', 'r') as infile:
            data = json.load(infile)
    except:
        with open('./docs/doc.json', 'r') as infile:
            data = json.load(infile)

    with open('doc.rst', 'w') as out:
        out.write(':tocdepth: 2\n\n')
        out.write('.. highlight:: none\n\n')
        out.write(header)
#        out.write('.. contents::\n')
#        out.write('    :depth: 1'+'\n')
#        out.write('    :local:\n')
#        out.write('    :class: this-will-duplicate-information-and-it-is-still-useful-here\n')
#        out.write('    :backlinks: none\n\n')
        
        sec_hdr ='Full Bash and Python Command Usage'
        out.write(headline(sec_hdr, adorn='-')+'\n\n')
        
        out.write('.. contents::\n')
        out.write('    :depth: 3'+'\n')
        out.write('    :local:\n')
        out.write('    :class: this-will-duplicate-information-and-it-is-still-useful-here\n')
        out.write('    :backlinks: none\n\n')
        
        for cmd in data['cmd']:
            cmd['doc'] = cmd['doc'].replace('\n','\n    ')
            out.write(mask.format(type='bin', fmt = '^'*len(cmd['name']), **cmd))
           
        out.write('\n')
        sec_hdr ='IDL Command Usage'
        out.write(headline(sec_hdr, adorn='-')+'\n\n')
        
        out.write('.. contents::\n')
        out.write('    :depth: 3'+'\n')
        out.write('    :local:\n')
        out.write('    :class: this-will-duplicate-information-and-it-is-still-useful-here\n')
        out.write('    :backlinks: none\n\n')

        for cmd in data['idl']:
            cmd['doc'] = cmd['doc'].replace('\n','\n    ')
            out.write(mask.format(type='idl', fmt = '^'*len(cmd['name']), **cmd))

        out.write('\n\n.. highlight:: defaults\n\n')

        out.write(footer)

if __name__ == '__main__':
    main()

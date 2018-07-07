import os

walker = os.walk('.')

# main_dir = next(walker)[1]

# print(main_dir)

def isIgnored(file):
    return file.startswith('/.git') or file.startswith('/docs') or\
        file.startswith('/documentation_utils')

def compile_content(file_name, file_path, content):
    f = open(file_path[:-2] + 'md', 'a+')
    f.write('# {}\n'.format(file_name))
    previous = ''
    doc_comments = False
    for line in content.split('\n'):
        if not line: pass
        elif line == '"""' or line == "'''":
            doc_comments = not doc_comments
        elif doc_comments:
            f.write(line)
            previous = 'comment'
        elif line.startswith('#'):
            f.write(line[1:].strip())
            previous = 'comment'
        else:
            if previous == 'comment': f.write('\n')
            f.write('\t\t' + line)
            previous = 'code'
        f.write('\n')
    f.close()

_ = next(walker)

for i in walker:
    path = './documentation_utils' + i[0][1:]
    if not isIgnored(i[0][1:]):
        if not os.path.isdir(path): os.makedirs('./documentation_utils' + i[0][1:])
        for file in i[2]:
            print('reading', os.path.join(i[0], file))
            if file.endswith('.py'):
                with open(os.path.join(i[0], file), 'r') as f:
                    py_content = f.read()
                compile_content(file[:-3], os.path.join('./documentation_utils' + i[0][1:], file), py_content)

import os

# Initialize a recursive walker
walker = os.walk('.')



def isIgnored(file):
    '''
    Checks if the directory should be ignored or not
    '''
    return file.startswith('/.git') or file.startswith('/docs') or\
        file.startswith('/documentation_utils')

def compile_content(file_name, file_path, content):
    '''
    Compile content line by line separating comments and code
    '''
    f = open(file_path[:-2] + 'md', 'a+')
    f.write('# {}\n'.format(file_name))
    previous = ''
    doc_comments = False
    for line in content.split('\n'):
        if not line: pass
        # Checks for start and end of doc string
        elif line == '"""' or line == "'''":
            doc_comments = not doc_comments
        # Checks for doc string
        elif doc_comments:
            f.write(line)
            previous = 'comment'
        # Checks for line comments
        elif line.startswith('#'):
            f.write(line[1:].strip())
            previous = 'comment'
        # Adds code
        else:
            # Add a line before code so that it renders correctly
            if previous == 'comment': f.write('\n')
            f.write('\t\t' + line)
            previous = 'code'
        f.write('\n')
    f.close()

# Ignore first layer of directory
_ = next(walker)

# Walk through content recursively
for i in walker:
    # check if path is not ignored, ignores first dot in path
    path = './documentation_utils' + i[0][1:]
    if not isIgnored(i[0][1:]):
        if not os.path.isdir(path): os.makedirs('./documentation_utils' + i[0][1:])
        for file in i[2]:
            print('reading', os.path.join(i[0], file))
            # Only reads python files. Can be improved later
            if file.endswith('.py'):
                # Read content of python file
                with open(os.path.join(i[0], file), 'r') as f:
                    py_content = f.read()
                compile_content(file[:-3], os.path.join('./documentation_utils' + i[0][1:], file), py_content)

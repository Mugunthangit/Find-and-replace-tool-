import os
 
def main(path, file_name, old_content, new_content):
    path = os.path.abspath(path)
    if path:
        print "Given Directory Name %s" % path
    if file_name:
        print "Given File Name %s" % file_name
    for dirname, dirnames, filenames in os.walk(path):
        if file_name in filenames:
            with open(os.path.join(dirname, file_name), 'r+') as fobj:
                lines = fobj.read()
                if old_content in lines:
                    print "Matched...."
                    lines = lines.replace(old_content, new_content)
                    fobj.seek(0)
                    fobj.write(lines)


if __name__ == '__main__':
    old_content = "pazhaya content"
    new_content = "puthusu kanna puthusu"
    main('file/path/to/specify', 'file_name', old_content, new_content)

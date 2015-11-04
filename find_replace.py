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
    old_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim  ad minim veniam,"
    new_content = "Effective of 01st August 2015, the passport collection time in UAE Centers (Abu Dhabi, Dubai & Sharjah ) will be from 02.00 pm till 05.00 pm only"
    main('vfs_webpage_bak/views/', 'homelayout.html', old_content, new_content)

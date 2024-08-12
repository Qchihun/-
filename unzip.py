import zipfile
import threading
import optparse


def extractFile (zipFile,password):
    try:
        zipFile.extractall(pwd=str(password).encode())
        print("password:", password)
    except:
        pass
def main():
    parser = optparse.OptionParser("usage%prog -f <ZIP目录> -d <字典目录>")
    parser.add_option("-f", dest="zipFile", type="string", help="指定zip文件")
    parser.add_option("-d", dest="dictionary", type="string", help="指定字典文件")
    (options, args) = parser.parse_args() #解析命令行参数
    if options.zipFile is None or options.dictionary is None:
        print(parser.usage) #如果命令行参数为空，则打印帮助信息
        exit(0)
    else:
        zname = options.zipFile
        dname = options.dictionary
    threads = []  # 创建一个线程列表
    zFile = zipfile.ZipFile(zname, 'r')
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n') #strip()函数用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        t = threading.Thread(target=extractFile,args=(zFile,password))
        threads.append(t) #将线程添加到线程列表中
        t.start()
    for t in threads:
        t.join() #等待所有线程执行完毕
if __name__ == '__main__':
    main()

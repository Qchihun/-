from socket import *
from threading import Thread
import optparse
#ASCII艺术形式打印Qscan
text ='''
欢迎使用Qscan
Qscan是一个简单的端口扫描器
请误使用Qscan进行非法行为
'''
def TCPscan(port,ip):

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(1)
        c = s.connect_ex((ip, port))
        if c == 0:
            print(f"端口 {port} 状态: open")
        else:
            print(f"端口 {port} 状态: closed")
        s.close()
    except:
        pass

def UDPscan(port,ip):

    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.settimeout(1)
        s.sendto(b'hello', (ip, port))
        try:
            data, addr = s.recvfrom(1024)
            if data is not None:
                print(f"端口 {port} 状态: open")
        except:
            print(f"端口 {port} 状态: closed")
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog -s <欲扫描的网址> -p <端口号>,<端口号2> -t TCP扫描 -u UDP扫描")
    parser.add_option("-s", dest="tgtHost", type="string", help="网址")
    parser.add_option("-p", dest="tgtPort", type="string", help="端口")
    parser.add_option("-t", dest="tgtTCP", action="store_true", help="TCP 扫描")
    parser.add_option("-u", dest="tgtUdp", action="store_true", help="UDP 扫描")
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    tgtTCP = options.tgtTCP
    tgtUdp = options.tgtUdp
    if tgtHost is None or tgtPort is None:
        print(parser.usage) #如果tgtHost或tgtPort为空，则打印帮助信息
        exit(0)
    if tgtTCP is not None:
        for port in tgtPort.split(','):
            t = Thread(target=TCPscan, args=(int(port), tgtHost))
            t.start()
    if tgtUdp is not None:
        for port in tgtPort.split(','):
            t = Thread(target=UDPscan, args=(int(port), tgtHost))
            t.start()
            t.join()
if __name__ == '__main__':
    main()
    print(text)

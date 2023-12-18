#sources: https://realpython.com/python-sockets/, https://realpython.com/intro-to-python-threading/
import socket
import threading
import sys
import json
import time

HOSTS = ["fa23-cs425-2001.cs.illinois.edu", "fa23-cs425-2002.cs.illinois.edu",
    "fa23-cs425-2003.cs.illinois.edu", "fa23-cs425-2004.cs.illinois.edu",
    "fa23-cs425-2005.cs.illinois.edu", "fa23-cs425-2006.cs.illinois.edu",
    "fa23-cs425-2007.cs.illinois.edu", "fa23-cs425-2008.cs.illinois.edu",
    "fa23-cs425-2009.cs.illinois.edu", "fa23-cs425-2010.cs.illinois.edu"]

PORT = 65432 # arbitrary
logs = {}

def query_threads(host, cmd):
    begin = time.time()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, PORT))
            query = json.dumps({"command_parameters":cmd}).encode('utf-8')
            s.sendall(query)
        
            output = b'' # get server response 
            while True:
                response = s.recv(1024) # buffer
                if response:
                    output += response
                else:
                    break

            if output != "":
                logs[host] = (json.loads(output.decode('utf-8')), time.time() - begin)

        except Exception as e:
            if ("Expecting value" in str(e)):
                logs[host] = ('0', '0')
            else:
                print(host, e)

if __name__ == '__main__':
    cmd = sys.argv[1:] # this is everything but the file name. fix this later maybe
    threads = []
    total_time = time.time()

    # TODO: Multiple VM's, have to change arguments in thread 
    for vm in HOSTS:
        t = threading.Thread(target = query_threads, args = (vm, cmd))
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    for log in logs:
        print(log, logs[log][0], logs[log][1])
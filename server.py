import socket
import json
import subprocess

HOST = socket.gethostname()
#HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True: # multiple clients
        conn, addr = s.accept()
        with conn:
            try: 
                data = conn.recv(1024)
                cmd=json.loads(data.decode('utf-8'))["command_parameters"]
                print(cmd)
                cmd.append("vm2.log") # file to run, change this to log file later 
                result = subprocess.check_output(cmd).decode("utf-8") # run grep command
                result = result[:-1] # get rid of the \n 
                conn.sendall(json.dumps(result).encode('utf-8'))
            except Exception as e:
                print(e)
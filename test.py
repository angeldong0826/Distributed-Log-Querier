import unittest
import log_generator
import client
import subprocess


class TestLogQueries(unittest.TestCase):
    def test_frequent(self):
        client_command = ["python3", "client.py", "grep", "-c", "app"]

        try:
            result = subprocess.run(client_command, check=True, stdout=subprocess.PIPE)
            output = result.stdout.decode("utf-8").strip()  
            splitted = output.split()
            print(splitted)

            for s in range(0, len(splitted), 3):
                if splitted[s] =="fa23-cs425-2001.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "84527")
                elif splitted[s] =="fa23-cs425-2002.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "80131")
                elif splitted[s] =="fa23-cs425-2003.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "80156")
                elif splitted[s] =="fa23-cs425-2004.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "80472")
                elif splitted[s] =="fa23-cs425-2005.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "81051")
                elif splitted[s] =="fa23-cs425-2006.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "80350")
                elif splitted[s] =="fa23-cs425-2007.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "79799")
                elif splitted[s] =="fa23-cs425-2008.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "81367")
                elif splitted[s] =="fa23-cs425-2009.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "80216")
                elif splitted[s] =="fa23-cs425-2010.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "78786")

        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")

    def test_somewhat_frequent(self):
        client_command = ["python3", "client.py", "grep", "-c", "hi"]

        try:
            result = subprocess.run(client_command, check=True, stdout=subprocess.PIPE)
            output = result.stdout.decode("utf-8").strip()  
            splitted = output.split()
            print(splitted)
            
            for s in range(0, len(splitted), 3):
                if splitted[s] =="fa23-cs425-2001.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7770")
                elif splitted[s] =="fa23-cs425-2002.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7571")
                elif splitted[s] =="fa23-cs425-2003.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7344")
                elif splitted[s] =="fa23-cs425-2004.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7432")
                elif splitted[s] =="fa23-cs425-2005.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7396")
                elif splitted[s] =="fa23-cs425-2006.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7390")
                elif splitted[s] =="fa23-cs425-2007.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7372")
                elif splitted[s] =="fa23-cs425-2008.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7410")
                elif splitted[s] =="fa23-cs425-2009.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7342")
                elif splitted[s] =="fa23-cs425-2010.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "7248")

        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")

    def test_rare(self):
        client_command = ["python3", "client.py", "grep", "-c", "rubio"]

        try:
            result = subprocess.run(client_command, check=True, stdout=subprocess.PIPE)
            output = result.stdout.decode("utf-8").strip()  
            splitted = output.split()
            print(splitted)
            
            for s in range(0, len(splitted), 3):
                if splitted[s] =="fa23-cs425-2001.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "131")
                elif splitted[s] =="fa23-cs425-2002.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "116")
                elif splitted[s] =="fa23-cs425-2003.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "125")
                elif splitted[s] =="fa23-cs425-2004.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "130")
                elif splitted[s] =="fa23-cs425-2005.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "108")
                elif splitted[s] =="fa23-cs425-2006.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "107")
                elif splitted[s] =="fa23-cs425-2007.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "119")
                elif splitted[s] =="fa23-cs425-2008.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "121")
                elif splitted[s] =="fa23-cs425-2009.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "123")
                elif splitted[s] =="fa23-cs425-2010.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "110")

        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")
        

    def test_single_appearance(self):
        client_command = ["python3", "client.py", "grep", "-c", "17/Aug/2022:18:23:49"]

        try:
            result = subprocess.run(client_command, check=True, stdout=subprocess.PIPE)
            output = result.stdout.decode("utf-8").strip()  
            splitted = output.split()
            print(splitted)
            
            for s in range(0, len(splitted), 3):
                if splitted[s] =="fa23-cs425-2001.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "1")
                elif splitted[s] =="fa23-cs425-2002.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2003.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2004.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2005.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2006.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2007.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2008.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2009.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2010.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")

        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")
        

    def test_some_appearance(self):
        client_command = ["python3", "client.py", "grep", "-c", "Aug/2022:18:23:49"]

        try:
            result = subprocess.run(client_command, check=True, stdout=subprocess.PIPE)
            output = result.stdout.decode("utf-8").strip()  
            splitted = output.split()
            print(splitted)
            
            for s in range(0, len(splitted), 3):
                if splitted[s] =="fa23-cs425-2001.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "1")
                elif splitted[s] =="fa23-cs425-2002.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2003.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "1")
                elif splitted[s] =="fa23-cs425-2004.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2005.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2006.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2007.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2008.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "1")
                elif splitted[s] =="fa23-cs425-2009.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")
                elif splitted[s] =="fa23-cs425-2010.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "0")

        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")
    

    def test_regex_appearance(self):
        client_command = ["python3", "client.py", "grep", "-c", "r[a-m]sm[a-z]sse[a-z]"]

        try:
            result = subprocess.run(client_command, check=True, stdout=subprocess.PIPE)
            output = result.stdout.decode("utf-8").strip()  
            splitted = output.split()
            print(splitted)
            
            for s in range(0, len(splitted), 3):
                if splitted[s] =="fa23-cs425-2001.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "126")
                elif splitted[s] =="fa23-cs425-2002.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "119")
                elif splitted[s] =="fa23-cs425-2003.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "100")
                elif splitted[s] =="fa23-cs425-2004.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "109")
                elif splitted[s] =="fa23-cs425-2005.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "143")
                elif splitted[s] =="fa23-cs425-2006.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "101")
                elif splitted[s] =="fa23-cs425-2007.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "113")
                elif splitted[s] =="fa23-cs425-2008.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "128")
                elif splitted[s] =="fa23-cs425-2009.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "120")
                elif splitted[s] =="fa23-cs425-2010.cs.illinois.edu":
                    self.assertEqual(splitted[s+1], "116")

        except subprocess.CalledProcessError as e:
            print(f"Error running the command: {e}")



if __name__ == '__main__':
    unittest.main()
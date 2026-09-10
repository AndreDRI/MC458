import subprocess
import time
from colorama import init, Fore, Back, Style

TESTS_PATH = "./tests/"
MAX_NUM_TESTS = 50
MAX_RUNTIME = 1

def main():
    init(autoreset=True)
    tests_len = detect_tests()
    if tests_len > 0:
        print(Fore.BLUE + "[TESTER] " + Fore.CYAN + f"Found {tests_len} Tests")
    else:
        print(Fore.BLUE + "[TESTER] " + Fore.RED + "[ERROR] No Tests Found Exiting")
        return 0
    for i in range(1, tests_len + 1):
        with open(TESTS_PATH + f"test{i}_in.txt", "r") as infile:
            try:
                start = time.time()
                result_process = subprocess.run(["python", "./main.py"], stdin=infile,timeout=MAX_RUNTIME , capture_output=True, text=True)
                finish = time.time()
                with open(TESTS_PATH + f"test{i}_out.txt", "w") as f:
                    f.write(result_process.stdout.rstrip('\r\n'))
                compare(i, False, start, finish)
            except subprocess.TimeoutExpired as error:
                compare(i, True, 0, 0)
                    

def compare(test_num, timeout, start, finish):
    if timeout and not start and not finish:
        print(Fore.BLUE + "[TESTER] " + Fore.RED + f"[TEST {test_num}] " + Fore.RED + "Timeout out")
    else:
        with open(TESTS_PATH + f"test{test_num}_out.txt", "r") as f_out:
            output = f_out.read()
        with open(TESTS_PATH + f"test{test_num}_sol.txt", "r") as f_sol:
            solution = f_sol.read()
        if output == solution:
            print(Fore.BLUE + "[TESTER] " + Fore.GREEN + f"[TEST {test_num} {finish - start:.2f}s] " + Fore.GREEN + "Success")
        else:
            print(Fore.BLUE + "[TESTER] " + Fore.RED + f"[TEST {test_num} {finish - start:.2f}s] " + Fore.RED + "Failed")


def detect_tests():
    tests_len = 0
    for i in range(1,MAX_NUM_TESTS + 1):
        try:
            with open(TESTS_PATH + f"test{i}_in.txt"):
                tests_len += 1
        except:
            return tests_len
    


main()
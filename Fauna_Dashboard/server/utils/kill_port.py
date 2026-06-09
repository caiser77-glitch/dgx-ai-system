import os
import signal
import subprocess
import sys

def kill_process_on_port(port):
    try:
        # lsof 명령을 통해 포트를 점유하고 있는 PID 리스트 조회
        cmd = f"lsof -t -i :{port}"
        pids = subprocess.check_output(cmd, shell=True).decode().strip().split('\n')
        for pid_str in pids:
            if pid_str:
                pid = int(pid_str)
                os.kill(pid, signal.SIGTERM)
                print(f"포트 {port}를 점ey하던 프로세스 {pid}를 안전하게 종료했습니다.")
    except subprocess.CalledProcessError:
        print(f"포트 {port}를 점유하고 있는 프로세스가 없습니다.")
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == '__main__':
    if len(sys.sys.argv) > 1:
        kill_process_on_port(int(sys.argv[1]))
    else:
        print("포트 번호를 인자로 제공해 주십시오.")

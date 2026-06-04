#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import smbclient

def test_connection():
    username = 'kwon-incheon01'
    password = 'aurum2026!'
    server_ip = '100.94.64.83'
    share_name = 'dgxbackup'
    
    print(f"Connecting to NAS ({server_ip}) via smbclient as user '{username}'...")
    
    try:
        # 세션 등록
        smbclient.register_session(server_ip, username=username, password=password)
        
        # 공유 폴더 경로 정의 (Windows style backslash)
        nas_path = f"\\\\{server_ip}\\{share_name}"
        print(f"Listing directory content of {nas_path}...")
        
        # 파일 목록 가져오기
        files = smbclient.listdir(nas_path)
        print("\n--- List of Files/Folders ---")
        for f in files:
            print(f"- {f}")
            
        print("\nConnection verification passed successfully!")
        smbclient.reset_session(server_ip)
        return True
    except Exception as e:
        print(f"Error occurred during SMB connection: {e}")
        return False

if __name__ == '__main__':
    success = test_connection()
    sys.exit(0 if success else 1)

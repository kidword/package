# -*- coding:utf-8 -*-
"""
本地到服务器文件上传/下载
"""
import paramiko
import os
from spiders.setting import *


class TransferFile:
    def __init__(self):
        self.local_dir = LOCAL_DIR
        self.remote_dir = REOTE_DIR
        self.t = paramiko.Transport((HOST_NAME, FW_PORT))
        self.t.connect(username=USERNAME, password=PASSWORD)
        self.sftp = paramiko.SFTPClient.from_transport(self.t)

    def upload(self):
        """
        上传本地数据到服务器上
        """
        for root, dirs, files in os.walk(self.local_dir):
            for filespath in files:
                local_file = os.path.join(root, filespath)
                a = local_file.replace(self.local_dir, '').replace('\\', '/').lstrip('/')
                remote_file = os.path.join(self.remote_dir, a)
                try:
                    self.sftp.put(local_file, remote_file)
                except Exception as e:
                    self.sftp.mkdir(os.path.split(remote_file)[0])
                    self.sftp.put(local_file, remote_file)
                    print(e)
            for name in dirs:
                local_path = os.path.join(root, name)
                a = local_path.replace(self.local_dir, '').replace('\\', '')
                remote_path = os.path.join(self.remote_dir, a)
                try:
                    self.sftp.mkdir(remote_path)
                except Exception as e:
                    print(e.args)
        self.t.close()

    def remote_scp(self):
        """
        从服务器上下载数据到本地
        """
        src = self.remote_dir
        des = self.local_dir
        self.sftp.get(src, des)
        self.t.close()

if __name__ == '__main__':
    s = TransferFile()
    s.remote_scp()

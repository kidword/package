from qiniuyun.setting import *
from qiniu import Auth, put_file, etag


class QiNiuYunUpFile(object):
    def __init__(self):
        self.q = Auth(AK, SK)  # 自己的AK和SK
        self.bucket_name = 'kidword'  # 要上传的空间

    def upfile(self, localfile, key):
        """
        :param localfile: 本地路径
        :param key: 上传后的文件名
        """
        token = self.q.upload_token(self.bucket_name, key, ExpirationDate)  # 生成上传 Token，可以指定过期时间等
        ret, info = put_file(token, key, localfile)
        if info.status_code == 200:
            assert ret['key'] == key
            assert ret['hash'] == etag(localfile)
            print('上传成功')
        else:
            print('上传失败')

if __name__ == '__main__':
    ce = QiNiuYunUpFile()
    ce.upfile(r'H:\360用户文件\tls_passthrough.py', 'test')

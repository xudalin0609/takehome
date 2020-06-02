import unittest

import requests


class MyTest(unittest.TestCase):
    def setUp(self):
        print("start test")
        pass

    def tearDown(self):
        print("end test")
        pass


class test_ocr_post(MyTest):

    def test_ocr_png_post(self):
        '''标准png图片测试'''
        self.url = "http://127.0.0.1:5000/api/v1/ocr"
        with open("./test_materail/test.png", 'rb') as f:
            file = f.read()
        files = {
            "file": ("filename1.png", file),
        }
        r = requests.post(url=self.url, files=files)
        self.assertIn('code', r.json())

    def test_ocr_jpg_post(self):
        '''标准jpg图片测试'''
        self.url = "http://127.0.0.1:5000/api/v1/ocr"
        with open("./test_materail/test.jpg", 'rb') as f:
            file = f.read()
        files = {
            "file": ("filename1.png", file),
        }
        r = requests.post(url=self.url, files=files)
        self.assertIn('code', r.json())

    def test_ocr_no_file_post(self):
        '''无文件'''
        self.url = "http://127.0.0.1:5000/api/v1/ocr"
        files = {
            "file": ("filename1.png", None),
        }
        r = requests.post(url=self.url, files=files)
        self.assertIn('code', r.json())

    def test_ocr_wrong_suffix_post(self):
        '''错误后缀文件'''
        self.url = "http://127.0.0.1:5000/api/v1/ocr"
        with open("./test_materail/abnormal_file.test", 'rb') as f:
            file = f.read()
        files = {
            "file": ("filename1.png", file),
        }
        r = requests.post(url=self.url, files=files)
        self.assertIn('code', r.json())

    def test_ocr_abnormal_file_post(self):
        '''错误后缀文件测试'''
        self.url = "http://127.0.0.1:5000/api/v1/ocr"
        with open("./test_materail/abnormal_file.png", 'rb') as f:
            file = f.read()
        files = {
            "file": ("filename1.png", file),
        }
        r = requests.post(url=self.url, files=files)
        self.assertIn('code', r.json())


if __name__ == "__main__":
    unittest.main()

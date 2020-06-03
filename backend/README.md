# Backend Projects

- [Simple OCR Letters](https://github.com/teletraan/takehome/blob/master/backend/simple_ocr_letters.md)



## ocr

### 方案




### 接口列表
ip|port|api|method|content
--|--|--|--|--
http://127.0.0.1:8000 | 8000 | /api/v1/ocr | ['POST'] | 传入图片，进行ocr，列表形式返回结果


### 参数列表
参数|解释|备注|
--|--|--
file | 上传的图片文件 | 必须传入

### 返回示例
参数|解释|备注
--|--|--
code | 状态码 | 含义见
content | 图片识别结果 | 格式为列表
errMsg | 接口错误原因 | 正确为空字符串


### python request demo
```python
def page_info_api(url):
    loc = '/api/v1/ocr'
    args = {
        "file
    }

    r = requests.post(url+loc, json=args)
    return r.json()
```

```json
{
    "code": 200,
    "content": [
        "风",
        "急",
        "天",
        "高",
        "猿",
        "喝",
        "哀",
        "渚",
        "清",
        "沙",
        "白",
        "鸟",
        "飞",
        "回",
        "无",
        "边",
        "落",
        "木",
        "萧",
        "萧",
        "下",
        "不",
        "尽",
        "长",
        "江",
        "滚",
        "滚",
        "来",
        "万",
        "里",
        "悲",
        "秋",
        "常",
        "作",
        "客",
        "百",
        "年",
        "多",
        "病",
        "独",
        "登",
        "台",
        "艰",
        "难",
        "苦",
        "恨",
        "繁",
        "霜",
        "鬓",
        "漫",
        "倒",
        "新",
        "停",
        "浊",
        "酒",
        "杯"
    ],
    "errMsg": "",
    "unix_time": 1591078303
}

```
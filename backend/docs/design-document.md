### 代码结构
```
--backend
    --bluprints           # 业务逻辑控制
        --v1              # api版本
            --ocr         # api实现
        --index.py        # 返回所有可用api列表
    --common
        --utils.py        # 工具函数
        --extensions.py   # 扩展工具的实例
    --data                # 存放模型及数据库文件
    --test                # 测试文件路径
    --app.py              # 项目入口及初始化
    --models.py           # sqlalchemy模型
    --settings.py         # 项目配置
```

### 部署方案
使用flask+gunicorn+nginx,采用docker进行部署
1. 生成镜像
```
docker build -t ocr-server .
```

2. 启动容器
```
docker run -d --name ocr-server -p 5000:5000 ocr-server
```


### api规则
1. 采用 **[地址]/api/[版本]/[资源]** 的格式,例如http://localhost/api/v1/ocr
2. 根据不同的操作对资源采取不同的行为,例如POST /ocr,返回图片的ocr结果, GET /ocr?limit=5,返回一定条数的历史结果

### 返回数据
1. 返回格式为json
2. 返回的内容必须包含code,errMsg, unixTime,data（返回码, 错误信息, 时间戳, 内容）

### 返回码
- 0：成功
- 1XX：客户端错误
- 2XX：服务器错误

### 版本控制
1. 版本展示在url中,不同的版本应该在不同的blueprints/[版本]中
2. 通过settings.py中ACTIVE_API对api的进行控制,格式为**api名称:(api资源路径, endpoint)**
```
ACTIVE_API = {
    'img_ocr': ('blueprints.v1.ocr.Ocr', ['/api/v1/ocr']),
}

```
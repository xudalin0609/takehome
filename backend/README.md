# Backend Projects

- [Simple OCR Letters](https://github.com/teletraan/takehome/blob/master/backend/simple_ocr_letters.md)



## ocr

### 部署方法
1. 生成镜像
```
docker build -t ocr-server .
```

2. 启动容器
```
docker run -d --name ocr-server -p 5000:5000 ocr-server
```

### 初始化数据库
```
>>> flask initdb
```

### 接口文档
[接口文档](./docs/api.md)


### 设计文档
[设计文档](./docs/design-document.md)
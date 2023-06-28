# HrmsTool-tamper

将HrmsTool与sqlmap进行联动

感谢[[vaycore](https://github.com/vaycore/HrmsTool/commits?author=vaycore)]提供的 [HrmsTool](https://github.com/vaycore/HrmsTool)

## 食用方式

修改tamper配置

```
#java环境路径（java 1.8）
java_path = r"path to\java.exe"
#HrmsTool.jar路径
hrms_tool_path = r"path to\HrmsTool.jar"
```

将=HrmsTool-tamper.py放入sqlmap的tamper目录下

sqlmap

```
sqlmap.py --tamper=HrmsTool-tamper 
```

举个栗子

![image-20230628214906533](./README/image-20230628214906533.png)

## 哦豁
实际用下来好像没啥叼用，就这样吧
欢迎各位师傅提交 Issue 和 Pull requests，一起完善

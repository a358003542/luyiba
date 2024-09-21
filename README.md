# luyiba
英雄联盟随机英雄选择器

安装用pip安装即可:
```
pip install luyiba
```

具体用法如下所示：

```
luyiba --help
```

或者

```
python -m luyiba --help
```



```
Usage: luyiba [OPTIONS]

  英雄联盟辅助小工具

Options:
  -v, --version                   本软件版本
  -V, --verbose                   打印输出冗余信息
  -l, --list                      列出全英雄名
  -m, --mode TEXT                 模式： all 全英雄随机 mylist 我的喜好清单随机 rank 排名列出模式
                                  [default: all]
  --rank [hot|ban|show|win]       根据什么排名，默认热门率  [default: hot]
  -n, --name TEXT                 指定英雄名字选取模式
  --number INTEGER                rank模式下显示数目  [default: 5]
  -p, --position [top|mid|jungle|bottom|support|t|m|j|b|s]
                                  指定我只想玩那个位置
  -r, --role [tank|mage|support|marksman|fighter|assassin|t|g|s|k|f|a]
                                  指定我只想玩某种角色
  --mylist-list                   列出我的喜好英雄清单
  --mylist-add TEXT               我的喜好清单添加一个
  --mylist-remove TEXT            我的喜好清单删除一个
  --mylist-delete                 我的喜好清单清空
  --help                          Show this message and exit.
```

## 基本使用

### 列出所有的英雄名字

```
luyiba -l
```

### 列出指定英雄信息

```
luyiba -n 百裂冥犬
```

### 随机选择英雄
默认随机选择英雄模式

```
luyiba 
```

### 个人喜好清单随机模式

```
luyiba -m mylist
```

### 个人喜好清单操作
需要你往个人喜好清单里面增删一些英雄，具体英雄名字可以通过 `luyiba -l` 来查看。

- `luyiba --mylist-add 寒冰射手` 将某个英雄添加到个人喜好清单
- `luyiba --mylist-list` 列出我的个人喜好清单
- `luyiba -m -p t` 从个人喜好清单中随机抽选一名上单

### 排名模式

```
luyiba -m rank 
```

rank排名模式支持 `--rank` 来指定具体的排名逻辑：

- hot 热门率排名 根据ban率加上选用率而来 这个热门率算法是我推荐的，可以看出当前版本那些英雄最超模
- ban ban率排名
- show 选用率排名
- win 胜率排名

### 过滤逻辑支持
所有模式均支持过滤逻辑的添加：

```
-p 位置过滤

-r 英雄角色过滤
```

目前提供了两种过滤， `--position` 和 `--role` ，比如说我想从我喜爱的英雄里面今天打上单：

```text
luyiba --position=top
```


比如说我今天打中路刺客

```text
luyiba --position=mid --role=assassin
```

 


## 视频讲解

[https://www.bilibili.com/video/BV1nK411K7wv](https://www.bilibili.com/video/BV1nK411K7wv)
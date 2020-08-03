# luyiba
英雄联盟随机英雄选择器

安装用pip安装即可:
```
pip install luyiba
```

具体用法如下所示：

```
Usage: luyiba [OPTIONS]

  英雄联盟随机英雄选择器

  默认全英雄随机选择，你可以设置为自己喜好的清单随机选择。

Options:
  -v, --version                   本软件版本
  -l, --list                      列出全英雄名
  --mylist-list                   列出我的喜好英雄清单
  --mylist-input PATH             读取文本导入我的喜好清单
  --mylist-add TEXT               我的喜好清单添加一个
  --mylist-remove TEXT            我的喜好清单删除一个
  --mylist-delete                 我的喜好清单清空
  -i, --input PATH                指定文本随机模式
  -a, --all                       全英雄随机模式
  -m, --mylist                    个人喜好清单随机模式
  -p, --position [top|mid|jungle|bottom|support|t|m|j|b|s]
                                  指定我只想玩那个位置
  -r, --role [tank|mage|support|marksman|fighter|assassin|t|g|s|k|f|a]
                                  指定我只想玩某种角色
  --help                          Show this message and exit.
```

## 基本使用
### 全英雄随机模式
- `luyiba -p t` 随机抽选一名上单

### 个人喜好清单随机模式
需要你往个人喜好清单里面增删一些英雄，具体英雄名字可以通过 `luyiba -l` 来查看。

- `luyiba --mylist-add 寒冰射手` 将某个英雄添加到个人喜好清单
- `luyiba --mylist-list` 列出我的个人喜好清单
- `luyiba -m -p t` 从个人喜好清单中随机抽选一名上单

## 亮点
1. 所有英雄数据不定时从英雄联盟官网获取，并保存在本地。

2. 用户可以提供一个自己喜好的英雄列表，然后从该列表中随机选择英雄。

3. 用户可以指定一个txt文件，然后从这个txt文件中随机选择一行。

4. 过滤模式： 目前提供了两种过滤， `--position` 和 `--role` ，比如说我想从我喜爱的英雄里面今天打上单：

```text
luyiba --position=top
```


比如说我今天打中路刺客

```text
luyiba --position=mid --role=assassin
```

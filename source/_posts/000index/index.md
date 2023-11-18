
# 待办事项
```dataview
	table time-played, length, rating, 标签 , tags
from ""
sort rating desc
```


# 目标

# 兴趣

# 最近的 50 条笔记（领域、文件夹、创建日期）
```dataview
table area, file.folder, file.cday
from ""
limit (50)
sort file.cday desc
```
```dataview
table file.标签
from ""
limit (50)
sort file.cday desc
```

# 获取标签为笔记的文件
```dataview
list from "" where contains(tags,"笔记") sort file.ctime desc
```

# dataviewjs
```dataviewjs
dv.list([1, 2, 3]) //生成一个1，2，3的列表
dv.list(dv.pages().file.name)  //生成所有文件的文件名列表
dv.list(dv.pages().file.link)  //生成所有文件的文件链接列表，即双链
dv.list(dv.pages("").file.标签.distinct()) //生成所有标签的列表
dv.list(dv.pages("#book").where(p => p.rating > 7)) //生成在标签 book 内所有评分大于 7 的书本列表
```
# 获取所有标签
```dataviewjs
dv.list(dv.pages("").标签.distinct()) //生成所有标签的列表

```

![[Pasted image 20230211160840.png]]


```dataviewjs
// dv.list(dv.pages())  //生成所有文件的文件名列表

dv.list(app.vault.getMarkdownFiles().标签)
```
```dataviewjs
let pages = dv.pages();


dv.table(["tag", "link"], pages

.map(d=>[d.tags, d.file.link])) //生成所有文件的文件名列表
```


```dataviewjs
// 修改标签
const tag = "#笔记"
// 获取 Obsidian 中的所有 Markdown 文件
const files = app.vault.getMarkdownFiles()
// 将带有标签的文件筛选出来
const taggedFiles = new Set(files.reduce((acc, file) => {
    const tags = app.metadataCache.getFileCache(file).tags
    if (tags) {
      let filtered = tags.filter(t => t.tag === tag)
      if (filtered) {
        return [...acc, file]
      }
    }
    return acc
}, []))

// 创建带有标签的行数组
const arr = Array.from(taggedFiles).map(async(file) => {
  const content = await app.vault.cachedRead(file)
const lines = await content.split("\n").filter(line => line.includes(tag))
return [file.name, lines]
})

// 生成表格
Promise.all(arr).then(values => {
dv.table(["file", "lines"], values)
})
````



```dataviewjs
let pages = dv.pages();
dv.list(pages)

```

​```

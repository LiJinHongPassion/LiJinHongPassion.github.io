---
优先级: 
开始时间: 2023-02-11 13:50
结束时间: 2023-02-11 13:50
剩余天数: 
tags:
- 学习/效率
- 学习/笔记/Obsidian安装
创建时间: 2023-02-11 13:50
---

# 安装过程

- 安装obsidian：https://obsidian.md/
- 配置插件下载地址：https://gitee.com/juqkai/obsidian-proxy-github；移动js文件至目录下；https://zhuanlan.zhihu.com/p/430538023
![[Pasted image 20230211124917.png]]
- 开启访问插件
![[Pasted image 20230211125057.png]]
- 下载dataview插件：开启dataviewjs的配置;[dataviewjs教程](https://zhuanlan.zhihu.com/p/373623264)
	dataview能自动的对每个页面添加大量的元数据。
	-   `file.name`: 该文件标题(字符串)。
	-   `file.folder`: 该文件所在的文件夹的路径(字符串)。
	-   `file.path`: 该文件的完整路径(字符串)。
	-   `file.link`: 该文件的一个链接(链接)。
	-   `file.size`: 该文件的大小(bytes)(数字)
	-   `file.ctime`: 该文件的创建日期(日期和时间)。
	-   `file.cday`: 该文件的创建日期(仅日期)。
	-   `file.mtime`: 该文件最后编辑日期(日期和时间)。
	-   `file.mday`: 该文件最后编辑日期(仅日期)。
	-   `file.tags`: 笔记中所有标签组成的数组。子标签按每个级别进行细分，所以`#Tag/1/A`将会在数组中储存为`[#Tag, #Tag/1, #Tag/1/A]`。
	-   `file.etags`: 笔记中所有显式标签组成的数组；不同于`file.tags`，不包含子标签。
	-   `file.outlinks`: 该文件所有外链(outgoing link)组成的数组。
	-   `file.aliases`: 笔记中所有别名组成的数组。
	
	如果文件的标题内有一个日期（格式为yyyy-mm-dd或yyyymmdd），或者有一个Date字段/inline字段，它也有以下属性:
	
	-   `file.day`: 一个该文件的隐含日期。
- 下载Templater插件：[[笔记模版（dataview）]]
- 下载Kanban插件
- 下载onedrive，用于数据同步


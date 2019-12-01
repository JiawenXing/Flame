# Flame
大数据分析作业相关
## crawler_12345.py
* 爬取网站：http://www.sh12345.gov.cn/r/cms/www/shline12345/appeal_public.html
* 爬取内容：每一诉求标题点进去后的诉求标题、提交时间、诉求内容、承办单位、办结时间、办结回复。例如http://www.sh12345.gov.cn/r/cms/www/shline12345/appeal_publicinfo.html
* 爬取数量：第一部分爬取了前1000条。第二部分的第一版本爬取了2019/1/1至今标题含有“垃圾”二字的信息；第二部分的第二版本爬取了2019/1/1至今内容含有“垃圾”二字的信息。
* 主要问题：
  1. 网站采用ajax异步刷新，例如第一页和第二页网页显示内容不同，但URL不变。
  2. 按网上的一些教程，找到Network - XHR - Headers里的Request URL，直接 requests.get url 并不能get到所需资源。
* 解决方案：
  1. 主要思路和常规处理ajax爬虫的思路一样。
  2. 对比浏览器在浏览http://www.sh12345.gov.cn/r/cms/www/shline12345/appeal_public.html 时XHR 显示get下一页的URL和浏览http://www.sh12345.gov.cn 时XHR显示get URL时Request Headers的区别，发现Referer不同，所以在代码中手动设置Referer即可！太坑了。

## crawler_peopleadvice.py
* 爬取网站：http://wsxf.sh.gov.cn/xf_rmyjzj/list.aspx?nav=&pageindex=1&pagesize=20
* 爬取内容：每一条诉求的建议标题、超链接、时间。
* 爬取数量：第一部分爬取了前1000条。第二部分爬取了2019/1/1至今标题含有“垃圾”二字的信息。
* 其他：
  1. 代码没有写将第二部分爬取内容保存至txt的部分。
  2. 代码没有写完爬取含垃圾二字的信息的二级网页的部分。

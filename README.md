- 框架：Django
- 语言：Python
- 算法：Item-to-Item CF

毕设项目，采用MovieLens 数据集（https://files.grouplens.org/datasets/movielens/ml-latest-small-README.html),由 610 名用户对 9742 部电影的 100836 个打分组成，评分
从 0.5 分到 5.0 分，0.5 分一个间隔，打分时间是 1996 年至 2018 年。

<br>**算法处理后的相似度数据如下：**

<img src="https://github.com/yutian-9264/CF-Recommendation-System-with-Django/blob/main/Photo-example/8.png" width="600">

<br>**演示效果如下：**<br>
(更多演示图片请查看“Photo-example”文件夹)

<img src="https://github.com/yutian-9264/CF-Recommendation-System-with-Django/blob/main/Photo-example/3.png" width="300">
<img src="https://github.com/yutian-9264/CF-Recommendation-System-with-Django/blob/main/Photo-example/4.png" width="450">
<img src="https://github.com/yutian-9264/CF-Recommendation-System-with-Django/blob/main/Photo-example/5.png" width="450">

<br>**系统可实现的功能：**
- 登录注册
- 点击电影进行打分，并可查看喜爱类型分布饼状图
- 查看推荐电影，及它们的类型分布饼状图

<br>**不足之处：**
- 没有解决冷启动问题
- 不能增删电影打分，交互性不好
- 电影名称没有转换成中文
- 没有搜索功能
- 界面问题





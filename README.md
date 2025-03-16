<div align="center">
  <h1 align="center">
    <img src="icon.png" width="200"/>
    <br/>
    ok-ww
  </h1> 
<h3><i>基于图像识别的鸣潮自动化, 使用windows接口模拟用户点击, 无读取游戏内存或侵入修改游戏文件/数据.</i></h3>
</div>

![Static Badge](https://img.shields.io/badge/platfrom-Windows-blue?color=blue)
[![GitHub release (with filter)](https://img.shields.io/github/v/release/ok-oldking/ok-wuthering-waves)](https://github.com/ok-oldking/ok-wuthering-waves/releases)
[![GitHub all releases](https://img.shields.io/github/downloads/ok-oldking/ok-wuthering-waves/total)](https://github.com/ok-oldking/ok-wuthering-waves/releases)

### [English Readme](README_en.md) | 中文说明

演示和教程 [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtu.be/apalaRDDmVw)

# 免责声明

本软件是一个外部工具，旨在自动化鸣潮的游戏玩法。它仅通过现有用户界面与游戏交互，并遵守相关法律法规。该软件包旨在简化用户与游戏的交互，不会破坏游戏平衡或提供不公平优势，也不会修改任何游戏文件或代码。

本软件开源、免费，仅供个人学习交流使用，仅限于个人游戏账号，不得用于任何商业或营利性目的。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目及开发者团队无关。若您发现商家使用本软件进行代练并收费，这是商家的个人行为，本软件不授权用于代练服务，产生的问题及后果与本软件无关。本软件不授权任何人进行售卖，售卖的软件可能被加入恶意代码，导致游戏账号或电脑资料被盗，与本软件无关。

请注意，根据库洛的《鸣潮》公平运营声明:

```
严禁利用任何第三方工具破坏游戏体验。
我们将严厉打击使用外挂、加速器、作弊软件、宏脚本等违规工具的行为，这些行为包括但不限于自动挂机、技能加速、无敌模式、瞬移、修改游戏数据等操作。
一经查证，我们将视违规情况和次数，采取包括但不限于扣除违规收益、冻结或永久封禁游戏账号等措施。
```

### 使用说明

* 点击[releases](https://github.com/ok-oldking/ok-wuthering-waves/releases), 下载7z压缩包(200M左右的), 解压缩双击运行.exe

### 有多强?

1. 4K分辨率流畅运行,支持所有16:9分辨率,1600x900以上, 1280x720不支持是因为鸣潮bug, 它的1280x720并不是1280x720.
   部分功能也可以在21:9等宽屏分辨率运行
2. 可后台运行,可窗口化,可全屏,屏幕缩放比例无要求
3. 全角色自动识别，无需配置出招表，一键运行
4. 后台自动静音游戏

### 出现问题请检查

有问题点这里, 挨个检查再提问:

1. **解压问题:** 将压缩包解压到仅包含英文字符的目录中。
2. **杀毒软件干扰:** 将下载和解压目录添加到您的杀毒软件/Windows Defender 白名单中。
3. **显示设置:** 禁用 Windows HDR、护眼模式和自动颜色管理。使用默认游戏亮度并禁用在游戏上显示FPS(如小飞机)。
4. **自定义按键绑定:** 如没有使用默认按键，请在APP设置中设置, 不在设置里的按键不支持。
5. **版本过旧:** 确保您使用的是最新版本的 OK-GI。
6. **性能:** 在游戏中保持稳定的 60 FPS，如果需要，降低分辨率。
7. **进一步帮助:** 如果问题仍然存在，请提交错误报告。

### Usage (Python Source Code)

Use Python 3.12，other versions might work but are not tested.

```
pip install -r requirements.txt #install python dependencies
python main.py # run the release version
python main_debug.py # run the debug version
python main_gpu_debug.py # run the gpu debug version
python main_gpu.py # run the gpu release version
```

### 命令行参数

```
ok-ww.exe -t 1 -e
```

- -t 或 --task 代表启动后自动执行第几个任务, 1就是第一个, 一条龙任务
- -e 或 --exit 加上代表如果执行完任务之后自动退出

### 加入我们

* 由于基于[ok-script](https://github.com/ok-oldking/ok-script)开发，项目代码仅有3000行（Python），简单易维护
* 鸣潮水群 970523295 933070924 进群答案:老王同学OK
* 有兴趣的请加开发者群926858895

### 致谢

[https://github.com/lazydog28/mc_auto_boss](https://github.com/lazydog28/mc_auto_boss) 后台点击代码
  

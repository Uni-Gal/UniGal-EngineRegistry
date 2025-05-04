# UniGal-EngineRegistry

本项目旨在为每个视觉小说引擎赋予一个用于标识的唯一性代码以便 normalize 后统计使用，会收录尽可能多的其名称的变体，并收录引擎对应的语言、语法、授权协议等信息。

<!-- MARKDOWN_TABLE BEGIN -->
<!-- WARNING: THIS TABLE IS MAINTAINED BY PROGRAMME, YOU SHOULD ADD DATA TO COLLECTION JSON -->
| 引擎唯一标识 | 引擎名称 | 引擎技术栈语言 | 引擎脚本语言 | 存活状态 | UniGal适配程度 | 双向导入导出 | 可从Unigal导入 | 可导出为Unigal | 是否自由 | 官方网站或仓库 |
| - | - | - | - | - | - | - | - | - | - | - |
|  | Ayaka | rust | ayaka script | 活跃 | 语法简单适合标准方研究支持 |  |  |  | MIT | https://github.com/Uni-Gal/Ayaka |
|  | Ink | js | YAML | 活跃 | 语法简单适合标准方研究支持 |  |  |  | MIT | https://www.inklestudios.com/ink/ |
|  | VNFrameworkCore | 未知 | C# | 活跃 | 语法简单适合标准方研究支持 |  |  |  | MIT | https://github.com/soryu-ryouji/VNFrameworkCore |
|  | AVG.js | js | json | 未知 |  |  |  | √（开发中） |  |  |
|  | AVGPlus | js | json | **活跃** | （考虑要不要联系开发者） |  |  | √（开发中） |  | https://avg-engine.com/ |
|  | BKEngine | 面包工坊 | bkspr (.bkspr) | 已停止维护 |  |  | √（开发中） |  |  | https://bke.bakery.moe/index.html |
|  | EvkWorld幻境 | 橙光 | 可视化 | 未知 | 暂无计划 |  |  |  |  |  |
|  | GameCreator | json | 未知 | **活跃** | （考虑要不要联系开发者） |  |  | √（开发中） |  |  |
|  | Krkr | Krkr | TJS | 已停止维护 |  |  |  | √（开发中） |  |  |
|  | Librian | Python | liber | **活跃** | （正在说服开发者） | √（开发中） | √（开发中） | √（开发中） |  | http://librian.net/ |
|  | Monogatari | json | json | **活跃** |  |  |  | √（开发中） |  | https://monogatari.io |
|  | Renjs | js | javascript | 未知 |  |  |  | √（开发中） |  |  |
|  | Renpy | Python | Python (.rpy) | **活跃** |  |  |  | √（开发中） |  | https://www.renpy.org/ |
|  | Unity-Fungus | Unity | C# | **活跃** | 暂无计划 |  |  |  |  |  |
|  | Unity-Kirino-Engine | Unity | C# | 已停止维护 | 暂无计划 |  |  |  |  |  |
|  | Unity-Utage | Unity | C# | **活跃** | 暂无计划 |  |  |  |  |  |
|  | Unity-XiheAnimation | Unity | C# | 未知 | 暂无计划 |  |  |  |  |  |
|  | VoidMatrix系列 | SDL | C++ | **活跃** | （正在与开发者合作，已经提供XML读取支持了） | √（开发中） | √（开发中） | √（开发中） |  |  |
|  | WebGal | js | 未知 | 未知 |  |  |  | √（开发中） |  | https://github.com/MakinoharaShoko/WebGAL |
|  | YukimiScript | Strrationalism | C++ | 不能理解它到底有多少是属于非Galgame的，处于观察中 |  |  |  | √（艰难开发中） |  | https://github.com/Strrationalism/YukimiScript |
|  | [Unity-Naninovel](https://naninovel.com/guide/naninovel-scripts.html) | Unity | JS (.nani) | **活跃** | 做梦 | 做梦 | 做梦 | √（开发中） |  | https://naninovel.com/ |
|  | [Unity-Nova](https://github.com/Lunatic-Works/Nova/wiki/NovaScript) | Unity | Lua/C# (.txt) | **活跃** | （正在说服开发者） | √（开发中） | √（开发中） | √（开发中） |  | https://github.com/Lunatic-Works/Nova |
|  | iFAction | 橙光 | 可视化 | 活跃 | 暂无计划 |  |  |  |  |  |
|  | 橙光文字游戏制作工具 | 橙光 | 可视化 | **生不如死** | 暂无计划 |  |  |  |  |  |

<!-- MARKDOWN_TABLE END -->

需要注意的是，大部分DSL并未收录在[github/linguist](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)里。

另可参考如下网友根据其破解和解包经验完善的引擎与代表作信息。请注意，我们不鼓励破解和反编译等逆向工程。

+ YeLikesss的 https://github.com/YeLikesss/CNGALTools 
+ 2439905184的 https://github.com/2439905184/Galgame-Engine-Collect#%E6%AD%A3%E9%A2%98

## 目前各类语言的编辑器支持详表

编辑器支持包含语言引擎（LSP）支持和语法高亮支持两部分。

| 引擎 | 对应文档 | 支持的编辑器 | 仓库 |
|-|-|-|-|
| BKEngine | [BKE官方教程](http://docs.bakery.moe/faq) | Sublime | [AllanZyne/BKS4Sublime](https://github.com/AllanZyne/BKS4Sublime) |
| BKEngine | - | VSCode | [BKEngine/vscode-bkscr](https://github.com/BKEngine/vscode-bkscr) |
| Librian | - | Sublime | [RimoChan/Librian](https://github.com/RimoChan/Librian/tree/master/librian/librian%E6%9C%AC%E9%AB%94/%E5%9C%9F%E7%89%B9%E7%94%A2) |
| Unity-Nova | - | VSCode | [zhouhaoyu/vscode-nova-script](https://github.com/zhouhaoyu/vscode-nova-script) |
| Naninovel | [Guide](https://naninovel.com/guide/ide-extension) | VSCode | [Naninovel/VSCode](https://github.com/Naninovel/VSCode) |

注意，以上部分引擎的编辑器支持开发者维护较缓慢，可能不适合非开发者使用。

## 耻辱柱

橙光文字游戏制作工具：**业界毒瘤**，捆绑平台，逼迫作者吊死在自家一颗树上

iFAction：是商业引擎并有基于账号云端验证的加密功能，作品的打开需要掌握在引擎制作方的手里，提供导出工具既与开发者的盈利和用户素材安全违背，又不符合本项目开放的初衷。

EvkWorld：曾经以群邮件的形式大量向使用者推销官方的打卡课程。并且该引擎并非专注于AVG，而是杂糅式的的多功能引擎，但又高度依赖模板，在AVG的可扩展空间不一定足够大。

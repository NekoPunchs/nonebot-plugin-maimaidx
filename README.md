<div align='center'>

<a><img src='https://raw.githubusercontent.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx/master/favicon.png' width='200px' height='200px' akt='maimaidx'></a>

[![python3](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![QQGroup](https://img.shields.io/badge/QQGroup-Join-blue)](https://qm.qq.com/q/gDIf3fGSPe)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

</div>

## 重要更新

**2025-03-28**

> [!WARNING]
> 对于这个版本之前的插件和修改版的插件请注意，预更新版本别名库将全部更换成新的 `API` 地址，返回的数据结构均更改，目前旧版 `API` 将再运行一段时间，预计正式更新 `舞萌DX2025` 时将会关闭

1. 预更新 `舞萌DX2025` UI，资源全部更换，更新部分依赖和文件，**请重新进行安装**

## 安装

1. 安装 `nonebot-plugin-maimaidx`
    - 使用源代码 **需自行安装额外依赖**
        ``` git
        git clone https://github.com/NekoPunchs/nonebot-plugin-maimaidx.git
        ```

> [!WARNING]
> `ginfo` 指令已删除

## 配置
   
1. 下载静态资源文件，将该压缩文件解压，且解压完为文件夹 `static`
   - [AList网盘](https://shadowdr.cn/disk/maimaiDX)

2. 在 `.env` 文件中配置静态文件绝对路径 `MAIMAIDX_PATH`

    ``` dotenv
    MAIMAIDX_PATH=path.to.static

    # 例如 windows 平台，非 "管理员模式" 运行Bot尽量避免存放在C盘
    MAIMAIDX_PATH=D:\bot\static
    # 例如 linux 平台
    MAIMAIDX_PATH=/root/static
    ```

3. 可选，如果拥有 `diving-fish 查分器` 的开发者 `Token`，请在 `.env` 文件中配置 `MAIMAIDX_TOKEN`
   
    ``` dotenv
    MAIMAIDX_TOKEN=MAIMAITOKEN
    ```

4. 可选，如果你的服务器或主机不能顺利流畅的访问查分器和别名库的API，请在 `.env` 文件中配置代理。均为香港服务器代理中转，例如你的服务器访问查分器很困难，请设置 `MAIMAIDX_PROBER_PROXY` 为 `ture`，别名库同理

    ``` dotenv
    # 查分器代理，推荐境外服务器使用
    MAIMAIDX_PROBER_PROXY=false
    # 别名代理，推荐国内服务器使用
    MAIMAIDX_ALIAS_PROXY=false
    ```
5. 可选，如果需要节省服务器带宽外出流量，请在 `.env` 文件中配置 `MAIMAIDX_IMAGE_QUALITY`，范围20~100

   ``` dotenv
    MAIMAIDX_IMAGE_QUALITY=50
    ```

> [!NOTE]
> 安装完插件需要使用定数表或完成表指令时，需私聊Bot使用 `更新定数表` 和 `更新完成表` 进行生成

> [!NOTE]
> 插件带有别名更新推送功能，如果不需要请私聊Bot使用 `全局关闭别名推送` 指令关闭所有群组推送

## 指令

![img](https://raw.githubusercontent.com/Yuri-YuzuChaN/nonebot-plugin-maimaidx/master/nonebot_plugin_maimaidx/maimaidxhelp.png)

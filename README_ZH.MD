# QuecPython 可穿戴解决方案

中文 | [English](README.MD)

欢迎来到 QuecPython 可穿戴解决方案仓库！本仓库提供了一个全面的解决方案，用于使用 QuecPython 开发可穿戴设备应用程序。

## 目录

- [介绍](#介绍)
- [功能](#功能)
- [快速开始](#快速开始)
  - [先决条件](#先决条件)
  - [安装](#安装)
  - [运行应用程序](#运行应用程序)
- [目录结构](#目录结构)
- [使用](#使用)
- [贡献](#贡献)
- [许可证](#许可证)
- [支持](#支持)

## 介绍

QuecPython 推出了针对穿戴行业的 GUI 解决方案，包括时钟显示、拨打/接听电话、心率/体温/血氧测量、步数显示、系统设置及其他可选功能。

![可穿戴解决方案](./docs/zh/media/image-20231124092228717.png)

穿戴行业方案使用 [LVGL](https://lvgl.io/) 绘制图形化界面，它是一个轻量级的、开源的嵌入式图形库。QuecPython 集成了 LVGL，并且使用 NXP 公司的 [GUI Guider](https://www.nxp.com/design/software/development-software/gui-guider:GUI-GUIDER) 作为图形化界面设计工具，能自动生成 QuecPython 代码，极大提高了嵌入式平台图形化界面设计的效率。

## 功能

- **时钟显示**：具有实时更新的数字和模拟时钟界面。
- **健康监测**：心率、体温和血氧测量。
- **活动追踪**：步数显示和目标设置。
- **通信**：拨打和接听电话，聊天功能。
- **系统设置**：设备信息、系统升级、表盘设置、铃声设置、振动模式、恢复出厂设置、关机。

## 快速开始

### 先决条件

在开始之前，请确保您具备以下先决条件：

- **硬件**：
  - 一块 QuecPython 可穿戴开发板
  - USB 数据线（USB-A 转 USB-C）
  - 电脑（Windows 7、Windows 10 或 Windows 11）

- **软件**：
  - QuecPython 模块的 USB 驱动
  - QPYcom 调试工具
  - QuecPython 固件及相关软件资源
  - Python 文本编辑器（例如，[VSCode](https://code.visualstudio.com/)、[Pycharm](https://www.jetbrains.com/pycharm/download/)）

### 安装

1. **克隆仓库**：
   ```bash
   git clone https://github.com/QuecPython/solution-wearable.git
   cd solution-wearable
   ```

2. **烧录固件**：
   按照[说明](https://python.quectel.com/doc/Application_guide/dev-tools/QPYcom/qpycom-dw.html#Download-Firmware)将固件烧录到开发板上。

### 运行应用程序

1. **连接硬件**：
   - 使用 USB 数据线将开发板连接到计算机的 USB 端口。

2. **将代码下载到设备**：
   - 启动 QPYcom 调试工具。
   - 将数据线连接到计算机。
   - 按下开发板上的 **PWRKEY** 按钮启动设备。
   - 按照[说明](https://python.quectel.com/doc/Application_guide/zh/dev-tools/QPYcom/qpycom-dw.html#Download-Script)将 `code` 文件夹中的所有文件导入到模块的文件系统中，保留目录结构。

3. **运行应用程序**：
   - 选择 `File` 选项卡。
   - 选择 `main_t.py` 脚本。
   - 右键单击并选择 `Run` 或使用`运行`快捷按钮执行脚本。

## 目录结构

```plaintext
solution-wearable/
├── code/
│   ├── EventMesh.py        # 事件管理模块
│   ├── common.py           # 公共工具和基类
│   ├── constant.py         # 常量配置
│   ├── lcd.py              # LCD 和 TP 驱动初始化
│   ├── css.py              # CSS 样式和字体样式
│   ├── ui.py               # UI 屏幕类和接口逻辑
│   ├── mgr.py              # 后台功能和管理器
│   ├── main_t.py           # 应用程序入口脚本
│   ├── 16px.bin            # 字体文件
│   ├── 28px.bin            # 字体文件
│   ├── 56px.bin            # 字体文件
│   ├── img/                # 图片资源
│   │   ├── point.png
│   │   ├── gps.png
│   │   ├── bat4.png
│   │   └── ...png
└── README.md               # 本 README 文件
```

## 使用

点击[这里](https://python.quectel.com/doc/Application_guide/zh/solutions/Wear/index.html)查看可穿戴解决方案的详细实现。

## 贡献

我们欢迎对本项目的改进做出贡献！请按照以下步骤进行贡献：

1. Fork 此仓库。
2. 创建一个新分支（`git checkout -b feature/your-feature`）。
3. 提交您的更改（`git commit -m 'Add your feature'`）。
4. 推送到分支（`git push origin feature/your-feature`）。
5. 打开一个 Pull Request。

## 许可证

本项目使用 Apache 许可证。详细信息请参阅 [LICENSE](LICENSE) 文件。

## 支持

如果您有任何问题或需要支持，请参阅 [QuecPython 文档](https://python.quectel.com/doc) 或在本仓库中打开一个 issue。

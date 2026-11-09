# WQFiles v0.3 简体中文源码补丁（实验性）

本补丁基于用户上传的 WQFiles 0.3 IPA 中实际提取出的可见字符串整理，不是 IPA，也不是已经编译的应用。

## 内容
- `zh-Hans.json`：英文原文与简体中文映射
- `translation.csv`：可查看的中英文对照表
- `apply_zh_hans.py`：在官方源码目录中替换匹配到的 Objective-C 字符串，并修改显示名称

## 使用方法
1. 从官方仓库下载 v0.3 对应的 Source code ZIP，并解压。
2. 将本补丁中的三个文件复制到源码根目录（与 `main.m`、`WQAccess.m`、`Info.plist` 同一层）。
3. 在有 Python 3 的环境运行：`python3 apply_zh_hans.py`
4. 使用 macOS/Xcode 按官方 `build.sh` 编译 arm64，并签入 `group.cz.kolbi.wqfiles` App Group entitlement。
5. 重新签名时必须保留 App Group entitlement；否则应用无法访问其依赖的其他容器。

## 重要限制
- 本补丁只修改源码中的精确英文字符串，不会从 IPA 直接生成可安装包。
- 该项目使用原生 UIKit 字符串，不是可通过简单添加 `.lproj` 文件自动汉化的标准本地化工程。
- 当前执行环境没有 Apple Xcode/iOS SDK，不能在这里完成 iOS 编译、签名或设备验证。
- 不要把未签名或未经验证的 IPA 安装到主力设备。
- GPL-3.0-or-later：分发修改版时需遵守原项目许可证及源码提供义务。

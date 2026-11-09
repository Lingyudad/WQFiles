# WQFiles v0.3 简体中文云端编译包

## 目标
在 GitHub Actions 的 macOS runner 上尝试编译 WQFiles v0.3 arm64 IPA。此工作流不会上传 Apple ID、证书或密码。

## 手机端操作概览
1. 登录 GitHub，在官方仓库 https://github.com/kolbicz/WQFiles 点击 Fork，创建自己的副本。
2. 在自己的 Fork 仓库中，依次上传本目录内的 `zh-Hans.json`、`translation.csv`、`apply_zh_hans.py` 到仓库根目录。
3. 同时上传 `.github/workflows/build-zh-hans.yml`，GitHub 会将它放到 `.github/workflows/`。
4. 打开自己仓库的 Actions 页面，若提示需启用 Actions，先启用；选择 “Build WQFiles Simplified Chinese IPA”，点 Run workflow。
5. 等待工作流结束，打开成功的运行记录，在 Artifacts 下载 `WQFiles-v0.3-zh-Hans-unsigned-for-sideloading`。

## 重要说明
- 工作流固定从 `v0.3` 标签取源码；如果官方仓库没有这个 tag，工作流会在 Checkout 步骤失败。
- 翻译脚本只替换源码中与翻译表完全一致的 Objective-C 字符串。若显示 “No source literals matched”，表示源码版本或字符串格式不匹配，不要继续安装。
- `build.sh` 生成的是 ad-hoc 签名 IPA，不等于已通过 SideStore 签名的可安装包。导入 SideStore 前需要确认 SideStore 的重签名过程保留 `group.cz.kolbi.wqfiles` App Group entitlement；官方 README 明确指出丢失此权限会导致功能不可用。
- 本项目为 GPL-3.0-or-later。修改和再分发时遵守许可证要求。
- 该流程只编译，不保证在 iOS 27.0.1 上功能正常；安装前请保留原版 IPA，并先在非关键环境验证。

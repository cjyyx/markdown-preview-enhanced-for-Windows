# markdown-preview-enhanced-for-Windows

## 简介

[Markdown Preview Enhanced](https://github.com/shd101wyy/vscode-markdown-preview-enhanced) 是 vscode 上最强大的 markdown 预览扩展之一。但是每次查看 markdown 文件都要打开 vscode 非常麻烦。幸运的是 Markdown Preview Enhanced 基于的 markdown 解析引擎 [crossnote](https://github.com/shd101wyy/crossnote) 也是开源的。因此我基于 crossnote 写了一款可以直接打开 markdown 文件的 Windows 应用。

## 安装

1. 确保已经安装了 node.js 且配置环境变量，比如在终端中运行 `node -v` 会看到版本号
2. 在 [Github Release](https://github.com/cjyyx/markdown-preview-enhanced-for-Windows/releases) 上下载 crossnote.zip，解压后双击 setup.cmd
3. 打开任意 markdown 文件时，选择始终用 crossnote.exe 打开

## 原理

crossnote 是一个 nodeJS 包，提供一个 api 可以把 markdown 文件解析为 html 文件并用浏览器打开。于是可以写一个 js 脚本，查看 markdown 文件。我使用 gcc 构建了一个 Windows 应用程序，该程序调用 node 运行 js 脚本，从而实现查看 markdown 文件。

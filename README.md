# CutAuto - 剪映草稿自动化助手 | CapCut Draft Automation Assistant

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**[中文](#中文) | [English](#english)**

</div>

---

<a name="中文"></a>
## 中文

### 简介

**剪映草稿自动化助手 (CutAuto)** 是一个基于 Python + FastAPI 开发的后端服务，旨在帮助用户快速批量化生成剪映视频草稿。通过加载预定义的剪映模板并替换其中的素材，用户可以在短时间内生成大量专业水准的视频草稿。

### 功能特性

- **模板加载**：支持加载剪映模板工程，自动解析草稿结构
- **素材替换**：支持替换视频、音频、图片、文本等多种素材类型
- **多轨编辑**：支持视频轨、音频轨、文本轨、特效轨等多轨道编辑
- **特效配置**：支持视频特效、转场、滤镜、动画等特效配置
- **批量生成**：通过 API 接口快速批量生成视频草稿
- **草稿导出**：生成标准剪映草稿格式，可直接导入剪映客户端

### 技术栈

| 组件 | 版本 | 说明 |
|------|------|------|
| Python | 3.11+ | 编程语言 |
| FastAPI | 0.100+ | Web 框架 |
| uv | 最新版 | 包管理工具 |
| Docker | - | 容器化部署 |
| pymediainfo | 7.0+ | 媒体信息解析 |

### 快速开始

#### 方式一：Docker 部署（推荐）

```bash
# 克隆项目
git clone <repository-url>
cd CutAuto

# 使用 Docker Compose 启动
docker-compose up -d
```

#### 方式二：本地运行

```bash
# 1. 安装 uv
pip install uv

# 2. 安装依赖
uv sync

# 3. 启动服务
uv run main.py
```

服务启动后，访问 `http://localhost:30000` 即可使用 API。

### API 接口

#### 创建草稿

```http
POST /openapi/cutauto/v1/create_draft
```

**请求参数：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| tpl_name | string | 是 | 模板名称 |

**响应示例：**

```json
{
  "draft_url": "https://example.com/openapi/cutauto/v1/get_draft?draft_id=xxx",
  "tip_url": "https://docs.jcaigc.cn/"
}
```

#### 使用指定模板创建草稿

```http
POST /openapi/cutauto/v1/mashup688001
```

使用 688001 模板快速创建草稿。

### 项目结构

```
CutAuto/
├── src/
│   ├── pyJianYingDraft/    # 剪映草稿核心库
│   │   ├── script_file.py   # 草稿文件操作
│   │   ├── track.py         # 轨道管理
│   │   ├── segment.py       # 片段管理
│   │   └── metadata/        # 特效元数据
│   ├── router/              # API 路由
│   ├── service/             # 业务逻辑
│   ├── schemas/             # 数据模型
│   ├── middlewares/         # 中间件
│   └── utils/               # 工具函数
├── tpls/                    # 模板目录
├── main.py                  # 应用入口
├── config.py                # 配置文件
├── pyproject.toml           # 项目依赖
├── Dockerfile               # Docker 镜像
└── docker-compose.yaml      # Docker Compose 配置
```

### 环境变量

| 变量名 | 默认值 | 说明 |
|--------|--------|------|
| DRAFT_URL | - | 草稿下载 URL |
| DOWNLOAD_URL | - | 文件下载 URL |
| TIP_URL | - | 帮助文档 URL |
| DOWNLOAD_FILE_SIZE_LIMIT | 209715200 | 文件下载大小限制（字节）|

### 许可证

本项目基于 [MIT License](LICENSE) 开源。

---

<a name="english"></a>
## English

### Introduction

**CutAuto (CapCut Draft Automation Assistant)** is a backend service built with Python + FastAPI, designed to help users quickly generate CapCut video drafts in batches. By loading predefined CapCut templates and replacing the materials within, users can generate a large number of professional-quality video drafts in a short time.

### Features

- **Template Loading**: Support loading CapCut template projects and automatically parsing draft structures
- **Material Replacement**: Support replacing various material types including video, audio, images, and text
- **Multi-track Editing**: Support multi-track editing for video, audio, text, and effect tracks
- **Effect Configuration**: Support video effects, transitions, filters, animations, and other effect configurations
- **Batch Generation**: Quickly generate video drafts in batches through API interfaces
- **Draft Export**: Generate standard CapCut draft formats that can be directly imported into the CapCut client

### Tech Stack

| Component | Version | Description |
|-----------|---------|-------------|
| Python | 3.11+ | Programming Language |
| FastAPI | 0.100+ | Web Framework |
| uv | Latest | Package Manager |
| Docker | - | Containerized Deployment |
| pymediainfo | 7.0+ | Media Information Parser |

### Quick Start

#### Option 1: Docker Deployment (Recommended)

```bash
# Clone the project
git clone <repository-url>
cd CutAuto

# Start with Docker Compose
docker-compose up -d
```

#### Option 2: Local Development

```bash
# 1. Install uv
pip install uv

# 2. Install dependencies
uv sync

# 3. Start the service
uv run main.py
```

Once the service is started, access the API at `http://localhost:30000`.

### API Endpoints

#### Create Draft

```http
POST /openapi/cutauto/v1/create_draft
```

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tpl_name | string | Yes | Template name |

**Response Example:**

```json
{
  "draft_url": "https://example.com/openapi/cutauto/v1/get_draft?draft_id=xxx",
  "tip_url": "https://docs.jcaigc.cn/"
}
```

#### Create Draft with Specific Template

```http
POST /openapi/cutauto/v1/mashup688001
```

Quickly create a draft using the 688001 template.

### Project Structure

```
CutAuto/
├── src/
│   ├── pyJianYingDraft/    # CapCut Draft Core Library
│   │   ├── script_file.py   # Draft file operations
│   │   ├── track.py         # Track management
│   │   ├── segment.py       # Segment management
│   │   └── metadata/        # Effect metadata
│   ├── router/              # API routes
│   ├── service/             # Business logic
│   ├── schemas/             # Data models
│   ├── middlewares/         # Middleware
│   └── utils/               # Utility functions
├── tpls/                    # Template directory
├── main.py                  # Application entry
├── config.py                # Configuration file
├── pyproject.toml           # Project dependencies
├── Dockerfile               # Docker image
└── docker-compose.yaml      # Docker Compose configuration
```

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| DRAFT_URL | - | Draft download URL |
| DOWNLOAD_URL | - | File download URL |
| TIP_URL | - | Help documentation URL |
| DOWNLOAD_FILE_SIZE_LIMIT | 209715200 | File download size limit (bytes) |

### License

This project is open-sourced under the [MIT License](LICENSE).

---

<div align="center">

**Made with ❤️ for CapCut Automation**

</div>

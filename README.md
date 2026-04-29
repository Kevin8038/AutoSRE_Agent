# 🤖 AutoSRE Agent

> **企业级微服务全链路智能排障与自愈系统**  
> 基于大型语言模型（LLM）与多智能体（Multi-Agent）架构，实现从“告警接收”到“自动排障”，再到“自愈止血”与“总结复盘”的全生命周期自动化闭环。

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![OpenAI](https://img.shields.io/badge/LLM-OpenAI%20%7C%20DeepSeek-green)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## 🎯 1. 解决的核心痛点

在云原生微服务架构下，研发与 SRE（网站可靠性工程师）团队常常面临以下挑战，本项目致力于解决这些痛点：

1. **告警风暴与信息孤岛：** 一次 P0 故障往往引发成百上千条连锁告警。排障人员需要在监控（Prometheus）、日志（ELK）、链路追踪（Jaeger）等多个割裂的系统中来回切换，面临严重的“告警疲劳”。
2. **根因定位极其耗时：** 传统的排障高度依赖个人经验，手动查询 TraceID、对比代码库（Git Commits）和发版记录认知负荷大，导致 MTTR（平均恢复时间）居高不下。
3. **缺乏自动化闭环：** 定位问题后，执行回滚、扩容或提交修复代码仍需大量人工介入，缺乏敏捷的自愈手段。

---

## 🧠 2. 核心逻辑流：多 Agent 协作与长链推理

本系统摒弃了单体模型的局限，采用 **4 个专职 Agent** 协同工作流，并引入 **ReAct 长链推理** 机制，模拟资深 SRE 专家的思考路径。

### 📊 Agent 协作架构

```mermaid
graph TD
    A[Prometheus/Webhook 告警流] -->|海量告警| B(Triage Agent<br>告警降噪与事件提取)
    B -->|核心异常事件| C(Diagnostic Agent<br>长链推理与根因定位)
    
    C -->|Tool Call 1| DB[(查询 Metrics/连接池)]
    C -->|Tool Call 2| ES[(查询 ES 错误日志)]
    C -->|Tool Call 3| TR[(查询 Jaeger 链路)]
    C -->|Tool Call 4| GIT[(比对 GitHub 代码变更)]
    
    C -->|确诊根因| D(Action Agent<br>自愈策略与修复执行)
    D -->|回滚脚本/扩容/Hotfix PR| E(运维平台 / CI/CD)
    
    D -->|执行结果| F(Knowledge Agent<br>复盘与文档沉淀)
    F -->|Markdown RCA 报告| WIKI[(企业知识库)]

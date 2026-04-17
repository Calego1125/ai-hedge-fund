# 开发路线图

> 目标：从零到一构建自主交易的 AI 对冲基金
> 状态：🚀 基础设施已就绪

## Phase 1: 核心引擎 (当前)
- [x] 项目结构初始化
- [x] Agent 基类定义
- [x] Alpha Generator (信号生成)
- [ ] Risk Manager (风控)
- [ ] Execution Agent (执行)
- [ ] State Manager (状态共享)

## Phase 2: 数据与回测
- [ ] 数据源接入 (Yahoo Finance / Tushare)
- [ ] 历史数据清洗与存储
- [ ] 回测引擎 (Backtrader 集成)
- [ ] 绩效评估指标 (Sharpe, Max Drawdown, Win Rate)

## Phase 3: 策略进化
- [ ] 多因子模型 (Momentum + Value + Volatility)
- [ ] 动态权重调整 (基于 Ralph 评分机制)
- [ ] 强化学习优化 (PPO/DQN 用于仓位管理)

## Phase 4: 实盘部署
- [ ] 模拟交易对接
- [ ] 实盘交易 API 接入
- [ ] 异常监控与自动熔断
- [ ] Feishu 实时报告

## 下一步建议
**现在可以开始：**
1. 完善 `RiskManager`，实现 Kelly 公式和最大回撤控制。
2. 编写第一个回测脚本，验证 `AlphaGenerator` 信号。
3. 配置 Tushare API 获取 A 股数据。

from agents.monitor_agent import MonitorAgent
from agents.diagnostic_agent import DiagnosticAgent
from agents.action_agent import ActionAgent
from agents.report_agent import ReportAgent

def main():
    print("="*50)
    print("启动 AutoSRE Multi-Agent 排障系统模拟")
    print("="*50)
    
    # 模拟从监控系统收到的海量噪音告警
    raw_alerts = "[ALARM] CPU > 90%, [ALARM] HTTP 504, [ALARM] DB connections maxed..."
    
    # 初始化 Agents
    monitor = MonitorAgent()
    diagnoser = DiagnosticAgent()
    actioner = ActionAgent()
    reporter = ReportAgent()
    
    # Agent 协同工作流
    core_event = monitor.analyze_alerts(raw_alerts)
    root_cause = diagnoser.trace_root_cause(core_event)
    fix_plan = actioner.generate_fix(root_cause)
    rca_report = reporter.generate_rca(core_event, root_cause, fix_plan)
    
    print("\n" + "="*50)
    print("故障处理闭环完成，系统已恢复！")
    print("="*50)

if __name__ == "__main__":
    main()

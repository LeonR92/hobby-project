def generate_markdown_report(design_data, pricing_data) -> str:
    """
    Combines Architecture and Pricing data into a single SOTA Markdown report.
    """
    report = []

    # 1. Header & Summary
    report.append("# 🏛️ System Design & Cost Estimate")
    report.append(f"\n**Architecture Pattern:** {design_data.architecture_summary}")
    report.append(f"**Total Monthly Estimate:** `${pricing_data.total_cost:,.2f}`")
    report.append("\n---")

    # 2. Architecture Details
    report.append("## 📦 System Components")
    report.append("| Component | Role | Justification |")
    report.append("| :--- | :--- | :--- |")
    for comp in design_data.components:
        report.append(f"| **{comp.name}** | {comp.role} | {comp.justification} |")

    # 3. Visual Representation
    if design_data.architecture_diagram_url:
        report.append("\n### 🖼️ Architecture Diagram")
        report.append(f"![Diagram]({design_data.architecture_diagram_url})")

    # 4. Financial Breakdown
    report.append("\n---")
    report.append("## 💰 Monthly Pricing Breakdown")
    report.append("| Service | Category | Monthly Cost |")
    report.append("| :--- | :--- | :--- |")

    # Sort pricing by most expensive first
    sorted_pricing = sorted(pricing_data.breakdown, key=lambda x: x.price, reverse=True)
    for item in sorted_pricing:
        price_str = f"${item.price:,.2f}" if item.price > 0 else "**FREE**"
        report.append(f"| {item.service} | {item.category} | {price_str} |")

    # 5. Risks & Bottlenecks
    if design_data.bottlenecks:
        report.append("\n---")
        report.append("## ⚠️ Identified Bottlenecks")
        for issue in design_data.bottlenecks:
            report.append(f"* {issue}")

    report.append("\n\n*Generated on: 2025-12-26 | Agentic SOTA Pipeline*")

    return "\n".join(report)

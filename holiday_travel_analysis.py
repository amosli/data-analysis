
# 重新生成图表 - 使用英文标签避免中文乱码
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 数据准备
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026])

wuyi_people = np.array([1.21, 1.34, 1.39, 1.47, 1.95, 1.15, 2.30, 1.60, 2.74, 2.95, 3.14, 3.25])
wuyi_revenue = np.array([793.0, 791.0, 871.6, 871.6, 1176.7, 475.6, 1132.3, 646.8, 1480.6, 1668.9, 1803.0, 1854.92])
wuyi_days = np.array([3, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 5])

shiyi_people = np.array([5.26, 5.93, 7.05, 7.26, 7.82, 6.37, 5.15, 4.22, 8.26, 7.65, 8.88, np.nan])
shiyi_revenue = np.array([4213.0, 4822.0, 5836.0, 5990.8, 6497.1, 4665.6, 3890.6, 2872.1, 7534.3, 7008.2, 8090.06, np.nan])
shiyi_days = np.array([7, 7, 7, 7, 7, 8, 7, 7, 8, 7, 8, 7])

# 计算指标
wuyi_percapita = wuyi_revenue / wuyi_people
shiyi_percapita = shiyi_revenue / shiyi_people
wuyi_daily_people = wuyi_people / wuyi_days
shiyi_daily_people = shiyi_people / shiyi_days
wuyi_daily_revenue = wuyi_revenue / wuyi_days
shiyi_daily_revenue = shiyi_revenue / shiyi_days
wuyi_daily_percapita = wuyi_percapita / wuyi_days
shiyi_daily_percapita = shiyi_percapita / shiyi_days

# CPI数据
cpi_yearly = np.array([1.4, 2.0, 1.6, 2.1, 2.9, 2.5, 0.9, 2.0, 0.2, 0.2, 0.2, 1.0])
cumulative_factor = np.ones(12)
for i in range(1, 12):
    cumulative_factor[i] = cumulative_factor[i-1] * (1 + cpi_yearly[i-1] / 100)

# 折现
wuyi_percapita_real = wuyi_percapita / cumulative_factor
shiyi_percapita_real = shiyi_percapita / cumulative_factor
wuyi_daily_percapita_real = wuyi_daily_percapita / cumulative_factor
shiyi_daily_percapita_real = shiyi_daily_percapita / cumulative_factor
wuyi_daily_revenue_real = wuyi_daily_revenue / cumulative_factor
shiyi_daily_revenue_real = shiyi_daily_revenue / cumulative_factor

# 创建图表 - 使用英文标签
fig, axes = plt.subplots(2, 3, figsize=(24, 16))
fig.suptitle('2015-2026 Golden Week Tourism Data Analysis\n(CPI Adjusted to 2015 Prices)', 
             fontsize=20, fontweight='bold', y=0.98)

color_wuyi = '#2E86AB'
color_shiyi = '#A23B72'
color_wuyi_real = '#5CB85C'
color_shiyi_real = '#F0AD4E'

# 图1: 出行人次
ax1 = axes[0, 0]
ax1.plot(years, wuyi_people, 'o-', color=color_wuyi, linewidth=2.5, markersize=8, label='May Day', zorder=5)
ax1.plot(years[:-1], shiyi_people[:-1], 's-', color=color_shiyi, linewidth=2.5, markersize=8, label='National Day', zorder=5)
for i, (x, y1, y2) in enumerate(zip(years, wuyi_people, shiyi_people)):
    if not np.isnan(y1):
        ax1.annotate(f'{y1:.2f}', (x, y1), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7, color=color_wuyi)
    if not np.isnan(y2):
        ax1.annotate(f'{y2:.2f}', (x, y2), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=7, color=color_shiyi)
ax1.set_title('Travelers (100 million)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Travelers (100M)', fontsize=12)
ax1.legend(fontsize=11, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xticks(years)

# 图2: 旅游收入
ax2 = axes[0, 1]
ax2.plot(years, wuyi_revenue, 'o--', color=color_wuyi, linewidth=2, markersize=6, label='May Day (Nominal)', zorder=5, alpha=0.7)
ax2.plot(years, wuyi_revenue / cumulative_factor, 'o-', color=color_wuyi_real, linewidth=2.5, markersize=8, label='May Day (Real)', zorder=5)
ax2.plot(years[:-1], shiyi_revenue[:-1], 's--', color=color_shiyi, linewidth=2, markersize=6, label='National Day (Nominal)', zorder=5, alpha=0.7)
ax2.plot(years[:-1], (shiyi_revenue / cumulative_factor)[:-1], 's-', color=color_shiyi_real, linewidth=2.5, markersize=8, label='National Day (Real)', zorder=5)
ax2.set_title('Revenue (100M yuan) - Nominal vs Real', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Revenue (100M yuan)', fontsize=12)
ax2.legend(fontsize=9, loc='upper left')
ax2.grid(True, alpha=0.3)
ax2.set_xticks(years)

# 图3: 人均消费
ax3 = axes[0, 2]
ax3.plot(years, wuyi_percapita, 'o--', color=color_wuyi, linewidth=2, markersize=6, label='May Day (Nominal)', zorder=5, alpha=0.7)
ax3.plot(years, wuyi_percapita_real, 'o-', color=color_wuyi_real, linewidth=2.5, markersize=8, label='May Day (Real)', zorder=5)
ax3.plot(years[:-1], shiyi_percapita[:-1], 's--', color=color_shiyi, linewidth=2, markersize=6, label='National Day (Nominal)', zorder=5, alpha=0.7)
ax3.plot(years[:-1], shiyi_percapita_real[:-1], 's-', color=color_shiyi_real, linewidth=2.5, markersize=8, label='National Day (Real)', zorder=5)
for i, (x, y1, y2) in enumerate(zip(years, wuyi_percapita_real, shiyi_percapita_real)):
    if not np.isnan(y1):
        ax3.annotate(f'{y1:.0f}', (x, y1), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7, color=color_wuyi_real)
    if not np.isnan(y2):
        ax3.annotate(f'{y2:.0f}', (x, y2), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=7, color=color_shiyi_real)
ax3.set_title('Per Capita Spending (yuan) - Nominal vs Real', fontsize=14, fontweight='bold')
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('Per Capita (yuan)', fontsize=12)
ax3.legend(fontsize=9, loc='upper left')
ax3.grid(True, alpha=0.3)
ax3.set_xticks(years)

# 图4: 日均出行人次
ax4 = axes[1, 0]
ax4.plot(years, wuyi_daily_people, 'o-', color=color_wuyi, linewidth=2.5, markersize=8, label='May Day', zorder=5)
ax4.plot(years[:-1], shiyi_daily_people[:-1], 's-', color=color_shiyi, linewidth=2.5, markersize=8, label='National Day', zorder=5)
for i, (x, y1, y2) in enumerate(zip(years, wuyi_daily_people, shiyi_daily_people)):
    if not np.isnan(y1):
        ax4.annotate(f'{y1:.2f}', (x, y1), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7, color=color_wuyi)
    if not np.isnan(y2):
        ax4.annotate(f'{y2:.2f}', (x, y2), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=7, color=color_shiyi)
ax4.set_title('Daily Travelers (100M/day)', fontsize=14, fontweight='bold')
ax4.set_xlabel('Year', fontsize=12)
ax4.set_ylabel('Daily Travelers (100M/day)', fontsize=12)
ax4.legend(fontsize=11, loc='upper left')
ax4.grid(True, alpha=0.3)
ax4.set_xticks(years)

# 图5: 日均消费金额
ax5 = axes[1, 1]
ax5.plot(years, wuyi_daily_revenue, 'o--', color=color_wuyi, linewidth=2, markersize=6, label='May Day (Nominal)', zorder=5, alpha=0.7)
ax5.plot(years, wuyi_daily_revenue_real, 'o-', color=color_wuyi_real, linewidth=2.5, markersize=8, label='May Day (Real)', zorder=5)
ax5.plot(years[:-1], shiyi_daily_revenue[:-1], 's--', color=color_shiyi, linewidth=2, markersize=6, label='National Day (Nominal)', zorder=5, alpha=0.7)
ax5.plot(years[:-1], shiyi_daily_revenue_real[:-1], 's-', color=color_shiyi_real, linewidth=2.5, markersize=8, label='National Day (Real)', zorder=5)
ax5.set_title('Daily Revenue (100M yuan/day) - Nominal vs Real', fontsize=14, fontweight='bold')
ax5.set_xlabel('Year', fontsize=12)
ax5.set_ylabel('Daily Revenue (100M yuan/day)', fontsize=12)
ax5.legend(fontsize=9, loc='upper left')
ax5.grid(True, alpha=0.3)
ax5.set_xticks(years)

# 图6: 日均人均消费 - 核心图表
ax6 = axes[1, 2]
ax6.plot(years, wuyi_daily_percapita, 'o--', color=color_wuyi, linewidth=2, markersize=6, label='May Day (Nominal)', zorder=5, alpha=0.7)
ax6.plot(years, wuyi_daily_percapita_real, 'o-', color=color_wuyi_real, linewidth=2.5, markersize=8, label='May Day (Real)', zorder=5)
ax6.plot(years[:-1], shiyi_daily_percapita[:-1], 's--', color=color_shiyi, linewidth=2, markersize=6, label='National Day (Nominal)', zorder=5, alpha=0.7)
ax6.plot(years[:-1], shiyi_daily_percapita_real[:-1], 's-', color=color_shiyi_real, linewidth=2.5, markersize=8, label='National Day (Real)', zorder=5)
for i, (x, y1, y2) in enumerate(zip(years, wuyi_daily_percapita_real, shiyi_daily_percapita_real)):
    if not np.isnan(y1):
        ax6.annotate(f'{y1:.0f}', (x, y1), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=7, color=color_wuyi_real)
    if not np.isnan(y2):
        ax6.annotate(f'{y2:.0f}', (x, y2), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=7, color=color_shiyi_real)
ax6.set_title('Daily Per Capita (yuan/person/day) - CPI Adjusted', fontsize=14, fontweight='bold')
ax6.set_xlabel('Year', fontsize=12)
ax6.set_ylabel('Daily Per Capita (yuan/person/day)', fontsize=12)
ax6.legend(fontsize=9, loc='upper left')
ax6.grid(True, alpha=0.3)
ax6.set_xticks(years)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('holiday_travel_cpi_adjusted.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ 英文标签图表已保存（无中文乱码）")

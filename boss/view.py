import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 处理工资列，提取工资范围的中位数作为代表值
def parse_salary(salary):
    salary = salary.lower().replace('k', '').replace('·', '').replace('薪', '')
    if '-' in salary:
        low, high = salary.split('-')
        try:
            return (int(low) + int(high)) / 2
        except ValueError:
            return None
    else:
        try:
            return int(salary)
        except ValueError:
            return None

# 读取CSV文件
file_path = 'boss.csv'  # 请替换为你的CSV文件路径
data = pd.read_csv(file_path)

data['salary'] = data['salary'].apply(parse_salary)

# 移除无法解析的工资数据
data = data.dropna(subset=['salary'])

# 绘制工资分布图
plt.figure(figsize=(10, 6))
sns.histplot(data['salary'], kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary (k)')
plt.ylabel('Frequency')
plt.show()

# 按城市显示平均工资
plt.figure(figsize=(12, 8))
sns.barplot(x='city', y='salary', data=data)
plt.title('Average Salary by City')
plt.xlabel('City')
plt.ylabel('Average Salary (k)')
plt.xticks(rotation=45)
plt.show()

# 绘制学历与工资关系图
plt.figure(figsize=(10, 6))
sns.boxplot(x='degree', y='salary', data=data)
plt.title('Salary by Degree')
plt.xlabel('Degree')
plt.ylabel('Salary (k)')
plt.show()

# 绘制工作经验与工资关系图
plt.figure(figsize=(10, 6))
sns.scatterplot(x='experience', y='salary', data=data)
plt.title('Salary by Experience')
plt.xlabel('Experience')
plt.ylabel('Salary (k)')
plt.show()

# 绘制公司规模与工资关系图
plt.figure(figsize=(10, 6))
sns.boxplot(x='size', y='salary', data=data)
plt.title('Salary by Company Size')
plt.xlabel('Company Size')
plt.ylabel('Salary (k)')
plt.show()

# 绘制不同福利与工资的关系图
plt.figure(figsize=(10, 6))
sns.boxplot(x='welfare', y='salary', data=data)
plt.title('Salary by Welfare')
plt.xlabel('Welfare')
plt.ylabel('Salary (k)')
plt.show()

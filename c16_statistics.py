import statistics

data = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7]

print(f"平均值: {statistics.mean(data)}")
print(f"中位数: {statistics.median(data)}")
print(f"众数: {statistics.mode([1, 2, 2, 3, 3, 3, 4])}")
print(f"方差: {statistics.variance(data)}")
print(f"标准差: {statistics.stdev(data)}")
print(f"几何平均数: {statistics.geometric_mean([1, 2, 4, 8])}")
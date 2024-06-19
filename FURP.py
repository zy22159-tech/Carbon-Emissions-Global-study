import netCDF4 as nc

ncfile = r'E:/temporary/FURP/Complete_TAVG_LatLong1.nc'
data = nc.Dataset(ncfile)
print(data.variables.keys(),'\n')
for i in data.variables.keys():
    print(i)
    print(data.variables[i])
    print('\n')


# 读取名为'temperature'的变量的数据
temperature_data = data.variables['temperature'][:]
print(temperature_data)  # 打印变量的数据

# 关闭文件
data.close()
import os

config_path="liquorix-package-5.18-8/linux-liquorix/debian/config/kernelarch-x86/config-arch-64"
patch_path="liquorix-package-5.18-8/linux-liquorix/debian/patches/zen/v5.18.12-lqx1.patch"
f = open("delete.txt","r") 
data1 = [line.strip('\n') for line in f.readlines()]#读取全部内容 ，并以列表方式返回
f.close()
d = open("insert.txt","r")
data2 = [line.strip('\n') for line in d.readlines()]#读取全部内容 ，并以列表方式返回
d.close()
for i in range(len(data1)):
    os.system(f"sed -i 's/{data1[i]}/{data2[i]}/g' {patch_path}")
os.system(f'''sed -i '/CONFIG_CC_VERSION_TEXT="gcc (GCC) 12.1.0"/d' {config_path}''')
os.system(f'''sed -i '/CONFIG_GCC_VERSION=120100/d' {config_path}''')
os.system(f'''sed -i '/CONFIG_CLANG_VERSION=0/d' {config_path}''')
os.system(f'''sed -i '/CONFIG_AS_VERSION=23800/d' {config_path}''')
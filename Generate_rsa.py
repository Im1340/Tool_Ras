import rsa
import time
(pubkey, privkey) = rsa.newkeys(1024)
print(pubkey.save_pkcs1().decode('utf-8'))
print(privkey.save_pkcs1().decode('utf-8'))
file = open('rsa.json','w+')
print("ok")
now_time = time.strftime('%b %d %Y %H:%M:%S', time.gmtime(time.time()))         #获取现在的时间
#写入文本
file.write(str(pubkey.save_pkcs1().decode('utf-8')))
file.write('\n')
file.write(str(privkey.save_pkcs1().decode('utf-8')))
file.write('\n')
file.write('输出的时间：')
file.write('\n')
file.write(now_time)
#写入结束
print('输出完毕')
file.close()        #关闭文件

# _*_ coding:utf-8 _*_
import jpype
import os.path
import hashlib,json
import data

def encrypt(encipherText):
    jvmPath = jpype.getDefaultJVMPath()
    jarpath = os.path.join(os.path.abspath('./java'))
    print (jarpath)
    jvmArg = "-Djava.class.path=" + jarpath
    print(jvmArg)
    if not jpype.isJVMStarted():
        jpype.startJVM(jvmPath, "-ea", jvmArg)                                        # 打开jvm
        jpype.java.lang.System.out.println("jvm is open!")                       # 判断jvm是否打开
        javaClass = jpype.JClass('AesCrypto1')                                   # 获取java加解密的class
        print (javaClass)
        secret_key = data.Config.SECRET_KEY                                         # marvin给的可用的secret
        encrypt_text = javaClass.Encrypt(encipherText,secret_key)                   # 把需要加密的参数传给class
        jpype.shutdownJVM()                                                         # 关闭jvm
        return encrypt_text

def decrypt(decipherText):
    jvmPath = jpype.getDefaultJVMPath()
    jarpath = os.path.join(os.path.abspath('./java'))
    print (jarpath)
    jvmArg = "-Djava.class.path=" + jarpath
    print(jvmArg)
    if not jpype.isJVMStarted():
        jpype.startJVM(jvmPath, "-ea", jvmArg)                                        # 打开jvm
        jpype.java.lang.System.out.println("jvm is open!")                       # 判断jvm是否打开
        javaClass = jpype.JClass('AesCrypto1')                                   # 获取java加解密的class
        print (javaClass)
        secret_key = data.Config.SECRET_KEY                                             # marvin给的可用的secret
        decrypt_text = javaClass.Decrypt(decipherText,secret_key)                   # 把需要解密的字符串传给class,得到解密字符串
        jpype.shutdownJVM()                                                         # 关闭jvm
        return decrypt_text
if __name__ == '__main__':
    encrypt()





# _*_ coding:utf-8 _*_
import crypt
import json

def encrypt():
   raw =  {
       "filterType": "all",
       "fuzzyItem": "CustomerName",
       "fuzzyVal": "", "pageSize": 20,
       "currentPage": 1,
       "searchDate": "",
       "logicType": "AND",
       "advanceConditions": [],
       "settingsId": "",
       "customSource": ""
   }
   raw = json.dumps(raw)
   encrypt_data = crypt.encrypt(raw)
   print (encrypt_data)

def decrypt():
    decrypt_str = 'JQ5t6L5WbN7uuHEqCYAUEwi1bkEB61ba3xWEpzKDHUMVMXZZUIZti4TAXkxyhkak'
    decrypt_data = crypt.decrypt(decrypt_str)
    print (decrypt_data)

if __name__ == '__main__':
    decrypt()

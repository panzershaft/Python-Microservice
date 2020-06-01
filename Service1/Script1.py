"""
This Python script will do the following:

1.Take JSON as a input, if not specified will use the default json
2.Convert the JSON to XML
3.Encrypt the XML
4.Transfer to a remote location
"""
import json as JS
import xml.etree.cElementTree as Et
from xml.etree import ElementTree

from cryptography.fernet import Fernet
from dicttoxml import dicttoxml


def script_runner(file_name="default_json.json"):
    with open(file_name) as json_format_file:
        json_data = JS.load(json_format_file)

    xml_obj = dicttoxml(json_data, custom_root='test', attr_type=False)
    xml_string = ElementTree.fromstring(xml_obj)
    final_xml = Et.ElementTree(xml_string)
    final_xml.write("plain_xml.xml")

    new_key = Fernet.generate_key()
    with open("secret_key.key", "wb") as key_file:
        key_file.write(new_key)

    with open("plain_xml.xml", "rb") as file:
        # read all file data
        file_data = file.read()
    key = open("secret_key.key", "rb").read()
    f = Fernet(key)
    encrypted_data = f.encrypt(file_data)

    with open("encrypted_xml.xml", "wb") as file:
        file.write(encrypted_data)


if __name__ == '__main__':
    script_runner()
# while True:
#         time.sleep(600000)
print("It ran")

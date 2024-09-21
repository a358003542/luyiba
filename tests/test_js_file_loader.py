text = """var abc={"status":"0","gameVer":"14.18","date":"2024-09-21 10:15:13"};/*  |xGv00|6f030ee3e5d6d41c77457f94ebf5471a */ var ddd = 2 ; var eee="90"
var fff=3.14;
"""

from luyiba.js_file_loader import js_file_loader



def test_js_file_loader():
    data = js_file_loader(text)

    assert type(data['abc']) == dict
    assert data['ddd'] == 2
    assert data['eee'] == '90'
    assert data['fff']  == 3.14
    assert type(data['fff']) == float   

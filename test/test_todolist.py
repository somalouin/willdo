# TODO: aaa
# TODO: bbb
# TODO: ccc
# TODO: ddd
# TODO: eee

from willdo.todo import *

def test_extract_todos():
  assert extract_todos('test/test_todolist.py') == []
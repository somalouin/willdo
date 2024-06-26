from willdo.todo import extract_todo_comments

def test_todo():
  # TODO - aaa
  # test comment
  # TODO - bbb
  # TODO - ccc
  # test comment
  # test comment
  # test comment
  # TODO - ddd
  # TODO - eee

  assert len(extract_todo_comments("test/test_todo.py")) == 4
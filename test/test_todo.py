from willdo.todo import extract_todo_comments


def test_todo():
  # TODO - aaa
  # test comment
  # TODO - bbb
  # TODO - ccc

  assert extract_todo_comments("test/test_todo.py") == [
    (1, "# TODO - aaa"),
    (3, "# TODO - bbb"),
    (4, "# TODO - ccc")
  ]
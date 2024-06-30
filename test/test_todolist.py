from willdo.todolist import *
def test_extract_todo_comments():
  # TODO: aaa
  # TODO: bbb
  # TODO: ccc
  # TODO: ddd
  # TODO: eee
  comments = search_file("test/test_todo.py")
  assert len(comments) == 1

def test_display_todo_comments(capsys):
  comments = {"test": [(1, 'TODO: aaa'), (2, 'TODO: bbb')]}
  display_todo_comments(comments)
  captured = capsys.readouterr()
  all_outputs = captured.out.split('\n')
  assert len(all_outputs) == 4
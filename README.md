# willdo

terminal command to help you plan you coding session

## installation

```py
python3 -m pip install -e .
```

## testing

```py
python3 -m pytest test
```

## features

### list 
create a todolist from code comments
- with a file or directory path
```py
python3 willdo list test/test_todo.py
```
- without a file path (whole project)
```py
python3 willdo list
```

### export
export a todolist from code comments as markdown
- with a file or directory path
```py
python3 willdo export test/test_todo.py
```
- without a file path (whole project)
```py
python3 willdo export
```

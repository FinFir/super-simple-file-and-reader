# filelib

def read_file(filename: str):
  with open(filename, "r") as f:
    content = f.read()
    return content

def write_file(filename: str, content: str):
  with open(filename, "w") as f:
    f.write(content)
    return content

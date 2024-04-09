def sort_strings(strings: list[str]):
  result = sorted(strings, key=len)
  result.sort(key=len, reverse=True)
  return result

def reverse(args):
  USAGE = """
    Type a string to obtain the reverse
  """
  inp = args.get("input", None)
  out = USAGE if inp is None else inp[::-1]
  return { "output": out }

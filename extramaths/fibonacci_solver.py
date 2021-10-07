def fibonacci(number):
  try:
      if number == 0 or number == 1:
          return 1
      else:
          total = fibonacci(number - 1) + fibonacci(number - 2)
      return total
  except:
      return 0

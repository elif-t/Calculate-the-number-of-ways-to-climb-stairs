def count_ways(n):
    # Base cases
    
    if n == 1:
      return n
    elif n == 2:
      return n
    elif n > 2:
      return (count_ways(n-1) + count_ways(n-2))


print(f'''{count_ways(1)}
{count_ways(2)}
{count_ways(3)}
{count_ways(4)}
{count_ways(5)}
''')

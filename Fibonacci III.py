def fibonacci(n, counts):
  # Atualiza o contador para a chamada atual da função
  counts[n] += 1
  
  # Casos base da recursão
  if n == 0:
    return 0
  if n == 1:
    return 1

  # Chamadas recursivas
  result = fibonacci(n-1, counts) + fibonacci(n-2, counts)
  return result

def main():
  n = int(input())
  counts = [0] * (n+1)
  result = fibonacci(n, counts)
  
  print(f"fibonacci({n}) = {result}.")
  for i in range(n+1):
    print(f"{counts[i]} chamada(s) a fibonacci({i}).")

main()


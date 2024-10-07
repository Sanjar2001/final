def count_ways(n):
    ways = set()
    
    def jump(distance, jumps):
        if distance == 0:
            ways.add(tuple(sorted(jumps)))
        elif distance > 0:
            for i in range(1, 4):
                jump(distance - i, jumps + (i,))
    
    jump(n, ())
    return len(ways)

# Пример использования
n = int(input())
result = count_ways(n)
print(result)
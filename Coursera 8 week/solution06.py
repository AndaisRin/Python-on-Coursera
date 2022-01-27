# На вход подаются две последовательности (a₁,…,an) и (b₁,…,bn) из 0 и 1.
# Вычислите последовательность из (c₁,…,cn), где каждая cᵢ=xor(aᵢ,bᵢ).

print(*map(lambda x, y: x ^ y, map(int, input().split()), map(int, input().split())))

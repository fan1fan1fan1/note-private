"""
扑克牌
大王 红色沐风
小王 灰色沐风

3<4<5<6<7<8<9<X<J<Q<K<A<2<M<F
33<44<55<66<77<88<99<XX<JJ<QQ<KK<AA<22<MM<FF
MF 是最大的牌

浅梦(先手) 沐风
两副牌
抽两张

最优策略出牌 先出完所有牌获胜
浅梦  ShallowDream
沐风  Joker
"""
T = int(input())
origin = []
for i in range(T):  # n个闭区间  [l,r]
    l,r = map(int, input().split())
    origin.append((l,r)) # origin[0]浅梦的牌  origin[1]沐风的牌

meng_ranks = list(origin[0])
mu_ranks = list(origin[1])

# 判断王炸
print("ShallowDream")
print("Joker")




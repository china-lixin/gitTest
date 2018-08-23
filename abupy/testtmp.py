# 设置100个赌徒
gamblers = 100
def casino(win_rate, win_once=1, loss_once=1, commission=0.01):
    """
        赌场：简单设定每个赌徒都有1000000元，并且每个赌徒都想在赌场玩10000000次，
        但是如果没钱了就别想玩了
        win_rate:   输赢的概率
        win_once:   每次赢的钱数
        loss_once:  每次输的钱数
        commission: 手续费这里简单设置为0.01 1%
    """
    my_money = 1000000
    play_cnt = 10000000
    commission = commission
    for _ in np.arange(0, play_cnt):
        # 使用伯努利分布，根据win_rate来获取输赢
        w = np.random.binomial(1, win_rate)
        if w:
            # 赢了 +win_once
            my_money += win_once
            else:
            # 输了 -loss_once
            my_money -= loss_once
            # 手续费
        my_money -= commission
        if my_money <= 0:
            # 没钱就别玩了，不赊账
            break
    return my_money
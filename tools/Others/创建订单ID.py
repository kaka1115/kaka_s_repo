def create_order(product_id, quantity, price, customer_age):
    """创建订单函数，包含多个断言验证"""

    # 验证商品ID格式（必须是字符串且以'PROD-'开头）
    assert isinstance(product_id, str) and product_id.startswith('PROD-'), \
        f"无效的商品ID: {product_id}，必须以'PROD-'开头的字符串" # 这个地方是要被抛出的Fasle。

    # 验证数量（必须是正整数）
    assert isinstance(quantity, int) and quantity > 0, \
        f"无效的数量: {quantity}，必须是正整数"

    # 验证价格（必须是正数且最多两位小数）
    assert isinstance(price, (int, float)) and price > 0, \
        f"无效的价格: {price}，必须是正数"
    assert round(price, 2) == price, \
        f"价格 {price} 最多只能有两位小数"

    # 验证客户年龄（如果购买特定商品需要成年）
    if product_id in ['PROD-100', 'PROD-200']:  # 假设这些是需要成年才能购买的商品
        assert customer_age >= 18, \
            f"购买{product_id}需要年满18岁，当前年龄: {customer_age}"

    # 计算订单总额
    total = quantity * price
    return f"订单创建成功，商品: {product_id}，数量: {quantity}，总额: ¥{total:.2f}"


# 测试用例1：所有条件都满足
try:
    print(create_order("PROD-101", 3, 99.99, 20))
except AssertionError as e:
    print(f"测试1失败: {e}")

# 测试用例2：商品ID格式错误
try:
    print(create_order(101, 3, 99.99, 20))
except AssertionError as e:
    print(f"测试2失败: {e}")

# 测试用例3：价格小数位数过多
try:
    print(create_order('PROD-101', 2, 19.999, 20))
except AssertionError as e:
    print(f"测试3失败: {e}")

# 测试用例4：购买限制商品但年龄不足
try:
    print(create_order('PROD-100', 1, 50, 17))
except AssertionError as e:
    print(f"测试4失败: {e}")

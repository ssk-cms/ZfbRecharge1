from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# ==========================================
# 定义省市县相关的模型
# ==========================================
class Province(models.Model):
    pname = models.CharField(max_length=40)

    def __str__(self):
        return "%s" % self.pname


class City(models.Model):
    cname = models.CharField(max_length=40)
    pid = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.cname


class Area(models.Model):
    aname = models.CharField(max_length=40)
    cid = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.aname


# =======================================================
# 下面是店铺相关的模型搭建
# =======================================================
class Shop(models.Model):
    """定义门店类型"""
    boss = models.ForeignKey(User)  # 老板
    name = models.CharField(max_length=15,verbose_name='姓名')
    province = models.CharField(max_length=20, default='',verbose_name='省份')
    city = models.CharField(max_length=20, default='',verbose_name='城市')
    area = models.CharField(max_length=20, default='',verbose_name='区/县')
    phone_number = models.CharField(max_length=11, default='',verbose_name='电话')
    email = models.CharField(max_length=30, default='',verbose_name='邮箱')
    business = models.CharField(max_length=100, default='',verbose_name='店铺名称')
    address = models.CharField(max_length=50, default='',verbose_name='地址')
    is_active = models.BooleanField(default=True,verbose_name='是否活动')

    def __str__(self):
        """显示门店名称"""
        return self.name

    class Meta:
        verbose_name = '店铺'
        verbose_name_plural = verbose_name

class Position(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,verbose_name='店铺名称')
    p_name = models.CharField(max_length=10, default='',verbose_name='职位名称')
    right = models.BooleanField(default=True,verbose_name='是否更改')
    is_del = models.BooleanField(default=False,verbose_name='是否删除')

    def __str__(self):
        return "%s" % self.p_name

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = verbose_name

class Employee(models.Model):
    """定义员工的类"""
    pid = models.ForeignKey(Position, on_delete=models.CASCADE)
    e_name = models.CharField(max_length=15,verbose_name='员工姓名')
    e_age = models.IntegerField(verbose_name='年龄')
    e_sex = models.BooleanField('性别',default=True)  # 默认为男
    e_tel = models.CharField('电话',max_length=15, default='')
    e_ctime = models.DateField('时间',auto_now_add=True)
    isActive = models.BooleanField('是否生效',default=True)  # 默认创建后生效

    def __str__(self):
        return "%s" % self.e_name

    class Meta:
        verbose_name = '员工'
        verbose_name_plural = verbose_name


# =========================================
#  以下是商品类别的模型搭建
# =========================================
class GoodType(models.Model):
    """定义商品类别"""
    name = models.CharField('商品类型',max_length=15)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,default="",verbose_name='店铺')
    t_sort_num = models.IntegerField('排序',default=1)
    discription = models.CharField('描述',max_length=30, default=None)
    is_active = models.BooleanField('是否激活',default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


# 这里其实可以做个分类的子分类(分类明细),有时间再做


class Good(models.Model):
    """这是商品管理的模型"""
    goods_type = models.ForeignKey(GoodType,verbose_name='商品类型')
    goods_name = models.CharField('商品名称',max_length=15)
    good_status = models.BooleanField('商品状态',default=True)
    origin_price = models.FloatField('进价')  # 加权价格
    sell_price = models.FloatField('销售价格')
    good_img = models.FileField('商品图片',upload_to='.goods/upload/', default=None)
    update_time = models.DateTimeField('更新时间',auto_now_add=True)
    is_delete = models.BooleanField('是否删除',default=False)
    g_sort_num = models.IntegerField('销售数量',default=1)
    g_disc = models.TextField('排序',default='')

    # 产地 place
    # 规格 size
    # 包装 package
    # 生产批号 pcode
    # 批准文号 pmcode
    # 供应商编号 pid
    # 状态 status

    def __str__(self):
        """返回物品名称"""
        return self.goods_name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name


# =====================================================
#  库存相关的模型搭建
# =====================================================

class Paytype(models.Model):
    """定义支付类型"""
    snum = models.IntegerField(default=1,verbose_name='支付类型')
    type_name = models.CharField(max_length=20,verbose_name='支付名称')

    def __str__(self):
        return u"%s" % self.type_name

    class Meta:
        verbose_name = '支付'
        verbose_name_plural = verbose_name


class Customer(models.Model):
    cname = models.CharField(max_length=50,verbose_name='顾客名称')
    province = models.CharField(max_length=20, default='',verbose_name='省份')
    city = models.CharField(max_length=20, default='',verbose_name='城市')
    area = models.CharField(max_length=20, default='',verbose_name='区/县')
    caddr = models.CharField(max_length=80,verbose_name='地址')
    lxr = models.CharField(max_length=20,verbose_name='联系人')
    lxrphone = models.CharField(max_length=20,verbose_name='电话')
    bank = models.CharField(max_length=50,verbose_name='银行')
    account = models.CharField(max_length=50,verbose_name='支付')
    email = models.CharField(max_length=50,verbose_name='邮箱')
    fax = models.CharField(max_length=20,verbose_name='传真')
    avaliable = models.BooleanField(default=True,verbose_name='是否激活')

    def __str__(self):
        return "%s" % self.cname

    class Meta:
        verbose_name = '顾客'
        verbose_name_plural = verbose_name


class Supplier(models.Model):
    """定义供应商模型"""
    company = models.CharField(max_length=30,verbose_name='公司')
    province = models.CharField(max_length=20, default='',verbose_name='省份')
    city = models.CharField(max_length=20, default='',verbose_name='城市')
    area = models.CharField(max_length=20, default='',verbose_name='区/县')
    s_addr = models.CharField(max_length=50,verbose_name='地址')
    linkman = models.CharField(max_length=15,verbose_name='联系人')
    tel = models.CharField(max_length=30,verbose_name='电话')
    bank = models.CharField(max_length=30,verbose_name='银行')
    card = models.CharField(max_length=20,verbose_name='卡号')
    email = models.CharField(max_length=30,verbose_name='邮箱')
    status = models.BooleanField(default=True,verbose_name='状态')

    def __str__(self):
        return "%s" % self.company

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = verbose_name


class BasicRecord(models.Model):
    """定义库存清单"""
    good = models.ForeignKey(Good,verbose_name='商品')
    shop = models.ForeignKey(Shop,verbose_name='店铺')
    in_num = models.IntegerField(default=0,verbose_name='进价')
    out_num = models.IntegerField(default=0,verbose_name='出价')
    gnum = models.IntegerField(default=0,verbose_name='数量')
    loss = models.IntegerField(default=0,verbose_name='损耗')
    income = models.IntegerField(default=0,verbose_name='收入')
    updater = models.ForeignKey(User)
    cdate = models.DateTimeField(auto_now=True,verbose_name='日期')
    is_del = models.BooleanField(default=True,verbose_name='是否删除')

    def __str__(self):
        return u"%s--%s" % (self.shop, self.good)

    class Meta:
        verbose_name = '库存清单'
        verbose_name_plural = verbose_name


class InRecord(models.Model):
    """库存增加记录/进货单"""
    good = models.ForeignKey(Good,verbose_name='商品')
    shop = models.ForeignKey(Shop,verbose_name='店铺')
    paytype = models.ForeignKey(Paytype,verbose_name='支付方式')
    num = models.IntegerField(default=0,verbose_name='数量')
    cost_price = models.FloatField(default=0,verbose_name='支出成本')
    operator = models.ForeignKey(Employee,verbose_name='员工')
    supplier = models.ForeignKey(Supplier,verbose_name='供应商')
    remark = models.CharField(max_length=50, default='',verbose_name='备注')
    in_date = models.DateTimeField(auto_now_add=True,verbose_name='日期')

    def cost(self):
        """支出成本"""
        paycost = self.num * self.cost_price
        return paycost

    class Meta:
        verbose_name = '进货单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return u"[进] %s--%s" % (self.shop, self.good)


class OutRecord(models.Model):
    """出库记录/出库单"""
    goods = models.ForeignKey(Good,verbose_name='商品')
    shop = models.ForeignKey(Shop,verbose_name='店铺')
    paytype = models.ForeignKey(Paytype,verbose_name='支付方式')
    sell_num = models.IntegerField(default=0,verbose_name='数量')
    sell_money = models.FloatField(default=0,verbose_name='售价')
    customer = models.ForeignKey(Customer,verbose_name='顾客')
    operator = models.ForeignKey(Employee,verbose_name='员工')
    out_date = models.DateTimeField(auto_now_add=True,verbose_name='日期')

    def get_receivable(self):
        """出库总销售额"""
        receivable = self.sell_num * self.sell_money
        return receivable

    class Meta:
        verbose_name = '出库记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return u"[出] %s--%s" % (self.shop, self.goods)


class BackRecord(models.Model):
    """定义退库单"""
    good = models.CharField(max_length=30,default='',verbose_name='商品')
    shop = models.CharField(max_length=30,default='',verbose_name='店铺')
    customer = models.ForeignKey(Customer,verbose_name='顾客')
    reason = models.CharField(max_length=80,verbose_name='理由')
    r_num = models.IntegerField(default=0,verbose_name='数量')
    r_money = models.IntegerField(default=0,verbose_name='金额')
    rtime = models.DateField(auto_now_add=True,verbose_name='时间')
    operator = models.ForeignKey(User,verbose_name='操作人')
    rmark = models.CharField(max_length=100,verbose_name='备注')
    outrecord = models.ForeignKey(OutRecord,null=True,verbose_name='支出')

    def __str__(self):
        return u"[退] %s--%s" % (self.customer, self.reason)

    class Meta:
        verbose_name = '退库单'
        verbose_name_plural = verbose_name

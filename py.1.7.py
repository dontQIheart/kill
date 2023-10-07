'''设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。具有的 公有成员函数是：初始化商品信息的构造函数__init__，
显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata
'''
class Product:
    def __init__(self,number,name,price,total_quantity,remain_quantity):
        self.__number = number
        self.__name = name
        self.__price = price
        self.__total_quantity = total_quantity
        self.__remain_quantity = remain_quantity
    def display(self):
        print("商品序号:",self.__number)
        print("商品名:",self.__name)
        print("商品单价:",self.__price)
        print("商品总数量:",self.__total_quantity)
        print("剩余数量:",self.__remain_quantity)
    def income(self):
        T = self.__price*(self.__total_quantity-self.__remain_quantity)
        return T
    def setdata(self,number,name,price,total_quantity,remain_quantity):
        self.__number = number
        self.__name = name
        self.__price = price
        self.__total_quantity = total_quantity
        self.__remain_quantity = remain_quantity
def main():
    p = Product(1,'x',10,100,50)
    p.display()
    print(p.income())
    print('进行修改')
    p.setdata(2,'y',10,50,10)
    p.display()
    print(p.income())
if __name__ == '__main__':
    main()

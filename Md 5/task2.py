class Pen:
    name="ban"

    def __init__(self,name,pries,color):
            self.name=name
            self.pries=pries
            self.color=color
            
f_Pen=Pen('matador',10,'green')
s_Pen=Pen('eco',20,'jus')
T_Pen=Pen('good_luck',30,'sada')
print(f_Pen.name,f_Pen.pries,f_Pen.color)
print(s_Pen.name,s_Pen.pries,s_Pen.color)
print(T_Pen.name,s_Pen.pries,T_Pen.color)
        
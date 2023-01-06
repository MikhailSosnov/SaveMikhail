from pyowm.owm import OWM
owm = OWM('7d2dc58c49406df6017063b97db5ae4c')
reg = owm.city_id_registry()

# print(reg)
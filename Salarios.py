Horas=8
Horas_trabajadas= 12
sueldo_base=(8*200)
if Horas_trabajadas <= 8:
    Pago=(sueldo_base)
    print(Pago)
if Horas_trabajadas > 8:
     Extra= (Horas_trabajadas-8)
     Pago= (Extra)*(sueldo_base+350)
     print(Pago)
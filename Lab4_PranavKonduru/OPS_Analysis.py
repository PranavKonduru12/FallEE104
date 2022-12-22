import ahkab
mycir = ahkab.Circuit('Simple Example Circuit')
mycir.add_vsource('V1', 'n1', mycir.gnd, dc_value=5)
mycir.add_resistor('R1', 'n1', 'n2', value=2)
mycir.add_resistor('R2', 'n2', mycir.gnd, value=3)
mycir.add_resistor('R3', 'n2', 'n3', value=5)
mycir.add_resistor('R4', 'n3', mycir.gnd, value=9)
mycir.add_resistor('R5', 'n3', 'n4', value=7)
mycir.add_resistor('R6', 'n4', mycir.gnd, value=10)
opa = ahkab.new_op()
r = ahkab.run(mycir, opa)['op']

print(r)

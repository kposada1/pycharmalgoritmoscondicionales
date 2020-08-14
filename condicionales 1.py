'''Un hombre desea saber cuanto dinero se genera por concepto de intereses sobre la
cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses siempre y
cuando estos excedan a $7000, y en ese caso desea saber cuanto dinero tendrá finalmente
en su cuenta.'''

p_int = int(input("Ingrese intereses: "))
cap = int(input("Ingrese inversion en el banco: "))
int= cap * p_int
if int > 7000:
    capf=cap+int
    print(f"Dinero que tendra finalmente en su cuenta {capf}")
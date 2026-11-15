# Aula 11 - Programa 1: controle de acesso por objeto (A01)
# Proposito: mostrar que autorizar e conferir, no servidor e a cada pedido, se ESTE usuario pode ver ESTE objeto.
pedidos = {101: {"dono": "ana",   "total": 250.0},
           102: {"dono": "bruno", "total":  80.0},
           103: {"dono": "ana",   "total":  15.0}}
perfis = {"ana": "cliente", "bruno": "cliente", "carla": "cliente"}

def pode_ver(usuario, id_pedido):
    pedido = pedidos.get(id_pedido)
    if pedido is None:
        return False                          # negar por padrao; nao revela se existe
    if perfis.get(usuario) == "atendente":
        return True                           # papel com permissao sobre todos
    return pedido["dono"] == usuario          # cliente so ve o que e dele

def ver_pedido(usuario, id_pedido):
    if not pode_ver(usuario, id_pedido):
        return "403 acesso negado"
    return f"200 pedido {id_pedido}: R$ {pedidos[id_pedido]['total']:.2f}"

for usuario, pid in [("ana", 101), ("ana", 102), ("bruno", 102), ("carla", 102), ("ana", 999)]:
    print(f"{usuario:<6} pede o pedido {pid}: {ver_pedido(usuario, pid)}")

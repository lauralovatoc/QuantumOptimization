import os
import osmnx as ox

# CONFIG
ox.settings.use_cache = True
ox.settings.log_console = True

grafos_dir = "dados/grafos"
os.makedirs(grafos_dir, exist_ok=True)
place_name = "Porto Alegre, Brazil"

def gerar_grafo_poa():
    print(f"\n📍 Baixando grafo de: {place_name}")

    # Obter o grafo de direção para a cidade inteira
    G = ox.graph_from_place(place_name, network_type="drive")

    print(f"Grafo carregado: {len(G.nodes)} nós, {len(G.edges)} arestas")

    # adicionar velocidades e tempos de viagem
    try:
        G = ox.add_edge_speeds(G)
        G = ox.add_edge_travel_times(G)
    except Exception as e:
        print(f"Aviso: não foi possível adicionar speeds/travel_times: {e}")

    # salvar grafo como GraphML
    graph_path = os.path.join(grafos_dir, "poa.graphml")
    ox.save_graphml(G, filepath=graph_path)
    print(f"💾 Grafo salvo: {graph_path}")


gerar_grafo_poa()
print("\n✅ Operação concluída: apenas Porto Alegre processado.")

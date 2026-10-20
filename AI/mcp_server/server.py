from mcp.server.mcpserver import MCPServer
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()

mcp=MCPServer("API_Django")

# Modelo de entrada da ferramenta de listagem de estabelecimentos.
class ListarEstabelecimentosInput(BaseModel):
    token: str

# Modelo de entrada da ferramenta de listagem de salas.
class ListarSalasInput(BaseModel):
    token: str
    id_estabe: int

# Modelo de entrada da ferramenta de listagem de jammers.
class ListarJammerInput(BaseModel):
    token: str
    id_estabe: int
    id_sala: int

# Modelo de entrada da ferramenta para desligar um jammer.
class DesligarJammerInput(BaseModel):
    token: str
    id_estabe: int
    id_sala: int

@mcp.tool()
def listar_estabelecimentos(entrada: ListarEstabelecimentosInput):
    try:
        url=os.getenv("URL")+'/get/estabelecimentos'
        header={"Authorization":entrada.token}
        respose=requests.get(url,headers=header,timeout=10)
        respose.raise_for_status()
        return respose.json()
    except Exception as e:
        return e.json()



@mcp.tool()
def listar_salas(entrada: ListarSalasInput):
    try:
        url=os.getenv("URL")+'/get/sala'
        header={"Authorization":entrada.token}
        parametro={"id_estabelecimento":entrada.id_estabe}
        respose=requests.get(url,headers=header,params=parametro,timeout=10)
        respose.raise_for_status()
        return respose.json()
    except Exception as e:
        return e.json()

@mcp.tool()
def listar_jammer(entrada: ListarJammerInput):
    try:
        url=os.getenv("URL")+'/get/jammer'
        header={"Authorization":entrada.token}
        parametro={"id_estabelecimento":entrada.id_estabe,"id_sala":entrada.id_sala}
        response=requests.get(url,headers=header,params=parametro,timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return e.json()

@mcp.tool()
def desligar_jammer(entrada: DesligarJammerInput):
    try:
        pass
    except Exception as e:
        return e.json()

mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=3000
    )

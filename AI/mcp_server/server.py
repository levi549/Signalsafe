from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()

mcp=FastMCP("API_Django")


@mcp.tool()
def listar_estabelecimentos(token):
    try:
        url=os.getenv("URL")+'/get/estabelecimentos'
        header={"Authorization":token}
        respose=requests.get(url,headers=header,timeout=10)
        respose.raise_for_status()
        return respose.json()
    except Exception as e:
        return e.json()



@mcp.tool()
def listar_salas(token,id_estabe):
    try:
        url=os.getenv("URL")+'/get/sala'
        header={"Authorization":token}
        parametro={"id_estabelecimento":id_estabe}
        respose=requests.get(url,headers=header,params=parametro,timeout=10)
        respose.raise_for_status()
        return respose.json()
    except Exception as e:
        return e.json()

@mcp.tool()
def listar_jammer(token,id_estabe,id_sala):
    try:
        url=os.getenv("URL")+'/get/jammer'
        header={"Authorization":token}
        parametro={"id_estabelecimento":id_estabe,"id_sala":id_sala}
        response=requests.get(url,headers=header,params=parametro,timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return e.json()

@mcp.tool()
def desligar_jammer(token,id_estabe,id_sala):
    try:
        pass
    except Exception as e:
        return e.json()
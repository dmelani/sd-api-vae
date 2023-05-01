from modules import shared, script_callbacks, sd_vae
from pydantic import BaseModel, Field
from typing import List

class VAEItem(BaseModel):
    name: str = Field(title="VAE name")
    filename: str = Field(title="File name")

def list_vaes():

    resp = [VAEItem(name=name, filename=filename) for name, filename in sd_vae.vae_dict.items()]
    
    return resp

def app_started(demo, app):
    app.add_api_route("/sd_api_vae/vae", list_vaes, methods=["GET"], response_model=List[VAEItem])

script_callbacks.on_app_started(app_started)

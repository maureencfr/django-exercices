from django.views import generic
import requests
import base64


# On utilise ici un TemplateView car il y on fait un Get et on n'a pas de formulaire
class IndexView(generic.TemplateView):

    
    # TODO lier la vue au template


    # On a besoin de redéfinir get_context_data pour passer plus d'informations au template.
    def get_context_data(self, **kwargs):
        # On récupère le contexte de base
        context = super().get_context_data(**kwargs)  
        
        # TODO Faire une requête get sur l'API cataas donnée dans le sujet
        
        
        # Pour l'utilisation spécifique de cette api, nous avons besoin d'encoder et de décoder les bytes recus en base 64 
        # afin d'afficher l'image.

        encoded_string = base64.b64encode(r.content)

        # On crée une variable "cat_image_base64" qui devient accessible dans le template 
        context["cat_image_base64"] = encoded_string.decode()

        # /!\ On retrouve, dans la balise image du template,  "data:image/png;base64, {{ cat_image_base64 }}" . 
        # La première partie est TRES importante pour que l'image s'affiche correctement. /!\
        
        return context

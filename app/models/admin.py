from sqladmin import ModelView

from . import Cadastre
from .constants import ADMIN_NAME, ADMIN_NAME_PLURAL


class CadastreAdmin(ModelView, model=Cadastre):
    column_list = [
        Cadastre.cadastre_number,
        Cadastre.latitude,
        Cadastre.longitude,
        Cadastre.answer,
        Cadastre.created_at,
    ]
    can_create = True
    can_edit = False
    can_delete = False
    can_view_details = True
    name = ADMIN_NAME
    name_plural = ADMIN_NAME_PLURAL
    column_searchable_list = [Cadastre.cadastre_number,]
    column_sortable_list = [
        Cadastre.cadastre_number,
        Cadastre.latitude,
        Cadastre.longitude,
        Cadastre.answer,
        Cadastre.created_at,
    ]
    search_query = [Cadastre.answer]
